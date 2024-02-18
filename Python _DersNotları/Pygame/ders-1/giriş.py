import pygame
import pgzrun

WIDTH = 600
HEIGHT = 300

TITLE = "Yeni bir oyun"
FPS = 30

uzayli = Actor("uzayli",(50,200),WIDTH=10)
uzayli.angle = 0
arkaplan = Actor("arkaplan")

def draw():
    arkaplan.draw()
    uzayli.draw()
    
def update(dt):
    uzayli.x = uzayli.x + 5
    uzayli.y = uzayli.y - 2
    



pgzrun.go()