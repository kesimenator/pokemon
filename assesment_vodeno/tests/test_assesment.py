import pytest

from core.data_provider import get_pokemon_details

testdata = [
    "electrode",
    "exeggcute",
]


@pytest.mark.functional
@pytest.mark.parametrize("pokemon_name", testdata)
def test_01_list_of_abilities(pokemon_name):
    _abilities = get_pokemon_details(pokemon_name)['abilities']
    print(_abilities)


@pytest.mark.functional
@pytest.mark.parametrize("pokemon_name", testdata)
def test_02_height(pokemon_name):
    _height = get_pokemon_details(pokemon_name)['height']
    print(_height)


@pytest.mark.functional
@pytest.mark.parametrize("pokemon_name", testdata)
def test_03_ability_imposter(pokemon_name):
    pass


