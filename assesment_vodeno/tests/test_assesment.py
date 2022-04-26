import unittest

import pytest


@pytest.mark.usefixtures("pokemon_check_fixt")
class Assessment(unittest.TestCase):

    @pytest.mark.functional
    def test_01_list_of_abilities(self):
        _abilities = self.pokemon_details['abilities']
        print(_abilities)


    @pytest.mark.functional
    def test_02_height(self):
        _height = self.pokemon_details['height']
        print(_height)


    @pytest.mark.functional
    def test_03_ability_imposter(self):
        pass


