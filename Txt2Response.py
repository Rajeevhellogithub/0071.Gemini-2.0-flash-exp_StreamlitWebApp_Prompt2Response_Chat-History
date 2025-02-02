# .\tensorflowvenv\Scripts\activate
# cd PrakashSenapati\2024_12_23_Gemini_Projects
# streamlit run App_Self.py

# from dotenv import load_dotenv
# load_dotenv()

# os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

import streamlit as st
import os
import pathlib
import textwrap
from IPython.display import display
from IPython.display import Markdown
import google.generativeai as genai

os.environ['GEMINI_API_KEY'] = 'xxxxxxxxxx'
genai.configure(api_key=os.environ['GEMINI_API_KEY'])

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title="Gemini LLM App")
st.header("Gemini AI Bot Application")
input=st.text_input("Input: ",key="input")
submit=st.button("Click me to generate response")

if submit:
    
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)