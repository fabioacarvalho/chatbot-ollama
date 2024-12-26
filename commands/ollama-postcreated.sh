#!/bin/bash

# Check if llama3 is already installed
if ollama list | grep -q llama3; then
    echo "llama3 is already installed."
else
    # Run the ollama llama3 command
    ollama run llama3

    # Wait for llama3 to be installed
    until ollama list | grep -q llama3; do
        echo "Waiting for llama3 to be installed..."
        sleep 5
    done
fi

# Serve the application
ollama serve
