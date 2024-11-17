from diffusers import StableDiffusionPipeline
from PIL import Image

def generate_image(prompt, num_inference_steps=30):
    # Check if GPU is available, else fallback to CPU
    DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
    # print(DEVICE)

    # Load the pre-trained Stable Diffusion model
    pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
        # Move the model to the appropriate device (GPU or CPU)
    pipe = pipe.to(DEVICE)
    prompt = f"Generate an image that will engage learners reading besides that text delimited by triple backticks ```{prompt}```"
    # Generate an image based on the prompt and number of inference steps
    image = pipe(prompt, num_inference_steps=num_inference_steps).images[0]
    
    # Return the generated image
    return image