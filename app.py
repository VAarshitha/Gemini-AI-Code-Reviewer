# -*- coding: utf-8 -*-
import streamlit as st
import google.generativeai as genai  # Replacing OpenAI with Gemini
import os

# Load Gemini API key securely from the 'keys' file
def load_api_key():
    """Load API key from the 'keys' file."""
    try:
        with open("keys", "r") as key_file:
            return key_file.read().strip()
    except FileNotFoundError:
        st.error("API key file 'keys' not found. Please create the file and add your Gemini API key.")
        return None

def review_code(code_snippet):
    """Function to review Python code using Gemini AI API."""
    api_key = load_api_key()
    if not api_key:
        return "Error: Gemini API key is missing."

    genai.configure(api_key=api_key)  # Set Gemini API key

    prompt = f"""
    You are an AI code reviewer. Analyze the following Python code for errors, best practices, and improvements.
    Provide a list of issues and an improved version of the code.

    Code:
    {code_snippet}
    """

    try:
        model = genai.GenerativeModel("gemini-pro")  # Use Gemini AI model
        response = model.generate_content(prompt)  # Generate response
        return response.text  # Return AI feedback
    except Exception as e:
        return f"Error occurred while processing: {str(e)}"

def main():
    """Streamlit UI for AI Code Reviewer."""
    st.title("Gemini AI Code Reviewer")  
    st.write("Submit your Python code and get AI-powered feedback!")

    code = st.text_area("Enter your Python code here:", height=200)
    if st.button("Review Code"):
        if code.strip():
            review_result = review_code(code)
            st.subheader("Code Review Feedback")
            st.text_area("AI Suggestions:", review_result, height=300)
        else:
            st.error("Please enter some Python code before submitting.")

if __name__ == "__main__":
    main()
