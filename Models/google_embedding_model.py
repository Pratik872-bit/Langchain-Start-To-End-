from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()


embedding=GoogleGenerativeAIEmbeddings(model='gemini-embedding-001',dimensions=32)

result=embedding.embed_query("what is your name  ")

print(str(result))




