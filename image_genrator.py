import requests
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
from PIL import Image
import io

# Step 1: Get image prompt and caption from your Flask/Ollama
flask_url = "http://localhost:5000/caption"
user_prompt = "Lazy Monday"

response = requests.post(flask_url, json={"prompt": user_prompt})
data = response.json()

caption = data["caption"]
image_prompt = data["image_prompt"]
print("Caption:", caption)
print("Image Prompt:", image_prompt)

# Step 2: Generate image from Stability AI
stability_api = client.StabilityInference(
    key="sk-",  # Add your API Key here
    verbose=True,
)

answers = stability_api.generate(
    prompt=image_prompt,
    seed=42,
    steps=30,
    cfg_scale=8.0,
    width=512,
    height=512,
    samples=1,
)

# Step 3: Display image
for resp in answers:
    for artifact in resp.artifacts:
        if artifact.type == generation.ARTIFACT_IMAGE:
            img = Image.open(io.BytesIO(artifact.binary))
            img.show()  # or save with img.save("meme.png")

def add_caption_to_image(image_path, caption, output_path="output_meme.png"):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    # Load font
    try:
        font_path = "C:\\Windows\\Fonts\\arial.ttf"
        if not os.path.exists(font_path):
            font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        font = ImageFont.truetype(font_path, size=32)
    except IOError:
        font = ImageFont.load_default()

    # Calculate text size and position
    text_width, text_height = draw.textsize(caption, font=font)
    x = (image.width - text_width) / 2
    y = image.height - text_height - 20

    # Draw background rectangle for caption
    draw.rectangle([(x - 10, y - 10), (x + text_width + 10, y + text_height + 10)], fill="white")
    draw.text((x, y), caption, font=font, fill="black")

    image.save(output_path)
    return output_path
if __name__ == "__main__":
    user_prompt = "Lazy Monday"

    print("Generating caption...")
    caption = get_caption(user_prompt)
    print("Caption:", caption)

    print("Generating image...")
    image_path = generate_image(f"{caption} – digital illustration")
    if image_path:
        print("Overlaying caption...")
        final_path = add_caption_to_image(image_path, caption)
        print(f"✅ Meme saved to {final_path}")
    else:
        print("❌ Image generation failed.")