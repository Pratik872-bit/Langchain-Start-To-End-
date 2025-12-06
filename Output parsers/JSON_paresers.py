from html import parser
from itertools import chain
from pydoc_data import topics
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()


model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

parser=JsonOutputParser()
template=PromptTemplate(
    template='give me the name,age,and cit of a fictional person\n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

prompt=template.format()

result=model.invoke(prompt)
parsed_output=parser.parse(result.content)
print(parsed_output)


