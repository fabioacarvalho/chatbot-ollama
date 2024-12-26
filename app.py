import streamlit as st
import requests
import json
from dotenv import load_dotenv
import os


load_dotenv()


def generate_response(message):
    # url = "http://localhost:11434/api/generate"  # Localhost
    url = os.getenv("URL")  # Docker
    headers = {"Content-Type": "application/json"}

    prompt = {
        "model": os.getenv("MODEL"),
        "prompt": f"{message}",
        "options": {
            "temperature": float(os.getenv("TEMPERATURE", 0))
        },
    }

    response = requests.post(url, json=prompt, headers=headers)
    responses = []

    try:
        # Divida a resposta bruta em partes JSON individuais
        raw_responses = response.text.strip().split("\n")
        for raw in raw_responses:
            try:
                parsed = json.loads(raw)
                if "response" in parsed:
                    responses.append(parsed["response"])
            except json.JSONDecodeError:
                continue  # Ignora partes inválidas

        # Combine todas as respostas em uma única string
        return " ".join(responses)

    except Exception as e:
        return f"Error processing response: {e}"


def handle_message(message):
    response = "Sorry, I had a problem with the server. Please try again later."

    if message:
        st.write("Generating your answer based on knowledge...")
        st.info(body="Generating your answer based on knowledge...", icon=":material/smart_toy:")

        try:
            response = generate_response(message)
        except Exception as e:
            response = f"An error occurred: {e}"
            st.error(f"An error occurred: {e}")

        with st.chat_message("user"):
            st.write(message)

    with st.chat_message("ai"):
        st.write(response)


def main():
    st.set_page_config(
        page_title="Ollama Chatbot", page_icon=":bird")
    st.header("Ollama Chatbot")
    # with st.container():
    #     prompt = st.chat_input(placeholder="Say something", key="message")
    #     handle_message(prompt)
    message = st.text_area("Write here your question...")
    st.button(label="", icon=":material/send:", key="send", on_click=handle_message, args=(message,))

    # if message:
    #     st.write("Generating your answer based on knowledge...")
    #     result = "Nothing"  # generate_response(message)
    #     st.info(result)


if __name__ == "__main__":
    main()
