import streamlit as st
st.title("Some basic commands in streamlit" )
age=st.slider("enter your age",1,100)
city=st.selectbox("select your city",["delhi","mumbai","banglore","chennai"])

if st.button("show details"):
    st.write("your age is",age)
    st.write("your city is",city)