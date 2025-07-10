from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

#load openai api key from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

#Basic prompt template
prompt = PromptTemplate.from_template("what can you tell me about {topic}?")

#set up the LLM
llm = ChatOpenAI(temperature=0.7, model="gpt-4o-mini")

#combine the LLM with the prompt template to create a chain
#This chain will take a topic as input and return a response from the LLM
chain = prompt | llm

#Run the chain 
response = chain.invoke({"topic":"Artificial Intelligence"})

#Print the response
print("\nResponse from the LLM:\n", response.content)
