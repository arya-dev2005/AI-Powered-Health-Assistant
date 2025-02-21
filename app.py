import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Define the pipeline
chatbot = pipeline("text-generation", model="distilgpt2")

def healthcare_chatbot(user_input):
    try:
        if "symptoms" in user_input:
            return "Please consult a doctor for accurate advice."
        elif "appointment" in user_input:
            return "Please visit the website to book an appointment."
        elif "medication" in user_input:
            return "It's important to consult a doctor before taking any medication."
        elif "emergency" in user_input:
            return "Please call 911 for immediate assistance."
        elif "vaccine" in user_input:
            return "Please consult a doctor to get more information about the vaccine."
        elif "covid" in user_input:
            return "Please visit the CDC website for more information on COVID-19."
        else:
            response = chatbot(user_input, max_length=500, num_return_sequences=1, truncation=True)
            return response[0]['generated_text']
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    st.title("Healthcare Assistant Chatbot")
    user_input = st.text_input("How can I help you today?")
    if st.button("Submit"):
        if user_input:
            st.write("User: ", user_input)
            with st.spinner("Processing your query, please wait..."):
                try:
                    response = healthcare_chatbot(user_input)
                    st.write("Healthcare Assistant: ", response)
                    print(response)
                except Exception as e:
                    st.write(f"An error occurred while processing your request: {e}")
        else:
            st.write("Please enter a valid input to get a response.")

if __name__ == "__main__":
    main()