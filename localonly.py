import streamlit as st
import ollama
from langchain.llms import Ollama

st.title("Local Ollama Large Language Models with Streamlit")

models = ollama.list()
model_list = []

for model in models["models"]:
    model_list.append(model["name"])

selected_model = st.selectbox(
    "Select a model",
    model_list)

model = Ollama(model=selected_model)

prompt = st.text_input(label="Prompt:", value="", key="prompt")

response = model.predict(prompt)

st.write("Response:")
st.markdown(response)
