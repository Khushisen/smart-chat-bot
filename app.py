#chatbot using streamlit and google generative-ai
from dotenv import load_dotenv
import streamlit as st
import pandas as pd
import os
import textwrap
import google.generativeai as genai
from IPython.display import display, Markdown


#load env variables from .env file
load_dotenv()

genai_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=genai_api_key)

#function to interact with the gemini generative ai model and get a response

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text 

#initialize the streamlit app with custom page title
st.set_page_config(page_title="SKY-BOT")
st.header("Hello There!, Welcome To Sky-Bot.")

input = st.text_input("Input: ",key="input")
submit=st.button("ASK")
if submit:
    response = get_gemini_response(input)
    st.subheader("Response From Bot: ")
    st.write(response)
    
    
