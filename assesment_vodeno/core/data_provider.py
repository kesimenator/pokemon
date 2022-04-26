import json

import requests


def checkstatusok(response, param):
    status = response.status_code
    assert (status == 200), param
    pass  #  todo?


def get_pokemon(name=None):
    if name is None:
        print('Please deliver the pokemon name!!!')
        return
    url = 'https://pokeapi.co/api/v2/pokemon?offset=100&limit=100'
    response = requests.get(url)
    checkstatusok(response, 'Can NOT get response!')
    an_array = json.loads(response.text)['results']
    for ar in an_array:
        if ar.get('name') == name:
            return ar
        else:
            print('Can not find the pokemon with a given name!!!')
            return ''


def get_pokemon_details(pokemon=None):
    if pokemon is None:
        print('Did not received pokemon !!!')
        return

    pok = get_pokemon(pokemon)

    name = pok['name']
    print(f'pokemon name {name}')
    url = pok['url']
    response = requests.get(url)
    checkstatusok(response, 'Can NOT get response!')
    return json.loads(response.text)




# class DataProvider:
#     def __init__(self):
#         self.aaa = 1
#         print("aaa")


if __name__ == '__main__':
    # pokemon = get_pokemon("electrode")
    # print(pokemon)
    pokemon_details = get_pokemon_details("electrode")
    print(pokemon_details['abilities'])
    print(pokemon_details['height'])
    # print(pokemon_details['haveAbilityImposter'])
