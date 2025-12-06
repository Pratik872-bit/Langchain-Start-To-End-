from itertools import chain
from pydoc_data import topics
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

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

parser=StrOutputParser()

chain_1=template1 |model|parser|template2|model|parser
result=chain_1.invoke({'topic':'blackhole'})
print(result)