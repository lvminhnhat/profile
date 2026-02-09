import os
import time
from google import genai
from google.genai import types

def generate_image(client, prompt, output_path):
    print(f"Generating {output_path}...")
    try:
        # diverse modern tech abstract style
        enhanced_prompt = f"{prompt}, modern vector art, 3d render, unspalsh style, wallpaper, high definition, abstract technology background"
        
        response = client.models.generate_images(
            model='imagen-3.0-generate-001',
            prompt=enhanced_prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
                aspect_ratio="16:9",
                include_rai_reason=True,
                output_mime_type="image/png"
            )
        )
        if response.generated_images:
            image = response.generated_images[0]
            with open(output_path, "wb") as f:
                f.write(image.image.image_bytes)
            print(f"Saved to {output_path}")
        else:
            print(f"No image generated for {output_path}")
            
    except Exception as e:
        print(f"Error generating {output_path}: {e}")

# Check API Key
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY not set")
    exit(1)

client = genai.Client(api_key=api_key)

tasks = [
    {
        "path": "/home/minnyat/profile/public/assets/voicetype-cover.png",
        "prompt": "Abstract minimalist tech illustration, AI voice recognition, sound waves becoming digital text, glowing microphone silhouette, dark purple and violet neon lighting, isometric 3D style, clean lines, high quality, 4k, dark background, no text"
    },
    {
        "path": "/home/minnyat/profile/public/assets/filefilter-cover.png",
        "prompt": "Abstract minimalist tech illustration, image processing pipeline, grid of floating photographs being organized, digital filters, geometric shapes, cyan and teal blue lighting, glassmorphism style, modern, clean, 4k, no text"
    },
    {
        "path": "/home/minnyat/profile/public/assets/aicontent-cover.png",
        "prompt": "Abstract minimalist tech illustration, artificial intelligence brain, neural network nodes connecting, dual processing cores, digital content stream, emerald green and cyan glowing lines, futuristic, cybernetic, high contrast, 4k, no text"
    },
    {
        "path": "/home/minnyat/profile/public/assets/ghcagent-cover.png",
        "prompt": "Abstract minimalist tech illustration, coding automation, terminal command lines floating in space, digital robot assistant silhouette, abstract code syntax, orange and amber warm lighting, dark mode aesthetic, sleek, professional, 4k, no text"
    }
]

for task in tasks:
    generate_image(client, task["prompt"], task["path"])
    time.sleep(2) # Slight delay to be nice to rate limits
