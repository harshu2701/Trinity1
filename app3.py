import streamlit as st
st.title("make a simplelm calculator app")
num1=st.number_input("enter first number")
num2=st.number_input("enter second number")

operation= st.selectbox("choose operation",["addition","subtraction","multiplication","division"] )

if st.button("calculate"):
    if operation=="addition":
        result=num1+num2
        st.write("the result is",result)
    elif operation=="subtraction":
        result=num1 - num2
        st.write("the result is",result)
    elif operation=="multiplication":
        result=num1 * num2
        st.write("the result is",result)
    elif operation=="division":
        if num2 != 0:
            result=num1 / num2
            st.write("the result is",result)
        else:
            st.write("Error: Division by zero is not allowed.")