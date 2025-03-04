import openai
from dotenv import load_dotenv, find_dotenv

from assistent.chat import call_gpt


_ = load_dotenv(find_dotenv())

client = openai.Client()


if __name__ == '__main__':
    print('Bem vindo ao assistente virtal')
    print('escolha um assistente')
    print('1 - ChatGPT')
    print('2 - DALL-E')
    print('3 - Audio to Text')
    print('4 - Text to Audio')
    print('5 - Vision')
    print()
    try:
        opcao = input('Digite a opcao desejada: ')
        if opcao == '1':
            print('ChatGPT')
            call_gpt() 
        elif opcao == '2':
            print('DALL-E')
        elif opcao == '3':
            print('Audio to Text')
        elif opcao == '4':
            print('Text to Audio')
        elif opcao == '5':
            print('Vision')
        else:
            print('Opcao invalida')
    except EOFError:
        print('Opcao invalida')

