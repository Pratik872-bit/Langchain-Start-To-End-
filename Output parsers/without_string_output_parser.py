from pydoc_data import topics
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate


load_dotenv()


model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

template1=PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']
)

template2=PromptTemplate(
    template='write a 15 line summary  on following text. /n{text}',
    input_variables=['text']
)
prompt1=template1.invoke({'topic':'blackhole'})
result=model.invoke(prompt1)
print("detailed report",result.content)
prompt2=template2.invoke({'text':result.content})

result1=model.invoke(prompt2)

print("Final summary:",result1.content)


