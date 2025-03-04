import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.Client()

msg = []

def generate_text(msg, model='gpt-3.5-turbo-0125', max_tokens=1000, temperature=0):
    resp = client.chat.completions.create(
        messages=msg,
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
        stream=True
    )
    print('Assistant: ', end='')
    full_resp = ''
    for stream_resp in resp:
        text = stream_resp.choices[0].delta.content
        if text:
            full_resp += text
            print(text, end='')
    print()    
    msg.append({'role': 'assistant', 'content': full_resp})
    return msg

def call_gpt():
    print('Welcome to the chatbot!')
    print('Enter "quit" to exit the chat.')
    print('='*50)
    while True:
        user_input = input('You: ')
        if user_input.lower() == 'quit':
            break
        msg.append({'role': 'user', 'content': user_input})
        generate_text(msg)
    print('Goodbye!')


