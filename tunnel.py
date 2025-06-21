from pyngrok import ngrok

# Start a tunnel to the Flask app
public_url = ngrok.connect(5000)
print("🔗 Public URL:", public_url)
  #https://e6cf-49-36-26-245.ngrok-free.app