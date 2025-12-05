from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

result=model.invoke("what is large language models plane formating is required ")

print(result.content)



