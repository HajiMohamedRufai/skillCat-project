import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import json

def generate_images_for_slides(starting_slide=1, last_slide=1):
    if starting_slide > last_slide:
        print("Invalid slide range. Ensure starting_slide <= last_slide.")
        return
    
    # Check if GPU is available, else fallback to CPU
    DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"Using device: {DEVICE}")
    
    # Load the pre-trained Stable Diffusion model once
    print("Loading Stable Diffusion model...")
    pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
    pipe = pipe.to(DEVICE)
    
    # Load the slides data once before the loop
    try:
        with open("slides.json", "r") as json_file:
            slides_dict = json.load(json_file)
    except FileNotFoundError:
        print("Error: 'slides.json' file not found.")
        return
    except json.JSONDecodeError:
        print("Error: Failed to parse 'slides.json'.")
        return
    
    # Iterate through the slides
    for slide_num in range(starting_slide, last_slide + 1):
        slide_key = f"slide_{slide_num}"
        
        # Check if the slide exists in the dictionary
        if slide_key not in slides_dict:
            print(f"Warning: No prompt found for {slide_key}. Skipping.")
            continue
        
        prompt = slides_dict[slide_key]
        full_prompt = f"Generate an image that will engage learners reading besides the text delimited by triple backticks ```{prompt}```"
        
        try:
            # Generate the image
            print(f"Generating image for slide {slide_num}...")
            image = pipe(full_prompt, num_inference_steps=30).images[0]
            
            # Save the image to a file
            file_path = f"slide_{slide_num}.png"
            image.save(file_path)
            print(f"Image saved as '{file_path}'")
        except Exception as e:
            print(f"Error generating image for slide {slide_num}: {e}")
            continue
    
    print("All slides processed.")

