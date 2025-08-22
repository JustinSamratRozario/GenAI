# 🎨 Anime Avatar Generator

> Generate anime-style portraits from text prompts or real human images using Stable Diffusion and the Counterfeit-V2.5 model — with a clean, intuitive Gradio interface.

This project allows users to create high-quality anime avatars from descriptions or photos using advanced AI models. Built with PyTorch, Hugging Face's Diffusers, and Gradio, it's ideal for digital artists, anime fans, and developers experimenting with generative AI.

---

## ✨ Features

- 🖋 **Text-to-Anime**: Convert detailed text prompts into anime-style portraits.
- 🖼 **Image-to-Anime**: Upload a real image and transform it into anime art.
- ⚙️ Adjustable Parameters:
  - Prompt guidance scale
  - Inference steps
  - Image transformation strength
  - Seed control for reproducibility
- 🚀 GPU support via PyTorch with automatic CUDA/CPU detection
- 💡 Built-in prompt engineering for anime aesthetics

---

## 📸 Demo Preview

| Mode              | Input                                | Output                                |
|-------------------|---------------------------------------|----------------------------------------|
| Text-to-Anime     | "Cool anime boy with spiky hair..."   | ![text_output](examples/output1.png)   |
| Image-to-Anime    | ![real_photo](examples/input1.jpg)    | ![anime_photo](examples/output2.png)   |

> Add your own samples in `/examples` to showcase outputs.

---

## 🛠️ Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/IMAGEtoAnime.git
cd IMAGEtoAnime
2. Create and Activate Virtual Environment (Recommended)
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Run the Application
bash
Copy code
python IMAGEtoAnime.py
The app will launch locally in your browser. If share=True, you'll receive a public Gradio link.

⚙️ Parameters Overview
Parameter	Mode	Description
prompt	Text & Image	Description for style and character generation
gender	Text & Image	Applies gender-based prompt optimization (male/female)
guidance_scale	Text & Image	Controls prompt influence on output (5.0–15.0)
num_steps	Text & Image	Number of inference steps (40–100)
strength	Image-to-Anime	Controls how much the image is altered (0.3–0.9)
seed	Text & Image	Use -1 for random; set a value for repeatable results

💡 Prompt Tips
Use rich, descriptive prompts:
"A girl with pink hair, wearing a school uniform, standing under sakura trees, anime style"

Use anime keywords:
bishoujo, shonen, mecha, glowing eyes, cyberpunk, cel shading

Lower strength values retain more of the original image (Image-to-Anime mode)

📁 Project Structure
bash
Copy code
IMAGEtoAnime/
├── IMAGEtoAnime.py        # Main application script
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── LICENSE                # (Optional) License file
└── examples/              # Input/output demo images
🧠 Tech Stack
Stable Diffusion 1.5

Counterfeit-V2.5 Model (for anime-style generation)

Hugging Face Diffusers

PyTorch

Gradio
