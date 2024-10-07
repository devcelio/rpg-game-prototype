import pyscroll, pytmx, pygame as pg
from core import settings as conf
from core.chunk_handler import ChunkTiledMap, load_tiled_map
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
        """
        I realized the loading takes more time because of the large amount of rects.
        If you keep the amount of collisions small, it won't take that long to load

        """
        self.simulate_collisions = False # Change this to disable the collision simulation)
        if self.simulate_collisions:
            self.load_rects()

    def load_rects(self):
        self.rects = [
            pg.Rect((random.randint(0, 30), random.randint(0, 30), 32, 32)) # simulating instantiation of many collision rects
            for i in range(1_000_000)
        ]

    def update(self, delta):
        if self.simulate_collisions:
            for i in range(100): # simulating 100 sprites calculating collision vs rects
                for r in self.rects:
                    r.colliderect(self.player.rect)

        self.camera_group.update(delta, sprites=self.camera_group, level=self.level)
        self.camera_group.center(self.center_rect)
        self.get_visible_tiles()

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
