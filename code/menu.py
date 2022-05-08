import pygame, sys
from button import Button
from pygame import mixer 

import Jogo

pygame.init()

mixer.init() 
keys = pygame.key.get_pressed()
mixer.music.load('../sounds/song.mp3') 
mixer.music.play() 
mixer.music.set_volume(0.1) 

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Brick Breaker")


BG_image = pygame.image.load("../assets/space.png")
BG = pygame.transform.scale(BG_image, (1280,720))

def get_font(size): 
    return pygame.font.Font("../assets/font.ttf", size)

def credits():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(20).render("Wood & Wever agredecem vocês por jogarem nosso jogo.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    width = 1280
    i = 0
    while True:
        SCREEN.fill("Black")
        SCREEN.blit(BG, (i, 0))
        SCREEN.blit(BG, (width+i, 0))

        if i == -width:
            SCREEN.blit(BG, (width+i, 0))
            i = 0
            
        i -= 1

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(80).render("Brick Breaker", True, "Red")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("../assets/Play Rect.png"), pos=(640, 250), 
                            text_input="JOGAR", font=get_font(50), base_color="White", hovering_color="Red")
        CREDITS_BUTTON = Button(image=pygame.image.load("../assets/Quit Rect.png"), pos=(640, 400), 
                            text_input="CRÉDITOS", font=get_font(40), base_color="White", hovering_color="Red")
                    
        QUIT_BUTTON = Button(image=pygame.image.load("../assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="SAIR", font=get_font(50), base_color="White", hovering_color="Red")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON,CREDITS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.music.stop() 
                    game = Jogo.Game(SCREEN)
                    game.run()
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    credits()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()