import torch
from diffusers import DiffusionPipeline, StableDiffusionImg2ImgPipeline
import gradio as gr
from PIL import Image

# Detect device
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Load anime-style models
def load_models():
    model_id = "gsdf/Counterfeit-V2.5"

    text2img_pipe = DiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float16 if device == "cuda" else torch.float32,
        safety_checker=None
    ).to(device)

    img2img_pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float16 if device == "cuda" else torch.float32,
        safety_checker=None
    ).to(device)

    return text2img_pipe, img2img_pipe

print("Loading models...")
text2img_pipe, img2img_pipe = load_models()
print("Models loaded!")

# Text-to-Anime generation
def text_to_anime(prompt, gender, guidance_scale=8.5, num_steps=70, seed=-1):
    # Anime prompt (without Ghibli words)
    gender_prompt = "male" if gender == "Male" else "female"
    anime_prompt = (
        f"{prompt}, anime portrait, {gender_prompt}, beautiful face, soft lighting, ultra detailed, "
        "sharp focus, vibrant colors, high quality, cinematic, masterpiece"
    )

    negative_prompt = (
        "low quality, bad anatomy, blurry, distorted, watermark, low res, 3d, cartoon, photo, jpeg artifacts"
    )

    generator = torch.Generator(device=device).manual_seed(seed) if seed != -1 else None

    with torch.autocast("cuda" if device == "cuda" else "cpu"):
        image = text2img_pipe(
            prompt=anime_prompt,
            negative_prompt=negative_prompt,
            guidance_scale=guidance_scale,
            num_inference_steps=num_steps,
            height=768,
            width=768,
            generator=generator
        ).images[0]

    return image

# Image-to-Anime transformation
def image_to_anime(input_image, prompt="", gender="Male", strength=0.8, guidance_scale=8.5, num_steps=70, seed=-1):
    if input_image is None:
        return None

    width, height = input_image.size
    max_size = 768
    if width > height:
        new_width = max_size
        new_height = int(height * max_size / width)
    else:
        new_height = max_size
        new_width = int(width * max_size / height)

    input_image = input_image.resize((new_width, new_height), Image.LANCZOS)

    base_prompt = prompt if prompt.strip() else "anime portrait"
    gender_prompt = "male" if gender == "Male" else "female"
    anime_prompt = (
        f"{base_prompt}, anime style, {gender_prompt}, highly detailed face, vibrant colors, smooth shading, digital art"
    )

    negative_prompt = (
        "blurry, lowres, distorted, jpeg artifacts, bad anatomy, poorly drawn face, photo, 3d"
    )

    generator = torch.Generator(device=device).manual_seed(seed) if seed != -1 else None

    with torch.autocast("cuda" if device == "cuda" else "cpu"):
        image = img2img_pipe(
            prompt=anime_prompt,
            negative_prompt=negative_prompt,
            image=input_image,
            strength=strength,
            guidance_scale=guidance_scale,
            num_inference_steps=num_steps,
            generator=generator
        ).images[0]

    return image

# Gradio Interface
def create_interface():
    with gr.Blocks(title="Anime Avatar Generator") as app:
        gr.Markdown("# 🎨 Anime Avatar Generator")

        with gr.Tab("🖋 Text to Anime"):
            with gr.Row():
                with gr.Column():
                    text_input = gr.Textbox(label="Describe the anime avatar", lines=3,
                                            placeholder="Example: A cool anime boy with spiky hair and blue eyes")
                    gender_selection = gr.Radio(label="Select Gender", choices=["Male", "Female"], value="Male")
                    guidance = gr.Slider(5.0, 15.0, value=8.5, step=0.5, label="Guidance Scale")
                    steps = gr.Slider(40, 100, value=70, step=5, label="Steps")
                    seed = gr.Slider(-1, 2147483647, value=-1, step=1, label="Seed (-1 for random)")
                    text_button = gr.Button("Generate", variant="primary")
                with gr.Column():
                    text_output = gr.Image(label="Anime Avatar Output")

            text_button.click(fn=text_to_anime, inputs=[text_input, gender_selection, guidance, steps, seed], outputs=text_output)

        with gr.Tab("🖼 Image to Anime"):
            with gr.Row():
                with gr.Column():
                    image_input = gr.Image(label="Upload a human image", type="pil")
                    image_prompt = gr.Textbox(label="Optional extra style prompt",
                                              placeholder="Example: glowing eyes, school uniform")
                    gender_selection_img = gr.Radio(label="Select Gender", choices=["Male", "Female"], value="Male")
                    strength = gr.Slider(0.3, 0.9, value=0.8, step=0.05, label="Transformation Strength")
                    img_guidance = gr.Slider(5.0, 15.0, value=8.5, step=0.5, label="Guidance Scale")
                    img_steps = gr.Slider(40, 100, value=70, step=5, label="Steps")
                    img_seed = gr.Slider(-1, 2147483647, value=-1, step=1, label="Seed (-1 for random)")
                    img_button = gr.Button("Transform", variant="primary")
                with gr.Column():
                    image_output = gr.Image(label="Anime Transformed Image")

            img_button.click(
                fn=image_to_anime,
                inputs=[image_input, image_prompt, gender_selection_img, strength, img_guidance, img_steps, img_seed],
                outputs=image_output
            )

        gr.Markdown("""
        ## 🔧 Tips:
        - Use full-body or face-only prompts for better detail.
        - Higher guidance = more stylized, lower = more realism.
        - Lower strength = more original image features preserved.
        - Use anime terms like "bishoujo", "shonen", "cyberpunk", etc.
        """)

    return app

# Launch app
app = create_interface()
app.launch(share=True)