import streamlit as st
import openai


st.title("Leed Certification Assistant")

# Set OpenAI API key from Streamlit secrets

openai.api_key = "sk-proj-dXDnQQVCMpJ8fzET9jtyT3BlbkFJHUQYdXE4cGDU6P2oer1s"

# Set a default model
models = ["gpt-3.5-turbo"]
default_model = "gpt-3.5-turbo"
model_choice = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.text_input("You", key="user_input"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response from OpenAI GPT
    response = openai.ChatCompletion.create(
        model=model_choice,
        messages=[
            {"role": "system", "content": "You are helping people get LEEd certified."},
            {"role": "user", "content": prompt}
        ]
    )

    # Add AI response to chat history
    ai_response = response.choices[0].message["content"]
    st.session_state.messages.append({"role": "AI", "content": ai_response})
    # Display AI response in chat message container
    with st.chat_message("AI"):
        st.markdown(ai_response)
