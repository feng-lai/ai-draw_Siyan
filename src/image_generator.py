import sys
import os
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

def generate_image(prompt, output_path):
    try:
        # Set up proxy if needed (uncomment if you need proxy)
        os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
        os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"
        
        # Initialize the client with your API key
        # Replace with your actual API key or use environment variable
        api_key = os.environ.get("GEMINI_API_KEY", "AIzaSyAy5-_q94y8DeBkoBFG9oTXPF4dbDD2cBQ")
        client = genai.Client(api_key=api_key)
        
        print(f"Generating image for prompt: {prompt}")
        
        # Generate content with image
        response = client.models.generate_content(
            model="gemini-2.0-flash-preview-image-generation",
            contents=prompt,
            config=types.GenerateContentConfig(response_modalities=["TEXT", "IMAGE"]),
        )
        
        # Process the response
        image_saved = False
        for part in response.candidates[0].content.parts:
            if part.text is not None:
                print(f"Generated text: {part.text}")
            elif part.inline_data is not None:
                # Save the generated image
                image = Image.open(BytesIO(part.inline_data.data))
                image.save(output_path)
                print(f"Image saved to: {output_path}")
                image_saved = True
                break
        
        if not image_saved:
            print("No image data found in response")
            sys.exit(1)
            
        print("Image generation completed successfully")
        
    except Exception as e:
        print(f"Error generating image: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python image_generator.py <prompt> <output_path>")
        sys.exit(1)
    
    prompt = sys.argv[1]
    output_path = sys.argv[2]
    
    generate_image(prompt, output_path)
