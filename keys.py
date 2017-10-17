import pygame

def keyup(event, game):
    "on key up"
    mods = pygame.key.get_mods()

    if event.key == pygame.K_q and mods & pygame.KMOD_CTRL:
        return False # CTRL + Q     exit game

    if event.key == pygame.K_c and mods & pygame.KMOD_CTRL:
        game.clipboard = True

    if event.key == pygame.K_v and mods & pygame.KMOD_CTRL:
        if game.clipboard:
            game.room.flower_clicked(cheat=True) # CTRL + V     paste style (for finishing lev ez)

    # uncommented for release
    #if event.key == pygame.K_a and mods & pygame.KMOD_CTRL:
    #    game.show_everything = not game.show_everything # CTRL + A     toggle show everything

    if event.key == pygame.K_t:
        game.show_tt = not game.show_tt # T     toggle show total time

    if event.key == pygame.K_ESCAPE:
            game.clipboard = False
            if game.room.hoyling:
                game.room.hoyl_stop()
            elif game.current_dialog and game.current_dialog.line:
                game.current_dialog.line = None
            else:
                game.room = game.rooms.world

    # http://stackoverflow.com/a/28929857
    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE: #Just a key to toggle fullscreen
        # pygame.display.toggle_fullscreen() # not working, at least on windows
        display = (800, 640)
        if pygame.display.get_driver()=='x11':
            pygame.display.toggle_fullscreen()
        else:
            acopy = game.screen.copy()                    
        if game.fullscreen:
            screen = pygame.display.set_mode(display)
            game.fullscreen = False
        else:
            screen = pygame.display.set_mode(display, pygame.FULLSCREEN)
            game.fullscreen = True
            screen.blit(acopy, (0,0))                    
            pygame.display.update()

    if event.key in (pygame.K_1, pygame.K_KP1, pygame.K_2, pygame.K_KP2, pygame.K_3, pygame.K_KP3, pygame.K_4, pygame.K_KP4, pygame.K_5, pygame.K_KP5, 
                    pygame.K_6, pygame.K_KP6, pygame.K_7, pygame.K_KP7, pygame.K_8, pygame.K_KP8, pygame.K_9, pygame.K_KP9, ):
        #print(game.dialog)
        if game.current_dialog and game.current_dialog.line and game.current_dialog.linehasoptions():
            if event.key in (pygame.K_1, pygame.K_KP1): game.current_dialog.triggeroption(1)
            if event.key in (pygame.K_2, pygame.K_KP2): game.current_dialog.triggeroption(2)
            if event.key in (pygame.K_3, pygame.K_KP3): game.current_dialog.triggeroption(3)
            if event.key in (pygame.K_4, pygame.K_KP4): game.current_dialog.triggeroption(4)
            if event.key in (pygame.K_5, pygame.K_KP5): game.current_dialog.triggeroption(5)
            if event.key in (pygame.K_6, pygame.K_KP6): game.current_dialog.triggeroption(6)
            if event.key in (pygame.K_7, pygame.K_KP7): game.current_dialog.triggeroption(7)
            if event.key in (pygame.K_8, pygame.K_KP8): game.current_dialog.triggeroption(8)
            if event.key in (pygame.K_9, pygame.K_KP9): game.current_dialog.triggeroption(9)

    # saves not implemented
    """if event.key in (pygame.K_F1, pygame.K_F2, pygame.K_F3, pygame.K_F4, pygame.K_F5, pygame.K_F6, pygame.K_F7, pygame.K_F8, pygame.K_F9, pygame.K_F10, pygame.K_F11, pygame.K_F12):
        import dill
        with open('save%d.pkl' % event.key, 'wb') as output:
            pickle.dump(game, output, pickle.HIGHEST_PROTOCOL)"""

    """if event.key == pygame.K_LEFT:
        if game.room and game.room.image:
            #game.room.image = pygame.transform.rotate(game.room.image, 30) # horrible rotation
            game.room.x -= 5

    if event.key == pygame.K_RIGHT:
        if game.room and game.room.image:
            # game.room.image = pygame.transform.rotate(game.room.image, -30) # horrible rotation
            game.room.x += 5

    if event.key == pygame.K_UP:
        if game.room and game.room.image:
            #game.room.image = pygame.transform.rotate(game.room.image, 30) # horrible rotation
            game.room.y -= 5

    if event.key == pygame.K_DOWN:
        if game.room and game.room.image:
            # game.room.image = pygame.transform.rotate(game.room.image, -30) # horrible rotation
            game.room.y += 5"""

    """if event.key == pygame.K_ESCAPE:
        pass # running = False
    if event.key == pygame.K_SPACE:
        gametime.pause()
    if event.key in (pygame.K_PLUS, pygame.K_KP_PLUS):
        gametime.faster()
    if event.key in (pygame.K_MINUS, pygame.K_KP_MINUS):
        gametime.slower()
    if event.key in (pygame.K_0, pygame.K_KP0):
        draw.show.messages = not draw.show.messages
    if event.key in (pygame.K_9, pygame.K_KP9):
        draw.show.stats = not draw.show.stats"""

    return True