import requests
import json

# URL of your Flask app
url = "http://127.0.0.1:5000/predict"

# Create the payload with your message
data = {
    "message": "Hello, is this spam?"
}

# Send the POST request
response = requests.post(url, json=data)

# Print the response from the server
print("Response Status Code:", response.status_code)
print("Response JSON:", response.json())
