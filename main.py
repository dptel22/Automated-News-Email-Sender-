import requests
import os
from dotenv import load_dotenv
from send_email import send_email

load_dotenv()

api_key= os.getenv("NEW_API_KEY")
url = os.getenv("URL")


request = requests.get(url)
content = request.json()

articles = content["articles"]

body = ""
for article in articles:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

send_email(message=body)