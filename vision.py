from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st 
from PIL import Image
import google.generativeai as genai

os.getenv("GEMINI_API_KEY")
genai.configure(api_key = os.getenv("GEMINI_API_KEY"))

def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-1.5-flash')
    if input !="":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text 

st.set_page_config(page_title="Sky-Image-Bot")

st.header("Sky-ImageBot")
input = st.text_input("Input Prompt: ",key="input")

uploaded_file = st.file_uploader("Choose an image....",  type=["jpg","jpeg","png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image.", use_column_width=True)
    
submit = st.button("Submit")
if submit:
    response = get_gemini_response(input,image)
    st.subheader("Response from the Bot: ")
    st.write(response)
    

