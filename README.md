🎨 Anime Avatar Generator

Generate anime-style portraits from text prompts or real human images using Stable Diffusion and the Counterfeit-V2.5 model — all within an intuitive Gradio interface.

This project enables users to create high-quality anime avatars from descriptive prompts or real photographs. It’s built using PyTorch, Hugging Face Diffusers, and Gradio, making it a powerful and user-friendly tool for digital artists, anime enthusiasts, and AI developers alike. Users can create anime-style art in two ways: from a text description using the Text-to-Anime feature or by transforming real photos using the Image-to-Anime pipeline.

Some of the key features of this application include full control over prompt guidance, the number of inference steps, image transformation strength, and seed settings to ensure reproducibility. The app also automatically detects CUDA-enabled GPUs to accelerate generation and leverages FP16 or FP32 precision as needed. The Gradio-powered interface makes the experience interactive and simple, even for non-technical users.

🧠 How It Works

The script loads the anime-style Counterfeit-V2.5 model via Hugging Face and supports two generation pipelines. In Text-to-Anime, users provide a creative description, such as “A cyberpunk girl with silver hair and neon eyes,” and the model generates an anime-style portrait from scratch. In Image-to-Anime, users can upload a real human image and optionally include a style prompt like “wearing school uniform with glowing eyes.” The model then transforms the original image into an anime rendition while maintaining key facial features. Inference is optimized to use GPU acceleration with automatic precision handling — FP16 on CUDA devices and FP32 on CPU fallback.

⚙️ Adjustable Parameters

The application exposes several parameters in the UI to fine-tune image generation. These include a Prompt field (used for both text and image modes), Gender selector (to guide aesthetics), Guidance Scale (which controls how strictly the model follows the prompt), and Inference Steps, which determines the rendering depth. For image uploads, there is a Strength parameter that adjusts how strongly the original photo is transformed, and a Seed input that lets users either randomize results or ensure repeatability by using a fixed number.

🧩 Dependencies

This project uses the following Python libraries:
1.torch
2.diffusers
3.transformers
4.gradio
5.Pillow
