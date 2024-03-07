import streamlit as st
#from langchain.llms import OpenAI
from langchain_community.llms import OpenAI

st.title(' Stylus Test App')
openai_api_key = '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'


def generate_response(input_text):
    lim = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(lim(input_text))

with st.form('my_form'):
    text = st.text_area('Enter text: ', 'Give me use case and ask for test cases')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sm-'):
        st.warning('Please enter your OpenAI Api key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)
