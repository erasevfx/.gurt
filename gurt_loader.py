import pygame as pg
import sys
import os

class GurtLoader:
    def __init__(self, path):
        # pg/window
        pg.init()
        pg.display.set_caption(os.path.basename(path))
        #flags = pg.SCALED | pg.FULLSCREEN
        #self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags)
        self.path = path
        self.screen = pg.display.set_mode(self.get_size())

        # state
        self.running = True

    def get_size(self):
        path = self.path
        with open(path, "rb") as f:
            header = f.read(8)
            magic = header[:4]

            if magic != b'GURT':
                raise ValueError("Not a valid .gurt file")
            
            width = int.from_bytes(header[4:6], 'big')
            height = int.from_bytes(header[6:8], 'big')

            return (width, height)
        
    def render(self):
        path = self.path
        with open(path, "rb") as f:
            header = f.read(8)
            width = int.from_bytes(header[4:6], 'big')
            height = int.from_bytes(header[6:8], 'big')
            pixel_data = f.read(width * height * 3)

            surface = pg.image.fromstring(pixel_data, (width, height), "RGB")

            self.screen.blit(surface, (0, 0))
            pg.display.flip()
        
    def run(self):
        clock = pg.time.Clock()
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            self.render()
            clock.tick(60)
        pg.quit()
        sys.exit()