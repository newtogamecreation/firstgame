import math
import pygame, sys, time
from pygame.locals import *
import random

BLACK = (0, 0, 0)  # BackGROUND
game_score = 0
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 245)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
color_mix = (0, 0, 0)
STEELBLUE = (70, 130, 180)
color_list = [BLUE, RED, WHITE, GREEN, YELLOW, GRAY, STEELBLUE]
color_key = ["l", "r", "w", "g", "y", "a", "s"]
score_plus="snare.wav"
score_minus="10.wav"




print("Game point initilized", game_score)
pygame.init()
pygame.mixer.init()

color_mix = random.choice(color_list)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('random circles')
print(color_mix)
pygame.draw.circle(surface, color_mix, (100, 100), 25, 1)
help_str=["A random color circle displayed on screen",
          "Color are BLUE, RED, WHITE, GREEN, YELLOW, GRAY, STEELBLUE",
          "Keys are l-blue, r-red, w-white, g-green, y-yellow, a-gray, s-steel blue",
          "Press the key to displayed color to continue," 
          "Press escape to quit",
          "            ",
          "            ",
          "I thank my",
          "Parents and family for the support",
          "stackoverflow community",
          "pygame community",
          "openart for sound effects",
          "  ",
          "  ",
          ]
x_coord=300
y_coord=200
for i in range(len(help_str)):
    score_text = pygame.font.Font("freesansbold.ttf", 15)
    text_socreobj = score_text.render(help_str[i], True, WHITE, BLACK)
    text_scorerect = text_socreobj.get_rect()
    text_scorerect.center = (x_coord, y_coord)
    surface.blit(text_socreobj, text_scorerect)
    y_coord=y_coord+20

class game_main():
    def __init__(self):
        self.game_score=0


    def game_logic(self,key_pressed):
        #print(color_list)
        #print(color_key)
        #print(color_mix)

        try:
            if key_pressed=='escape':

                pygame.quit()
                sys.exit()
            if key_pressed in color_key:


                #print(color_key.index(key_pressed))
                #print(key_pressed)
                key_idx=color_key.index(key_pressed)
                #print(key_idx)
                #print(color_list[key_idx])
                if color_list[key_idx]==color_mix:
                    if self.game_score>=0:
                        self.game_score+=10
                    elif self.game_score<0:
                        self.game_score-=10

                    pygame.mixer.music.load(open(score_plus, "rb"))
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy():
                       time.sleep(1)
                    pygame.mixer.stop()
                else:
                    if self.game_score>=0:
                        self.game_score-=10
                    elif self.game_score<0:
                        self.game_score+=10

                    pygame.mixer.music.load(open(score_minus, "rb"))
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy():
                        time.sleep(1)
                    pygame.mixer.stop()
                    #print(self.game_score)

                surface.fill(BLACK)
                score_text=pygame.font.Font("freesansbold.ttf",20)
                text_socreobj=score_text.render("Score="+str(self.game_score),True,GREEN,BLACK)
                text_scorerect=text_socreobj.get_rect()
                text_scorerect.center=(150,10)
                surface.blit(text_socreobj,text_scorerect)


                x_coord=random.randint(100,400)
                y_coord=random.randint(x_coord,400)
                pygame.draw.circle(surface, color_mix, (x_coord, y_coord), 25, 1)

            else:
                   pass #print("the pressed in invalid")

        except:
            print("Quitting", sys.exc_info())
            print()
            pygame.quit()
            sys.exit(1)


new_game=game_main()
while True:
    for event in pygame.event.get():

        if event.type==pygame.KEYDOWN:
            key_pressed=pygame.key.name(event.key).lower()
            color_mix=random.choice(color_list)
            new_game.game_logic(key_pressed)

    pygame.display.update()