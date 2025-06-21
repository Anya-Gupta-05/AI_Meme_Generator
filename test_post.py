import requests

# Your public ngrok URL
url = "https://d2d2-2405-201-301a-30f8-899-c22c-d4e5-58c6.ngrok-free.app/caption"

# JSON payload
data = {
    "prompt": "Lazy day"
}

# Send POST request
response = requests.post(url, json=data)

# Show result

print("Status Code:", response.status_code)
print("Raw Response Text:", response.text)

