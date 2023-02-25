import pygame,sys
from pokedex_settings.database_pokemon import Data_pokemon
from pokedex_settings.pokemon_imagem import request_image

pygame.init()

#configurações iniciais
size =  width, height = 1040, 520
black = 0, 0, 0

screen = pygame.display.set_mode(size)

#carregando imagens
image = pygame.image.load(r'./pokedex.png')
pikachu =  pygame.image.load(r'./pikachu.png')

new_pokedex_size = (1040,520)
pokemon_size = (635, 423)

#chamando dataframe e modificando o tambem para inputs automaticos
# name = input()
# data = Data_pokemon.Possible_names()

# redimensiona a imagem
resized_image = pygame.transform.scale(image, new_pokedex_size)
resized_pikachu = pygame.transform.scale(pikachu, pokemon_size)

                             #y,x
screen.blit(resized_pikachu,(17,15))
screen.blit(resized_image, (0, 0))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        pygame.display.update()