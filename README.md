# 🤖 AI Meme Generator

A complete end-to-end AI-powered meme generation system that takes a text prompt, generates a creative meme caption using AI, produces a relevant image using generative models, and combines both into a finished meme.

---

## 🧠 Project Overview

This project combines natural language processing and generative AI to create funny, meaningful memes with minimal user input. The user provides a prompt such as “Lazy Monday,” and the system:

1. Generates a meme-style caption from the prompt.
2. Generates an AI image based on the same theme.

It uses a modular design and is deployable locally with the help of Flask and ngrok for public endpoints.

---

## 💡 Project Architecture & Workflow


### 🧩 Components

- **`caption_generator.py`**  
  Flask API that takes a prompt (`POST /caption`) and returns:
  - Meme-style caption
  - Image prompt  

- **`image_generator.py`**  
  Uses `stability-sdk` (Stable Diffusion) to generate an image based on the prompt.  
- **`test_post.py`**  
  A test script that sends prompts to the API and prints the generated caption/image prompt.

- **`tunnel.py` / `ngrok`**  
  Creates a secure public URL to your local Flask API for easy access and testing.

---

## 🚀 How to Run the Project

### 1. Install Requirements

```bash
pip install -r requirements.txt
```
## 📦 Requirements
---

## 🚀 How to Run the Project

### 1. Start the Caption Generator API

```bash
python caption_generator.py
```
This launches a local Flask server at:
http://localhost:5000

2. Start ngrok
Navigate to the folder where ngrok.exe is located and run:

```bash
.\ngrok.exe http 5000
```
this will generate a  HTTPS URL (e.g., https://xxxxx.ngrok-free.app)

3. Test the API
Edit test_post.py and replace the URL with your ngrok tunnel:

```python
url = "https://your-ngrok-url.ngrok-free.app/caption"
```
Then run:
```bash
python test_post.py
```
You’ll receive:

✅ A caption

✅ An image generation prompt

4. Generate the Meme
Update image_generator.py with the returned caption and image prompt, then run:

```bash
python image_generator.py
```

📸 Example Output
Prompt:
I didn’t mean to pour my heart out like this...

Generated Image Prompt:
A glass of milk with a broken heart drawn on it

🖼 Output:
A glass of milk with a heart icon, captioned at the bottom using PIL.


### OUTPUT IMAGE 


![ouput](https://github.com/user-attachments/assets/7d2689b6-7784-499c-bc8b-b3c25497387f)

---





