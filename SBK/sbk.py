from hugchat import hugchat
from hugchat.login import Login
from dotenv import dotenv_values

secrets = dotenv_values('./credentials.env')

hf_email = secrets['EMAIL']
hf_pass = secrets['PASS']

def generate_response(prompt_input, email, passwd):
    # Hugging Face Login
    sign = Login(email, passwd)
    cookies = sign.login()
    # Create ChatBot
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbot.chat(prompt_input)

prompt = "Hello There!"
response = generate_response(prompt, hf_email, hf_pass)

print(response)