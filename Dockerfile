FROM python:3.12-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o requirements.txt para dentro do contêiner
COPY requirements.txt /app/

# Instalar dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Certifique-se de que o Streamlit está instalado
RUN pip install streamlit

# Copiar o código para o contêiner
COPY . /app/

# Definir o comando padrão para rodar o Streamlit
CMD ["streamlit", "run", "app.py"]  # Substitua 'app.py' pelo nome do seu script