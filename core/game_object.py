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
        #for gid, collider in level.get_objects_by_id():
        #    print(vars(collider))
        self.position.x += self.velocity.x * delta * 64
        self.position.y += self.velocity.y * delta * 64
        self.update_rect_position()
