import pygame,sys
import io 
import requests
from src.pokemon_imagem import RequestImage

# from scr.database_pokemon import Data_pokemon


pygame.init()

#configurações iniciais
size =  width, height = 1040, 520

screen = pygame.display.set_mode(size)

#carregando imagens
image_url = RequestImage('diglett').image()

image_stf = requests.get(image_url)
image_file = io.BytesIO(image_stf.content)

bg_url = 'https://thumbs.dreamstime.com/b/pokemon-silhouette-background-vector-cartoon-symbol-art-icon-play-go-sign-concept-ball-pokeball-shape-pokemon-silhouette-142907703.jpg'
bg_stf = requests.get(bg_url)
bg_file = io.BytesIO(bg_stf.content)

image = pygame.image.load(r'./pokedex.png')
pikachu =  pygame.image.load(image_file).convert_alpha()
bg = pygame.image.load(bg_file).convert_alpha()
bg.fill((255,255,255,128),special_flags=pygame.BLEND_RGBA_MULT)

new_pokedex_size = (1040,520)
pokemon_size = (635, 423)

#chamando dataframe e modificando o tambem para inputs automaticos
# name = input()
# data = Data_pokemon.Possible_names()

# redimensiona a imagem
resized_image = pygame.transform.scale(image, new_pokedex_size)
resized_pikachu = pygame.transform.scale(pikachu, pokemon_size)
resized_bg =pygame.transform.scale(bg, (bg.get_rect().width*1.5,bg.get_rect().height*1.5))

screen.fill([255,255,255])
screen.blit(resized_bg,(0,0))
                             #y,x
screen.blit(resized_pikachu,(17,15))
screen.blit(resized_image, (0, 0))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        pygame.display.update()
