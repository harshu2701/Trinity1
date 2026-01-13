import streamlit as st
import google.generativeai as genai

st.title("welcome to my streamlit app")

user_input=st.text_input("ASK ME ANYTHING")

genai.configure(api_key="AIzaSyAdDFTc4d_Qs2FDzfHKjHXjMbttmT5TtQs")

model = genai.GenerativeModel("models/gemini-2.5-flash")

if user_input:
    response = model.generate_content(user_input)
    st.write("Response:", response.text)



