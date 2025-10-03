import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key= os.getenv("NEW_API_KEY")
url = os.getenv("URL")


request = requests.get(url)
content = request.json()

articles = content["articles"]
for article in articles:
    print(article["title"])
    print(article["description"])