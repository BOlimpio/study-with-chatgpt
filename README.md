# Study with ChatGPT :fist_right: :fist_left:

# Chatbot using OpenAI API
This code is a simple chatbot that I created to help to study and use the OpenAI API to generate text based on user prompts. The chatbot prompts the user for input, sends the input to the OpenAI API, and displays the generated text. The user can then choose whether or not to save the generated text to a file.

Two models available:
+ text-davinci-003 (`ask-chatgpt-gpt-3.py`)
+ gpt-3.5-turbo (`ask-chatgpt-davinci-003.py`)

## Prerequisites
To run this code, you'll need to have Python 3 installed on your system, along with the requests library. You'll also need an API key from OpenAI. You can obtain an API key by signing up for OpenAI [here](https://beta.openai.com/signup/).

## Usage
To use the chatbot, run the script with the name of the file you want to save the generated text to as a command-line argument. For example:

```
python ask-chatgpt-gpt-3.py file_name
```

This will prompt the user for input and generate text based on that input. The generated text will be displayed on the screen, and the user will be prompted to save the text to the specified file.

To exit the chatbot, type "done" when prompted for input.

## Limitations
This chatbot uses the OpenAI GPT-3.5-turbo and text-davinci-003 model, which has a maximum context length of 4096 tokens including the message you typed. If you enter a prompt that exceeds this length, the chatbot will return an error.

## Contributing
If you have any suggestions for improving this chatbot, feel free to open a pull request, send me a message on [Linkedin](https://www.linkedin.com/in/bruno-olimpio/) or issue on GitHub.
