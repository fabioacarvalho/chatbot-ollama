FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# RUN curl -fsSL https://ollama.com/install.sh | sh
# RUN ollama

EXPOSE 8000

CMD ["python", "main.py"]