import pygame, sys, time, os

# screen needs to be initialized before loading sprites, which rooms does on start
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
size = 800, 640
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Elma RPG 3D HD')

import keys, mouse, draw, gui, rooms, dialog

# http://stackoverflow.com/questions/5814125/how-to-designate-where-pygame-creates-the-game-window

class Game:
    def __init__(self):
        # init pygame
        self.size = self.width, self.height = size
        #self.screen = pygame.display.set_mode(self.size)
        self.screen = screen
        
        self.pygame = pygame
        # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
        self.font = pygame.font.SysFont("monospace", 18)

        self.gui = gui
        self.draw = draw
        self.rooms = rooms
        self.dialog = dialog
        gui.game = self
        draw.game = self
        rooms.game = self
        dialog.game = self

        self.fullscreen = False
        self.room = rooms.world
        self.current_dialog = None
        self.show_everything = False
        self.show_tt = False
        self.clipboard = False

    def tt(self):
        "Count total time for all internals. Makes tt around 39 with good time on all."
        tt = 0
        for level in (self.rooms.warmup, self.rooms.flattrack, self.rooms.slesk, self.rooms.nekitbattle, self.rooms.nabland):
            tt += level.pr or 500.0
        return tt/10

game = Game()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            running = keys.keyup(event, game)
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse.buttonup(event, game)

    draw.draw()
    # keep a framerate of max 33.333
    #if tick < 0.03:
    #    #print("sleeping %.2f" % (0.03 - tick))
    #    time.sleep(0.03 - tick)
    