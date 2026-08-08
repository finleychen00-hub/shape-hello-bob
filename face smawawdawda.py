import pgzrun
import pygame

WIDTH=(750)
HEIGHT=(750)
TITLE=("FACE")




def draw():
    screen.draw.circle((WIDTH/2,HEIGHT/2),(125),color="green",10)
    screen.draw.line((325,350),(325,300),("green"))
    screen.draw.line((425,350),(425,300),("green"))
    pygame.draw.arc(screen.surface,("green"),(400,290,50,25),0,3.14)
    pygame.draw.arc(screen.surface,("green"),(300,290,50,25),0,3.14)
    pygame.draw.arc(screen.surface,("green"),(325,400,100,75),3.14,6.28)
    screen.draw.circle((WIDTH/2,HEIGHT/2),(12.5),("green"))


pgzrun.go()
