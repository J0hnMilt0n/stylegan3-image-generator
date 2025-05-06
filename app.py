from flask import Flask, request, send_file, jsonify, render_template
import hashlib
import subprocess
import os

app = Flask(__name__, template_folder='templates')

def prompt_to_seed(prompt: str) -> int:
    hash_object = hashlib.sha256(prompt.encode())
    return int(hash_object.hexdigest(), 16) % (2**32)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    print("Received data:", data)  # Debugging
    prompt = data.get('prompt', '')
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400
    seed = prompt_to_seed(prompt)
    outdir = 'outputs'
    os.makedirs(outdir, exist_ok=True)
    # Call StyleGAN3's gen_images.py to generate the image
    result = subprocess.run([
        'python', 'stylegan3/gen_images.py',
        '--outdir', outdir,
        '--trunc', '1',
        '--seeds', str(seed),
        '--network', 'stylegan3-t-ffhq-1024x1024.pkl'
    ], capture_output=True, text=True)
    print("Subprocess stdout:", result.stdout)  # Debugging
    print("Subprocess stderr:", result.stderr)  # Debugging
    if result.returncode != 0:
        return jsonify({'error': 'Image generation failed', 'details': result.stderr}), 500
    # Find the generated image file
    for fname in os.listdir(outdir):
        if fname.endswith('.png') and str(seed) in fname:
            img_path = os.path.join(outdir, fname)
            return send_file(img_path, mimetype='image/png')
    return jsonify({'error': 'Image not generated'}), 500

if __name__ == '__main__':
    app.run(debug=True)