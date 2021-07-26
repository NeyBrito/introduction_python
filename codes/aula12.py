# import requests
#
# def retorna_dados_cep(cep):
#     response = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))
#     print(response.status_code)
#     print(response.text)
#     # print(response.json())
#     dados_cep = response.json()
#     print(dados_cep['logradouro'])
#
# def retona_dados_pokemon(pokemon):
#     response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
#     dados_pokemon = response.json()
#     return dados_pokemon
#
# def retorna_response(url):
#     response = requests.get(url)
#     return response.text
#
# if __name__ == '__main__':
#     response = retorna_response('https://globallabs.academy/')
#     print(response)
#     # retorna_dados_cep('01001000')
#     # dados_pokemon = retona_dados_pokemon('pikachu')
#     # print(dados_pokemon['sprites']['front_shiny'])


# import requests
# busca = requests.get('https://viacep.com.br/ws/01001000/json/')
# status = busca.status_code
#
# def interpretarMensagem(mensagem):
#   print('{}'.format(mensagem))
#
# if status == 400:
#   print('Mensagem não chegou')
# elif status == 200:
#   mensagem = busca.json()
#   interpretarMensagem(mensagem)

import requests

response = requests.get('https://loja.com.br/frete/103229/json/')
dados = response.json()
print(
    'A entrega deve ser feita para {}, RG: {}, CPF: {}, nascido em {}, residente no CEP {}, na cidade de {}'.format())

