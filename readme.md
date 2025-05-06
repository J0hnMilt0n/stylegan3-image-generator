# StyleGAN3 Image Generator

A web app to generate stunning AI-powered images from text prompts using StyleGAN3.

## Features

- Generate images from text prompts
- TailwindCSS for Responsive and modern UI

## Requirements

- Python 3.8+
- pip
- [Git](https://git-scm.com/)
- [curl](https://curl.se/)

## Installation

1. **Clone this repository:**

   ```sh
   git clone https://github.com/J0hnMilt0n/stylegan3-image-generator.git
   cd stylegan3-image-generator
   ```
2. **Clone the official StyleGAN3 repository:**

   ```sh
   git clone https://github.com/NVlabs/stylegan3.git
   ```
3. **Download the pretrained StyleGAN3 model:**

   ```sh
   curl -L 'https://api.ngc.nvidia.com/v2/models/org/nvidia/team/research/stylegan3/1/files?redirect=true&path=stylegan3-t-ffhq-1024x1024.pkl' -o 'stylegan3-t-ffhq-1024x1024.pkl'
   ```
4. **Create a virtual environment (recommended):**

   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```
5. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```
6. **Run the app:**

   ```sh
   python app.py
   ```
7. **Open your browser and go to:**

   ```
   http://127.0.0.1:5000
   ```

## Usage

- Enter a text prompt describing the image you want..
- Click "Generate Image".

## Project Structure

```
.
├── app.py
├── requirements.txt
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── stylegan3/                # Cloned StyleGAN3 repo
├── stylegan3-t-ffhq-1024x1024.pkl   # Downloaded pretrained model
└── readme.md
```

## Notes

- Ensure you have the required model weights and dependencies for StyleGAN3.
- For production, consider using a production-ready server (e.g., Gunicorn) and configuring environment variables.

---

**Enjoy generating images!**
