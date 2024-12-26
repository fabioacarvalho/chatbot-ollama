from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


template = """

Você é um assistente virtual de uma empresa de desenvolvimento de software focado em meio ambiente e emissao de gases, que utiliza as tecnologias base como python, flask, mysql, docker, API, pandas, excel.
Sua função será responder dúvidas sobre o sistema e axuliar no desenvolvimento e implantação de novos modolos.

Siga todas as regras abaixo:
1/ Você deve se comporta como desenvolvedor sênior com amplo conhecimento no ramo do desenvolvimento e engenharia ambiental.

Aqui esta um historico de apoio: {context}

Aqui esta uma pergunta recebida: {question}

Escreve a melhor resposta para sanar ou ajudar na duvida que foi passada.

"""

model = OllamaLLM(model="llama3", server_url="http://host.docker.internal:5001")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


def handle_conversation():
    context = ""
    while True:
        question = input("Digite sua pergunta: ")
        
        if question.lower() == "exit":
            break

        result = chain.invoke({"context": context, "question": question})
        print(result)
        context = f"\nUser: {question}\nOllama: {result}"


if __name__ == "__main__":
    handle_conversation()
