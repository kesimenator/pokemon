import pytest

from core.data_provider import get_pokemon_details, check_pokemon_ability

testdata = [
    "electrode",
    "exeggcute",
    "marowak",
    "koffing",
]


@pytest.mark.functional
@pytest.mark.parametrize("pokemon_name", testdata)
def test_01_list_of_abilities(pokemon_name):
    _abilities = get_pokemon_details(pokemon_name)['abilities']
    print(_abilities)
    assert str(_abilities) != "", 'ability should exist'


@pytest.mark.functional
@pytest.mark.parametrize("pokemon_name", testdata)
def test_02_height(pokemon_name):
    _height = get_pokemon_details(pokemon_name)['height']
    print(_height)
    assert str(_height) != "", 'height should exist'


@pytest.mark.functional
@pytest.mark.parametrize("pokemon_name", testdata)
def test_03_check_ability_imposter_flag(pokemon_name):
    assert check_pokemon_ability(pokemon_name, "Imposter"), "Can't find flag Imposter"
