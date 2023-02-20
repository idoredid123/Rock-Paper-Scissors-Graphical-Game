import pygame, random

pygame.init()
pygame.font.init()

WINDOW_HEIGHT = 750
WINDOW_WIDTH = 630

#Setting up the game
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
pygame.display.set_caption('Paper Rock Scissors')


run_program = True
clock = pygame.time.Clock()

#Players Pictures Loading
bot = pygame.image.load("computer.png")
human = pygame.image.load("human.png")

#Options Pictures Loading
rock = pygame.image.load("rock.png")
paper = pygame.image.load("paper.png")
scissors = pygame.image.load("scissors.png")

def redraw_window():
    background = pygame.image.load("background.png")
    screen.blit(bot, (2, 50))
    screen.blit(human, (20, 30))
    screen.blit(rock, (50, 40))
    screen.blit(paper, (0, 20))
    screen.blit(scissors, (15, 20))

def main():
    '''
    The main function of the program, includes the program flow and running including FPS and drawing functions.
    '''

    run_program = True

    #Main prorgam loop
    while run_program:
        clock.tick(40) #40 Frames Per Second (FPS)
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_program = False
        
        redraw_window()
                
if __name__ == '__main__':
    main()

