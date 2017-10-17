import pygame

def buttonup(event, game):
    "on button up"
    #mods = pygame.key.get_mods()

    #if event.key == pygame.K_q and mods & pygame.KMOD_CTRL:
    #    return False # exit game

    x, y = pygame.mouse.get_pos()
    if event.button == 2:
        # mid button
        print( x,y )


    for entity in game.room.entities:
        if not entity.clickable and not game.show_everything:
            continue

        if entity.label or entity.filename:
            #text_width, text_height = entity.label_size()
            #if x >= entity.x and x <= entity.x + text_width and y >= entity.y and y <= entity.y + text_height:
            bbox = entity.bbox()
            #print( bbox, x, y )
            if x >= bbox[0] and x <= bbox[2] and y >= bbox[1] and y <= bbox[3]:
                # object was clicked
                entity.clicked(event)


    if game.room.hoyling:
        for apple in game.room.apples:
            bbox = apple[0], apple[1], apple[0] + 20, apple[1] + 20
            if x >= bbox[0] and x <= bbox[2] and y >= bbox[1] and y <= bbox[3]:
                game.room.apple_clicked(apple)

        for flower in game.room.flowers:
            bbox = flower[0], flower[1], flower[0] + 20, flower[1] + 20
            if x >= bbox[0] and x <= bbox[2] and y >= bbox[1] and y <= bbox[3]:
                game.room.flower_clicked(flower)
