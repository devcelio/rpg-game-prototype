import pygame as pg
from utils.constants import ColorPalette
from pytmx.util_pygame import load_pygame as load_pytmx
import pyscroll

WIDTH = 640
HEIGHT = 480
TILESIZE = 16

class GameObject(pg.sprite.Sprite):
    def __init__(self, color, x, y, width=TILESIZE, height=TILESIZE):
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

    def update(self, delta, sprites):
        self.position += self.velocity * delta * 64
        # print(sprites)
        self.update_rect_position()


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

class Scene:

    def __init__(self):
        self.level = load_pytmx('assets/levels/small_town.tmx')


class Game:
    def __init__(self):
        self.is_running = False
        self.display = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.game_font = pg.font.SysFont('Monospace', 18, True)

    def setup(self):
        self.is_running = True
        self.level = Scene()
        self.player = GameObject(ColorPalette.CRIMSON, 300, 300)
        self.player_controller = ControllerHandler(self.player)
        self.map_data = pyscroll.TiledMapData(self.level.level), (WIDTH / 1.5,  HEIGHT / 1.5)
        self.map_layer = pyscroll.BufferedRenderer(self.map_data)
        self.camera_group = pyscroll.PyscrollGroup(map_layer=self.map_layer, layer=-1)

        self.map_layer.zoom = 1.5

        self.camera_group.add(self.player, layer=4)
        self.run()

    def draw_fps(self):
        surface = self.game_font.render(f'FPS: {self.clock.get_fps():6.2f}', False, ColorPalette.WHITE, ColorPalette.BLACK)
        self.display.blit(surface, (10, 10))

    def run(self):
        # print(dir(self.map_layer.data.visi))

        print(self.map_data)
        while self.is_running:
            delta = self.clock.tick(0) / 1000
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.is_running = False

            self.player_controller.update(delta)
            self.camera_group.update(delta, sprites=self.camera_group)
            self.camera_group.center(self.player.rect)
            self.camera_group.draw(self.display)

            self.draw_fps()
            pg.display.flip()




if __name__ == '__main__':
    pg.init()
    game = Game()
    game.setup()