# Chatbot Ollama

This is your personal chatbot with Ollama.

![Chatbod](https://github.com/fabioacarvalho/chatbot-ollama/blob/ui-api/.github/img/chatbot.png?raw=true)

## TO-DO

[ ] - Setup ollama into docker-composer; <br>
    [ ] - Change the url into app.py; <br>
[ ] - Generate a desktop app with electron; <br>
[ ] - Create a function to getting the context chat; <br>
[ ] - Create a model to fining tuning the model with your own data and resources; <br>
[ ] - Setup `async` at `function generate_response`;  <br>

## How use this Project

To use this project you need had installed in your environment the Docker and Ollama. So after that you can run the follow command: <br>

Runnig Ollama: <br>
```bash
ollama serve
```

 <br>

 > This command will setup a new server ollama for you where you can doing request from `http://localhost:11434/api/generate` and use this json to send your prompt:

 <br>
 
 ```json
 
 {
  "model": "llama3:latest",
  "prompt": "hello world",
  "options": {
    "temperature": 0
  }
}
 
 ```
 
 <br>

After that you can run the follow command:

> Remember: if you change or download a diferent model by `llama3:latest` you'll need change into the .env at MODEL_OLLAMA.

```bash
docker compose up --build
```

 <br>

