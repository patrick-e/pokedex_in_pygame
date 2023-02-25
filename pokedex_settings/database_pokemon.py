import pandas as pd

class Data_pokemon:

    def All_name_req(csv:str):
        '''
        faz a requisição completa de lista de nomes
        '''
        a = pd.read_csv(csv)['name']
        return a

    def Possible_names(csv:str,name:str):
        '''
        faz a requisição de uma serie de possiveis nomes 
        
        '''
        possible = []
        df = pd.read_csv(csv)
        
        for nm in df['name']:
            if nm.lower().startswith(name.lower()):
                possible.append(nm)
        
        return possible


a = Data_pokemon.Possible_names("../data/poke.csv",'cha')
print(a)
