import pygame
game = None

white = 255, 255, 255
yellow = 255, 255, 0
cyan = 0, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
black = 0, 0, 0

class Show():
    def __init__(self):
        self.visible_labels = []
show = Show()


def draw():
    # draw screen
    global game
    screen = game.screen

    screen.fill(black)
    
    # render world
    game.room.render()
    #game.gui.window()
    """

    """
    if game.show_tt:
        game.gui.label('TT: %.0f mins club' % (game.tt()), 610)

    if game.room == game.rooms.world and game.rooms.worldLost29.visible and game.rooms.worldLost54.visible and game.rooms.worldLost55.visible:
        #for ent in game.rooms.world.entities:
        #
        game.rooms.worldLostinf.visible = True
        game.rooms.worldLostinf.clickable = True

    if game.room == game.rooms.irc and not game.rooms.ircBerh.visible and game.tt() < 40:
        game.rooms.ircBerh.visible = True
        game.rooms.ircBerh.clickable = True

    pygame.display.flip()

    #pygame.display.set_mode((640,480),pygame.FULLSCREEN) # messes up screen completely