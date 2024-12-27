from os import system
import pygame 
system ("cls")
print()

pygame.init()
pygame.mixer.music.load("ex21.mp3")
pygame.mixer.music.play()
pygame.event.wait()