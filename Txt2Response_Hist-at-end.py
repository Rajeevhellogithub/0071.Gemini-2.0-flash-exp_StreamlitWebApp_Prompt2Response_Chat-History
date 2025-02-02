# .\tensorflowvenv\Scripts\activate
# cd PrakashSenapati\2024_12_23_Gemini_Projects
# streamlit run Chat_Self.py

# from dotenv import load_dotenv
# load_dotenv()

import streamlit as st
import os
import pathlib
import textwrap
from IPython.display import display
from IPython.display import Markdown
import google.generativeai as genai

os.environ['GEMINI_API_KEY'] = 'xxxxxx'
genai.configure(api_key=os.environ['GEMINI_API_KEY'])

model = genai.GenerativeModel('gemini-2.0-flash-exp')
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response =chat.send_message(question, stream=True)
    return response

st.set_page_config(page_title="Q&A Demo")
st.header("Gemini Application")
input = st.text_input("Input: ", key="input")
submit=st.button("Ask the question")

if submit:
    
    response=get_gemini_response(input)
    st.subheader("The Response is")
    for chunk in response:
        print(st.write(chunk.text))
        print("_"*80)
    
    st.write(chat.history)