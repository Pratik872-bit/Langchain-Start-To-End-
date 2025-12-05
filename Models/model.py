import langchain
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
import os

from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")


llm=HuggingFaceEndpoint(
         repo_id="moonshotai/Kimi-K2-Instruct-0905",
        huggingfacehub_api_token=api_key)


model=ChatHuggingFace(llm=llm,temprature=0.1,max_completion_tokens=5)

response=model.invoke("what is the model BLUE score")
                     
print(response.content)

