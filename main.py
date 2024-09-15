import os
import openai
import streamlit as st
from fastapi import Request
from langchain_core.output_parsers import StrOutputParser
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

open_ai_key = os.getenv("OPENAI")
os.environ["OPENAI_API_KEY"] = open_ai_key

app = FastAPI()


prompt_template = PromptTemplate(
    input_variables=["query"],
    template="Given the following question, provide a logical reasoning-based answer in points: {query}"
)

def generate_response(query,api_key,temperture):
    openai.api_key = api_key
    llm = ChatOpenAI(temperature = temperture)
    output_parser = StrOutputParser()
    chain = LLMChain(llm = llm,prompt= prompt_template,output_parser = output_parser)
    result = chain.invoke(query)
    return result

st.title("Enhanced chatbot for Logical & Reasoning")
st.sidebar.title("setting")
api_key = st.sidebar.text_input("Enter OpenAI key:",type = "password")

temperture = st.sidebar.slider("Temperture",min_value = 0.0,max_value = 2.0,value = 1.0)

st.write("Logical Question")
user_input = st.text_input("YOU :")

if user_input:
    response = generate_response(user_input,api_key,temperture)
    st.write(response['text'])
else:
    st.write("Pease provide the question")
