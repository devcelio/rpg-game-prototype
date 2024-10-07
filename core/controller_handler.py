import pygame as pg


class ControllerHandler:

    def __init__(self, game_object):
        self.game_object = game_object

    def update(self, delta):
        key = pg.key.get_pressed()
        velocity = self.game_object.velocity
        velocity.x = 0
        velocity.y = 0

        if key[pg.K_UP]:
            velocity.y = -1

        if key[pg.K_DOWN]:
            velocity.y = 1

        if key[pg.K_LEFT]:
            velocity.x = -1

        if key[pg.K_RIGHT]:
            velocity.x = 1

        if velocity.x and velocity.y:
            self.game_object.velocity = velocity.normalize()  
