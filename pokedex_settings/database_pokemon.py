import pandas as pd

def name_req(csv:str):
    a = pd.read_csv(csv)['name']
    return a
    

name_req("../data/poke.csv")
