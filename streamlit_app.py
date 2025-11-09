import streamlit as st
from openai import OpenAI, OpenAIError

# Page Configuration
st.set_page_config(
    page_title="Agentic AI Demo",
    page_icon="🤖" ,
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Page Title
st.title("Agentic AI Demo")

# Page Sidebar Configuration
st.sidebar.header("Configuration")

# OpenAI API Key Input
api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")

if not api_key:
    st.warning("Please enter your OpenAI API Key in the sidebar to proceed.")
    st.stop()

# Initialize OpenAI Client
client = OpenAI(api_key=api_key)

# User Input
user_input = st.chat_input("Ask me to do something!")

if user_input:
    try:
        response = client.responses.create(
            model="gpt-5",
            input=user_input
        )
        st.write(response.output_text)
    except OpenAIError as e:
        st.error(f"OpenAI API error: {e}")
