
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()


document=[
    "pratik vijay naik is my name where he is leave in sangli",
    "virat kohli is cricketer",
    "elon musk is scientist"
]

query="pratik "
embedding=GoogleGenerativeAIEmbeddings(model='gemini-embedding-001')

document_embedd=embedding.embed_documents(document)
query_embedd=embedding.embed_query(query)

score=cosine_similarity([query_embedd],document_embedd)[0]

index,score=sorted(list(enumerate(score)),key=lambda x:x[1])[-1]
print(query)
print(document[index])
print(score)