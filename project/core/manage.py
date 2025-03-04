import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.Client()

def create_assistant(name, instructions, tools, model='gpt-3.5-turbo-0125'):
    """func to create new assistant
    name="Tutor de Matemática da Asimov",
    instructions='Você é um tutor pessoal de matemática da empresa Asimov. \
            Escreva e execute códigos para responder as perguntas de matemática que lhe forem passadas.',
    tools=[{'type': 'code_interpreter'}],
    tool_resources={'code_interpreter': {'file_ids': [file.id]}},
    model='gpt-3.5-turbo-0125'

    Args:
        name (str): reference name
        instructions (str): _description_
        tool (list): list with name of tools
        tool_resources (list): a list resources for used by tools
        model (str): chatgpt model
    """
    list_tools = [{'type': tool} for tool in tools]

    assitant = client.beta.assistants.create(
        name=name,
        instructions=instructions,
        tools=[{'type': list_tools}],
        model=model
    )
    return assitant