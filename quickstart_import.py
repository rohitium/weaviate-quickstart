import weaviate
from weaviate.classes.init import Auth

import requests, json, os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Best practice: store your credentials in environment variables
wcd_url = os.environ["WCD_URL"]
wcd_api_key = os.environ["WCD_API_KEY"]
cohere_api_key = os.environ["COHERE_APIKEY"]

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=wcd_url,                                    # Replace with your Weaviate Cloud URL
    auth_credentials=Auth.api_key(wcd_api_key),             # Replace with your Weaviate Cloud key
    headers={"X-Cohere-Api-Key": cohere_api_key},           # Replace with your Cohere API key
)

resp = requests.get(
    "https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json"
)
data = json.loads(resp.text)

questions = client.collections.get("Question")

with questions.batch.dynamic() as batch:
    for d in data:
        batch.add_object({
            "answer": d["Answer"],
            "question": d["Question"],
            "category": d["Category"],
        })

client.close()  # Free up resources