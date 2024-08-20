import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get('GITHUB_TOKEN')
print(token) # If the token is not loaded or load a old token, restart the IDE

if not token:
    print("GitHub token not found. Please make sure it's set correctly in your .env file.")
else:
    url = "https://api.github.com/user"  # Endpoint that requires authentication
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("Token is valid. Here's your user information:")
        print(response.json())
    else:
        print(f"Failed to authenticate. Status Code: {response.status_code}")
        print("Response:", response.json())