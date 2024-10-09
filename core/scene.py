import pyscroll, pytmx, pygame as pg
from core import settings as conf
from core.game_map import GameMap, load_tiled_map
import timeit
import random


class Scene:

    def __init__(self):
        self.level = load_tiled_map('assets/levels/small_town.tmx')
        self.map_data = pyscroll.TiledMapData(self.level)
        zoom = 1.4
        self.map_layer = pyscroll.BufferedRenderer(self.map_data, (conf.WIDTH / zoom,  conf.HEIGHT / zoom))
        self.map_layer.zoom = zoom
        self.camera_group = pyscroll.PyscrollGroup(map_layer=self.map_layer)
        self.center_rect = None
        self.player = None

    def update(self, delta):
        self.camera_group.update(delta, sprites=self.camera_group, level=self.level)
        self.camera_group.center(self.center_rect)
        # self.get_visible_tiles()

    def get_visible_tiles(self):
        view = self.map_layer.view_rect
        tile_width, tile_height = self.map_data.tile_size
        self.rects = []

        x_left = view.left // tile_width
        x_right = view.right // tile_width

        y_top = view.top // tile_height
        y_bottom = view.bottom // tile_height
        
        """
            for layer in self.level.visible_tile_layers:
                
                for x in range(x_left, x_right):
                    for y in range(y_top, y_bottom):
                        properties = self.level.get_tile_gid(x, y, layer)
                        
                        # if properties:
                        #    collision = pg.rect.Rect((x*tile_width, y*tile_width, tile_width, tile_height))
                        #    print(collision)
                        #if properties:
                        #    px = properties.get_rect(x=x*tile_width, y=y*tile_width)
        """
                        

    def draw(self, display):
        self.camera_group.draw(display)
