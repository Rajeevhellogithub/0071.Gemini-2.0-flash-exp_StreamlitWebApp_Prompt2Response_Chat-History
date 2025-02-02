# .\tensorflowvenv\Scripts\activate
# cd PrakashSenapati\2024_12_23_Gemini_Projects
# streamlit run Vision_Self.py

# from dotenv import load_dotenv
# load_dotenv()

# os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image
import google.generativeai as genai

os.environ['GEMINI_API_KEY'] = 'xxxxxxxxxxxxxx'
genai.configure(api_key=os.environ['GEMINI_API_KEY'])

def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    
    if input != "":
       response = model.generate_content([input, image])
    else:
       response = model.generate_content(image)
    return response.text

st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Q&A from Image")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_container_width=True)
    
input = st.text_input("Q&A from Image Prompt: ", key="input")
submit=st.button("Ask Info related to the image")

if submit:
    
    response = get_gemini_response(input, image)
    st.subheader("The Response is:-")
    st.write(response)