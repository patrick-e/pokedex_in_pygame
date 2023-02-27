from src.resources.pokemon_service import Pokedex,PokemonDB

class RequestImage():
    def __init__(self,nome):
        '''
        pega nomes de pokemon e ira pesquisar no google a imagem
        '''
        self.nome = nome
        

    def image(self):
        ps = Pokedex()
        link = ps.get_image(self.nome)
        if link == '':
            ps = PokemonDB()
            link = ps.get_image(self.nome)
        return link