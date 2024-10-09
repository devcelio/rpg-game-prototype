from pytmx import TiledMap
from pytmx.util_pygame import pygame_image_loader
import pygame as pg

def load_tiled_map(filename: str, *args, **kwargs,):
    kwargs["image_loader"] = pygame_image_loader
    return GameMap(filename, *args, **kwargs)


class GameMap(TiledMap):

    def __init__(self, filename, *args, **kwargs):
        super().__init__(filename, *args, **kwargs)
        # for layer in self.visible_layers:
            #for x,y,gid in layer.iter_data():
            #    properties = self.get_tile_properties_by_gid(gid)
            #    if properties and properties.get('colliders'):
            #        rct = 