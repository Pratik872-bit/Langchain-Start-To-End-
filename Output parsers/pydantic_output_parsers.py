
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
load_dotenv()
from proto import Field
from pydantic import BaseModel,Field


model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

class Person(BaseModel):
    name:str=Field(description='name of the person')
    age:int =Field(gt=18,description='age of the person ')
    city:str=Field(description='name of the city the person belong')
    
parser=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(
    template='give me the name,age,and cit of a fictional {place}person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

prompt=template.invoke({'place':'place'})
print(prompt)
result=model.invoke(prompt)
final_result=parser.parse(result.content)

print(final_result)