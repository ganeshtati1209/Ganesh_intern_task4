import torch
from torchvision import transforms
from diffusers import StableDiffusionImg2ImgPipeline
from PIL import Image
import sys


model_id = "runwayml/stable-diffusion-v1-5"  # Stable Diffusion for Image-to-Image tasks
device = "cuda" if torch.cuda.is_available() else "cpu"


pipe = StableDiffusionImg2ImgPipeline.from_pretrained(model_id, torch_dtype=torch.float32).to(device)
pipe.enable_attention_slicing()  # ✅ Reduce memory usage for better performance

def load_image(image_path):
    """
    Load and preprocess an image from the given file path.
    """
    image = Image.open(image_path).convert("RGB")
    transform = transforms.Compose([
        transforms.Resize((512, 512)),  # Resize for the model
        transforms.ToTensor()
    ])
    return transform(image).unsqueeze(0).to(device)

def translate_image(image_path, prompt="A realistic version of this image"):
    """
    Perform image-to-image translation using Stable Diffusion (Pix2Pix style).
    """
    image = Image.open(image_path).convert("RGB")

    # Generate image using the model
    result = pipe(prompt=prompt, image=image, strength=0.75, guidance_scale=7.5).images[0]

    # Save and display the result
    output_path = "translated_image.png"
    result.save(output_path)
    result.show()

    print(f"Image translation completed! Saved as '{output_path}'")

if __name__ == "__main__":
    input_image_path = "img.png"
    translate_image(input_image_path)
