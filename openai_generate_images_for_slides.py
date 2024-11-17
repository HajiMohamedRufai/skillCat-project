import requests
import json
from openai import OpenAI

def generate_images_for_slides(starting_slide=1, last_slide=1):
    # Validate slide range
    if starting_slide > last_slide:
        print("Invalid slide range. Ensure starting_slide <= last_slide.")
        return

    # Initialize OpenAI client once
    client = OpenAI()

    # Load slides data once
    try:
        with open("slides.json", "r") as json_file:
            slides_dict = json.load(json_file)
    except FileNotFoundError:
        print("Error: 'slides.json' file not found.")
        return
    except json.JSONDecodeError:
        print("Error: Failed to parse 'slides.json'.")
        return

    # Loop through the slides and generate images
    for slide_num in range(starting_slide, last_slide + 1):
        # Check if the slide exists in the dictionary
        slide_key = f"slide_{slide_num}"
        if slide_key not in slides_dict:
            print(f"Warning: No prompt found for {slide_key}. Skipping.")
            continue

        prompt = slides_dict[slide_key]
        full_prompt = f"Generate an image that will engage learners reading besides the text delimited by triple backticks ```{prompt}```"
        print(full_prompt)
        
        # Generate the image
        image_url = generate_image(client, full_prompt, slide_num)
        if not image_url:
            continue
        
        # Download the image
        download_image(image_url, slide_num)

    print("All slides processed.")

def generate_image(client, prompt, slide_num):
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        return response.data[0].url
    except Exception as e:
        print(f"Error generating image for slide {slide_num}: {e}")
        return None

def download_image(image_url, slide_num):
    try:
        image_response = requests.get(image_url, timeout=10)
        image_response.raise_for_status()
        file_path = f"slide_{slide_num}.png"
        with open(file_path, 'wb') as f:
            f.write(image_response.content)
        print(f"Image downloaded and saved as '{file_path}'")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image for slide {slide_num}: {e}")
