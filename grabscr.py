from pathlib import Path
import os

from utils import (
    write_surface_to_clipboard, save_surface, save_surface_as, crop_surface, bbox_xy_to_xywh, get_screenshot_image
)
from controls import Controls, KEY_C, KEY_S, KEY_CTRL, KEY_SHIFT, KEY_ESCAPE
import pygame


os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (0, 0)
os.environ['SDL_VIDEO_CENTERED'] = '0'

BASE_DIR = Path(__file__).resolve().parent
pygame.display.set_caption("GrabSCR")
pygame.display.set_icon(pygame.image.load(BASE_DIR / "icon.png"))
img, size = get_screenshot_image()
display = pygame.display.set_mode(
    size,
    flags=pygame.SCALED | pygame.NOFRAME
)
display.blit(img, (0, 0))
pygame.display.flip()


class AppControls(Controls):
    def __init__(self):
        super().__init__()
        self.bbox = None
        self.running = True

    def on_quit(self):
        self.running = False

    def handle_key_down(self, key):
        if key == KEY_ESCAPE:
            self.running = False
        if key == KEY_C and KEY_CTRL in self.modifiers:
            if self.bbox:
                write_surface_to_clipboard(crop_surface(img, bbox_xy_to_xywh(self.bbox)))
            else:
                write_surface_to_clipboard(img)
            self.running = False
        if key == KEY_S and KEY_CTRL in self.modifiers:
            if KEY_SHIFT in self.modifiers:
                if self.bbox:
                    save_surface_as(crop_surface(img, bbox_xy_to_xywh(self.bbox)))
                else:
                    save_surface_as(img)
            else:
                if self.bbox:
                    save_surface(crop_surface(img, bbox_xy_to_xywh(self.bbox)))
                else:
                    save_surface(img)
            self.running = False

    def handle_lmb_down(self, pos):
        self.bbox = [pos, pos]

    def handle_lmb_up(self):
        (x, y), (w, h) = bbox_xy_to_xywh(self.bbox)
        if w <= 0 or h <= 0:
            self.bbox = None

    def handle_rmb_down(self, pos):
        if not self.lmb_presed:
            self.bbox = None
            display.blit(img, (0, 0))
            pygame.display.flip()

    def handle_mouse_moved(self, pos):
        if self.bbox and self.lmb_presed:
            self.bbox[1] = pos
            display.blit(img, (0, 0))
            pygame.draw.rect(display, (0, 0, 0), bbox_xy_to_xywh(self.bbox), 3)
            pygame.display.flip()


controls = AppControls()

while controls.running:
    controls.handle_events()

pygame.quit()
