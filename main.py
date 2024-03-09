# main.py

import pygame
from menu import Menu

pygame.init()
display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake Game')

def main():
    menu = Menu(display)
    menu.show_menu()

if __name__ == "__main__":
    main()
