import requests
import sendemail
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
load_dotenv()
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY") # Gemini API Key

model =init_chat_model(model="gemini-2.5-flash",
                       model_provider="google-genai",
                       api_key=GOOGLE_API_KEY
                       )
API_KEY=os.getev("API_KEY")
queryInput ="tesla"

url =("https://newsdata.io/api/1/latest"
      f"?apikey={API_KEY}"
      f"&q={queryInput}"
      "&language=en"
      )

response= requests.get(url)
print(response.json()) #json will give in proper output to process instead of text
content = response.json()
message ="subject: Today's News"
write_prompt =f"""Act as Email summarizer.Write a short paragraph analyzing those news.
in the second paragraph, tell me how its impacts the stock market.
Summarize the following news articles
{content["results"]}
"""
response_ai = model.invoke(write_prompt)
message = message+"\n\n" + response_ai.content + "\n\n"
message=message.encode("utf-8")
sendemail.send_email(message)
