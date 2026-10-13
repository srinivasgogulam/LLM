import streamlit as st
from openapi import ask_gpt

st.set_page_config(
    page_title="My AI Assistant",
    page_icon="🤖"
)

st.title("🤖 My AI Assistant")

# Select GPT Model
model = st.selectbox(
    "Select GPT Model",
    ["gpt-5.5", "gpt-5-mini"]
)

# Enter User Question
user_input = st.text_area(
    "Enter your question",
    placeholder="Ask me anything..."
)

# Submit Button
if st.button("Submit"):

    if not user_input.strip():
        st.warning("Please enter your question")

    else:
        try:
            with st.spinner("Generating response..."):
                response = ask_gpt(model, user_input)

            st.subheader("AI Response")
            st.write(response)

        except Exception:
            st.error("Unable to generate a response. Please check your API configuration.")