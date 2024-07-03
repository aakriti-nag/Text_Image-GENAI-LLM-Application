from dotenv import load_dotenv
load_dotenv()  # to load all environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Configure the generative AI model
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Load Gemini Pro model
model = genai.GenerativeModel('gemini-pro-vision')

def get_response(input, image):
    if input!=' ':
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

# Initialize Streamlit app
st.set_page_config(page_title='Gemini Image App', layout='wide')
st.title('Gemini Image Application')

# Input section
input = st.text_input('Input Prompt:', key='input')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button('Submit')

if submit:
    if input:
        with st.spinner('Generating responses...'):
            response = get_response(input, image)
            st.subheader("The response is:")
            st.write(response)
    else:
        st.error('Please enter a question.')

# Sidebar
st.sidebar.header("About")
st.sidebar.info("This application uses Generative AI to answer questions. Enter your question in the input box and click 'Submit' to get a response.")
    