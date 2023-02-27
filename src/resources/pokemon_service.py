import requests
from lxml import etree

from bs4 import BeautifulSoup
from abc import ABC, abstractmethod

class Pokemon(ABC):
    '''
    classe abstrata de pokemon
    '''
    def __init__(self) -> None:
        super().__init__()
        
    @abstractmethod
    def get_image() -> str:
        pass


class Pokedex(Pokemon):
    '''Return a url for a pokemon name'''
    def __init__(self) -> None:
        self.headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
        self.image_base = "https://www.pokemon.com/br/pokedex/"

    def get_image(self, name: str) -> str:
        pokedex = requests.get(f"{self.image_base}{name.strip().lower()}",
                                headers=self.headers)
        if pokedex.status_code != 200:
            return
        soup = BeautifulSoup(pokedex.text, "html.parser")
        pokedex_model = etree.HTML(str(soup))
        return pokedex_model.xpath("/html/body/div[4]/section[3]/div[1]/div[1]/div/img/@src")[0]

class PokemonDB(Pokemon):
    def __init__(self) -> None:
        self.image_base = "https://pokemondb.net/pokedex/"
        self.headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
    
    def get_image(self, name: str) -> str:
        pokedex = requests.get(f"{self.image_base}{name.strip().lower()}",
                                headers=self.headers)
        if pokedex.status_code != 200:
            return
        soup = BeautifulSoup(pokedex.text, "html.parser")
        pokedex_model = etree.HTML(str(soup))
        return pokedex_model.xpath("//*[@id=\"tab-basic-50\"]/div[1]/div[1]/p[1]/a/picture/img/@src")[0]
