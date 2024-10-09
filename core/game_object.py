import pygame as pg
from core import settings as conf

class GameObject(pg.sprite.Sprite):
    def __init__(self, color, x, y, width=conf.TILESIZE, height=conf.TILESIZE):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([width, height])
        self.image.fill(color)
        self.position = pg.Vector2(x=x, y=y)
        self.rect = self.image.get_rect()
        self.velocity = pg.Vector2()
        self.update_rect_position()
    
    def update_rect_position(self):
        self.rect.x = self.position.x
        self.rect.y = self.position.y

    def update(self, delta, level, **kwargs):
        # projection_x = None
        move_x, move_y = self.get_movement(level, delta)
        
        
        # if self.velocity.x > 0:
        #     projection_x = self.rect.right + self.velocity.x * delta * 60
        # if self.velocity.x < 0:
        #     projection_x = self.rect.left + self.velocity.x * delta * 60

        # if projection_x and not self.check_collision(level, projection_x, self.position.y):
        # move = delta * self.velocity.x * 60
        # projection_x = None
        # if self.velocity.x > 0:
        #     projection_x = self.rect.right + move
        # if self.velocity.x < 0:
        #     projection_x = self.rect.left + move
        
        # if projection_x and not self.check_collision(level, projection_x, self.position.y):
        #     self.position.x += move
        
        # if projection_y and not self.check_collision(level, self.position.x, projection_y):
        self.update_rect_position()


    def get_movement(self, level, delta):
        move_x = self.velocity.x * delta * 60
        move_y = self.velocity.y * delta * 60
        corners_x = {}
        corners_y = {}

        if self.velocity.x > 0:
            corners_x['a'] = ((self.rect.topright[0] + move_x) // 16, self.rect.top // 16)
            corners_x['b'] = ((self.rect.bottomright[0] + move_x) // 16, self.rect.top // 16)
        
        if self.velocity.x < 0:
            corners_x['a'] = ((self.rect.topleft[0] + move_x) // 16, self.rect.top // 16)
            corners_x['b'] = ((self.rect.bottomleft[0] + move_x) // 16, self.rect.top // 16)

        if self.velocity.y > 0:
            corners_y['a'] = (self.rect.left // 16, (self.rect.topright[1] + move_y) // 16)
            corners_y['b'] = (self.rect.left // 16, (self.rect.bottomright[1] + move_y) // 16)
        
        if self.velocity.y < 0:
            corners_y['a'] = ((self.rect.topleft[0] + move_x) // 16, self.rect.top // 16)
            corners_y['b'] = ((self.rect.bottomleft[0] + move_x) // 16, self.rect.top // 16)

        for layer in level.visible_tile_layers:
            pass
                # corner_a = level.get_tile_properties((self.rect.topright[0] + move_x) // 16, self.rect.top // 16, layer)
                # corner_b = level.get_tile_properties((self.rect.bottomright[0] + move_x) // 16, self.rect.bottom // 16, layer)
                # print(corner_a, corner_b)
        return (move_x, move_y)