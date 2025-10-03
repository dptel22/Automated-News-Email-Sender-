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
for article in articles[:20]:
    if article["title"] is not None:
        body = ("Subject: Today's news" + '\n'+ body + article["title"] + "\n" +
               article["description"] + '\n' + article["url"]+ 2*"\n")

send_email(message=body)