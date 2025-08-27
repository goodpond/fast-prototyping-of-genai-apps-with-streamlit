# import packages
from dotenv import load_dotenv
import openai
import streamlit as st


# load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = openai.OpenAI()

st.title("Hello, GenAI!")
st.write("This is your 2nd Streamlit app.")
user_prompt = st.text_input("Enter your prompt here:", "Explain generative AI in one sentence.")

## add a slider for temperature
temperature = st.slider(
    "Select temperature:", 
    min_value=0.0, 
    max_value=1.0, 
    value=0.7, 
    step=0.01, 
    help="Adjust the creativity of the response. Higher values make the output more creative and diverse."
    )

@st.cache_data
def get_response(user_prompt, temperature):
    response = client.responses.create(
        model="gpt-4o",
        input=[
            {"role": "user", "content": user_prompt}  # Prompt
        ],
        temperature=temperature,  # A bit of creativity
        max_output_tokens=100  # Limit response length
    )
    
    return response

with st.spinner("Generating response..."):
    response = get_response(user_prompt, temperature)

    # print the response from OpenAI
    st.write(response.output[0].content[0].text)