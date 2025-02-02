# .\tensorflowvenv\Scripts\activate
# cd PrakashSenapati\2024_12_23_Gemini_Projects
# streamlit run Qachat_Self.py

# from dotenv import load_dotenv
# load_dotenv()
# os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

import os
import streamlit as st
import google.generativeai as genai

# Configure API key for Gemini
os.environ['GEMINI_API_KEY'] = 'xxxxxxxxx'
genai.configure(api_key=os.environ['GEMINI_API_KEY'])

# Initialize the Generative Model
model = genai.GenerativeModel('gemini-2.0-flash-exp')
chat = model.start_chat(history=[])

# Function to get the response from Gemini
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Streamlit app setup
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Input and submit button
user_input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit and user_input:
    response = get_gemini_response(user_input)
    st.session_state['chat_history'].append(("You", user_input))

    # Display subheader only once
    st.subheader("The Response is:-")
    
    # Aggregate the response chunks into a single text
    full_response = ""
    for chunk in response:
        full_response += chunk.text  # Collect the full response text
    st.write(full_response)  # Display the full response once
    st.session_state['chat_history'].append(("Bot", full_response))

# Display chat history
st.subheader("The Chat History is:-")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
