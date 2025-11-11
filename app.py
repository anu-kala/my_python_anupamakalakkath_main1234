import streamlit as st
import pandas as pd
st.title("Hello from Notepad!")
st.write("This Streamlit app")
st.title("Python")
st.header("Do you know me")
st.subheader("Can you guess")
st.text("I am very powerful")
st.write("I am very Simple")
st.markdown("Hai I am Python")
st.code("""print("Welcome to data class")""")
st.code("""for i in range(1,5):
print(i)""")
dataset=pd.read_csv("titanic.csv")
st.dataframe(dataset)
name=st.text_input("Enter your name:")
fname=st.text_input("Enter your father's name")
adr=st.text_input("enter your address:")
classdata=st.selectbox("Enter your class:",(1,2,3,4,5,6))

button=st.button("Done")
if button:
   st.markdown(f"""
Name:{name}
Father Name:{fname}
address:{adr}
class:{classdata}""")

number=st.slider("pick a number",0,100)

