import json

import requests

url = 'https://pokeapi.co/api/v2/pokemon?offset=100&limit=100'


def checkstatusok(response, param):
    status = response.status_code
    assert (status == 200), param
    pass


def get_pokemon(name=None):
    if name is None:
        print('Please deliver the pokemon name!!!')
        return
    response = requests.get(url)
    checkstatusok(response, 'Can NOT get response!')
    an_array = json.loads(response.text)['results']
    for ar in an_array:
        if ar.get('name') == name:
            print(ar.get('name'))
            return ar
    print('Can not find the pokemon with a given name!!!')
    return ''


def get_pokemon_details(pokemon=None):
    if pokemon is None:
        print('Did not received pokemon !!!')
        return

    pok = get_pokemon(pokemon)
    _url = pok.__getitem__('url')
    response = requests.get(_url)
    checkstatusok(response, 'Can NOT get response!')
    return json.loads(response.text)


if __name__ == '__main__':
    pokemon_details = get_pokemon_details("electrode")
    print(pokemon_details['abilities'])
    print(pokemon_details['height'])
    response = requests.get(url)
    an_array = json.loads(response.text)['results']

    for ar in an_array:
        print(ar)
    # print(pokemon_details['haveAbilityImposter'])
