import pygame,sys
import io 
import requests
from src.pokemon_imagem import RequestImage

# from scr.database_pokemon import Data_pokemon


pygame.init()

#configurações iniciais
size =  width, height = 1040, 520

screen = pygame.display.set_mode(size)

image_load = False
#carregando imagens
def bg(url):
    bg_url = url
    bg_stf = requests.get(bg_url)
    bg_file = io.BytesIO(bg_stf.content)
    bg = pygame.image.load(bg_file).convert_alpha()
    bg.fill((255,255,255,128),special_flags=pygame.BLEND_RGBA_MULT)
    resized_bg =pygame.transform.scale(bg, (bg.get_rect().width*1.5,bg.get_rect().height*1.5))
    screen.blit(resized_bg,(0,0))

def pikamon(nome):
    global image_load
    image_url = RequestImage(nome).image()
    image_stf = requests.get(image_url)
    image_file = io.BytesIO(image_stf.content)
    pikachu =  pygame.image.load(image_file).convert_alpha()
    resized_pikachu = pygame.transform.scale(pikachu, pokemon_size)
    pokeball = pygame.image.load('pokeballsprite.png')
   

    return screen.blit(resized_pikachu,(17,15))


image = pygame.image.load(r'./pokedex.png')

new_pokedex_size = (1040,520)
pokemon_size = (635, 423)

#chamando dataframe e modificando o tambem para inputs automaticos
# name = input()
# data = Data_pokemon.Possible_names()

# redimensiona a imagem
resized_image = pygame.transform.scale(image, new_pokedex_size)

screen.fill([255,255,255])
bg('https://thumbs.dreamstime.com/b/pokemon-silhouette-background-vector-cartoon-symbol-art-icon-play-go-sign-concept-ball-pokeball-shape-pokemon-silhouette-142907703.jpg')
                             #y,x
pikamon('pikachu')
screen.blit(resized_image, (0, 0))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        pygame.display.update()
