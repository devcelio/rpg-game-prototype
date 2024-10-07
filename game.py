import pygame as pg
from utils.constants import ColorPalette
from core import settings as conf
from core.scene import Scene
from core.controller_handler import ControllerHandler
from core.game_object import GameObject


class Game:
    def __init__(self):
        self.is_running = False
        self.display = pg.display.set_mode((conf.WIDTH, conf.HEIGHT))
        self.clock = pg.time.Clock()
        self.game_font = pg.font.SysFont('Monospace', 18, True)

    def setup(self):
        self.is_running = True
        self.scene = Scene()
        self.player = GameObject(ColorPalette.CRIMSON, 600, 600)
        self.scene.player = self.player
        self.scene.camera_group.add(self.player, layer=5)

        self.scene.center_rect = self.player.rect
        self.player_controller = ControllerHandler(self.player)
        self.run()

    def draw_fps(self):
        surface = self.game_font.render(f'FPS: {self.clock.get_fps():6.2f}', False, ColorPalette.WHITE, ColorPalette.BLACK)
        self.display.blit(surface, (10, 10))

    def run(self):
        while self.is_running:
            delta = self.clock.tick(0) / 1000
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.is_running = False
            #print(self.player.rect.x // 16, self.player.rect.y // 16)
            self.player_controller.update(delta)
            self.scene.update(delta)
            self.scene.draw(self.display)

            self.draw_fps()
            pg.display.flip()




if __name__ == '__main__':
    pg.init()
    game = Game()
    game.setup()