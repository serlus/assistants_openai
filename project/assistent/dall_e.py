import requests
from PIL import Image


import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.Client()



def generate_img(name, model='dall-e-3', prompt, size, quality, style):
    """ func to generate image
    name = 'bosque'
    modelo = 'dall-e-3'
    prompt = 'Crie uma imagem de um campo de flores, \
        amplo com uma leve elevação ao fundo.'
    qualidade = 'hd' or standart
    style = 'natural'

    Args:
        model (_type_): _description_
        prompt (_type_): _description_
        size (_type_): _description_
        quality (_type_): _description_
        style (_type_): _description_
    """    
    resp = client.images.generate(
        model=model,
        prompt=prompt,
        size='1024x1024',
        quality=quality,
        style=style,
        n=1
    )
    name_file = f'arquivos/imagens/{name}_{model}_{quality}_{style}.jpg'

    image_url = resp.data[0].url
    img_data = requests.get(image_url).content
    with open(name_file, 'wb') as f:
        f.write(img_data)
    return resp.data[0].revised_prompt

