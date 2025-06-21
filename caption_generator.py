from flask import Flask, request, jsonify
import subprocess
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def generate_caption(prompt):
    mistral_prompt = f"""
You are a witty meme bot. Given the topic: "{prompt}", respond in **exactly** this format:

Caption: <caption text for meme image>
Image Prompt: <prompt to generate the meme image>

Only use this format. Do not include anything else.
"""
    result = subprocess.run(
        ['ollama', 'run', 'mistral'],
        input=mistral_prompt,
        text=True,
        capture_output=True,
        encoding='utf-8'
    )

    output = result.stdout.strip()

    # Parse Caption and Image Prompt from output
    caption = ""
    image_prompt = ""

    for line in output.splitlines():
        if line.lower().startswith("caption:"):
            caption = line.split(":", 1)[1].strip().strip('"')
        elif line.lower().startswith("image prompt:"):
            image_prompt = line.split(":", 1)[1].strip().strip('"')

    return caption, image_prompt


@app.route("/caption", methods=["POST"])
def caption():
    data = request.get_json()
    prompt = data.get("prompt", "")
    caption, image_prompt = generate_caption(prompt)
    return jsonify({
        "caption": caption,
        "image_prompt": image_prompt
    })


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "cli":
        user_input = input("Enter meme theme: ")
        print("Generated Caption:", generate_caption(user_input))
    else:
        app.run(port=5000)
