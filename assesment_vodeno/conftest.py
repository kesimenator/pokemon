import pytest

from core.data_provider import get_pokemon, get_pokemon_details


@pytest.fixture
def pokemon_check_fixt(request):
    _pokemon_details = get_pokemon_details("electrode")
    # print(_pokemon_details)
    # pokemon_request.cls.pokemon_check = pokemon_details
    request.cls.pokemon_details = _pokemon_details
