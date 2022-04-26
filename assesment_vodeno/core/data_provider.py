import json
import logging
import requests

url = 'https://pokeapi.co/api/v2/pokemon?offset=100&limit=100'

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


def checkstatusok(response, param):
    status = response.status_code
    assert (status == 200), param
    pass


def get_pokemon(name=None):
    if name is None:
        logging.warning('Please deliver the pokemon name!!!')
        return
    response = requests.get(url)
    checkstatusok(response, 'Can NOT get response!')
    an_array = json.loads(response.text)['results']
    for ar in an_array:
        if ar.get('name') == name:
            logging.info(ar.get('name'))
            return ar
    logging.info('Can not find the pokemon with a given name!!!')
    return ''


def get_pokemon_details(pokemon=None):
    if pokemon is None:
        logging.warning('Did not received pokemon !!!')
        return
    pok = get_pokemon(pokemon)
    _url = pok.__getitem__('url')
    response = requests.get(_url)
    checkstatusok(response, 'Can NOT get response!')
    return json.loads(response.text)


if __name__ == '__main__':
    pokemon_details = get_pokemon_details("electrode")
    logging.info(pokemon_details['abilities'])
    logging.info(pokemon_details['height'])
    response = requests.get(url)
    an_array = json.loads(response.text)['results']

    for ar in an_array:
        logging.info(ar)
    # print(pokemon_details['haveAbilityImposter'])
