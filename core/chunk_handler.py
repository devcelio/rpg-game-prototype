from pytmx import TiledMap
from pytmx.util_pygame import pygame_image_loader


def load_tiled_map(filename: str, *args, **kwargs,):
    kwargs["image_loader"] = pygame_image_loader
    return ChunkTiledMap(filename, *args, **kwargs)


class ChunkTiledMap(TiledMap):

    def __init__(self, filename, *args, **kwargs):
        super().__init__(filename, *args, **kwargs)
    