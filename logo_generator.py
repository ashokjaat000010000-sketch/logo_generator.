import os

from openai import OpenAI
import requests
from PIL import Image
from io import BytesIO

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise EnvironmentError(
        "OPENAI_API_KEY not set. Set it as an environment variable (or in a .env file) before running this script."
    )

client = OpenAI(api_key=api_key)

def generate_logo(brand_name, style):

    prompt = f"Minimal modern logo for brand {brand_name}, style {style}, vector logo, white background"

    result = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1024"
    )

    image_url = result.data[0].url

    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))

    filename = f"{brand_name}_logo.png"
    img.save(filename)

    print("Logo saved as:", filename)


brand = input("Enter brand name: ")
style = input("Enter logo style: ")

generate_logo(brand, style)