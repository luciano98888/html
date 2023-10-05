import random
import pygame

BLANCO=(255,255,255)
NEGRO=(0,0,0)


def tecla(presionada, protagonista):
    if presionada[pygame.K_a]:
        protagonista.rect.x-=1
    if presionada[pygame.K_d]:
        protagonista.rect.x+=1

class Personaje(pygame.sprite.Sprite):
    
    def __init__(self, color, largo, alto):
        
        super().__init__()
        
        self.image = pygame.image.load("pixil-frame-0.png")
        self.image = pygame.transform.scale(self.image,(80,80))
        self.rect = self.image.get_rect()
    
class Enemigo(pygame.sprite.Sprite):
    
    def __init__(self, color, largo, alto):
        
        super().__init__()
        
        self.image = pygame.image.load("enemigo.png")
        self.image = pygame.transform.scale(self.image,(80,80))
        self.rect = self.image.get_rect()
        
    def actualizacion(self):
        self.rect.y += 3

pygame.init()

pantalla_largo =800
pantalla_alto = 600
pantalla =pygame.display.set_mode([800, 600])

enemigo_lista = pygame.sprite.Group()

listade_todoslos_sprites = pygame.sprite.Group()

#Cantidad de enemigos
c=random.randint(1,100)

for i in range(c):
    enemigo = Enemigo(NEGRO, 10, 10)
    
    enemigo.rect.x = random.randrange(pantalla_largo)
    enemigo.rect.y = random.randrange(10)
    
    
    enemigo_lista.add(enemigo)
    listade_todoslos_sprites.add(enemigo)
    

protagonista = Personaje(BLANCO, 10, 10)

listade_todoslos_sprites.add(protagonista)

hecho = False 
reloj = pygame.time.Clock()
marcador=0

while not hecho:
    for evento in pygame.event.get():
        if evento.type ==   pygame.QUIT:
            hecho = True
            
    pantalla.fill(BLANCO)
    
    tecla(pygame.key.get_pressed(), protagonista)
    
    listade_todoslos_sprites.draw(pantalla)
    reloj.tick(60)


    pygame.display.flip()

pygame.quit()




















