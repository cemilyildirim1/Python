import pygame
from pygame.locals import*
from OpenGL.GL import *
from OpenGL.GLU import*

def nokta():
    glPointSize(20)
    glBegin(GL_LINES)
    glVertex2d(0.005,0.005)
    glColor3f(255,255,255)
    glVertex2d(0.5,0.5)
    glColor3f(0,0,254)
    glEnd()
def nokta2():
    glLineWidth(20)
    glBegin(GL_LINES)
    glVertex2d(0.005,0.005)
    glColor3f(255,255,255)
    glVertex2d(0.5,0.5)
    glColor3f(0,0,254)
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display,DOUBLEBUF|OPENGL)
    color = (255,50,40)
    while True:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                quit()



        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        nokta()
        pygame.display.flip()
        pygame.time.wait(10)
def main2():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display,DOUBLEBUF|OPENGL)
    color = (255,50,40)
    while True:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                quit()



        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        nokta2()
        pygame.display.flip()
        pygame.time.wait(10)

main2()