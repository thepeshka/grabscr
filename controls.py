import pygame

KEY_ESCAPE = 41
KEY_CTRL = 224
KEY_SHIFT = 225
KEY_C = 6
KEY_S = 22
LMB = 1
RMB = 3


class Controls:
    def __init__(self):
        self.modifiers = []
        self.lmb_presed = False
        self.rmb_pressed = False

    def on_quit(self):
        pass

    def handle_key_down(self, key):
        pass

    def handle_key_up(self, key):
        pass

    def handle_lmb_down(self, pos):
        pass

    def handle_rmb_down(self, pos):
        pass

    def handle_lmb_up(self):
        pass

    def handle_rmb_up(self):
        pass

    def handle_mouse_moved(self, pos):
        pass

    def handle_events(self):
        try:
            if pygame.event.get(pygame.QUIT):
                self.on_quit()
            for e in pygame.event.get(pygame.KEYDOWN):
                if e.scancode in [KEY_CTRL, KEY_SHIFT]:
                    if e.scancode not in self.modifiers:
                        self.modifiers.append(e.scancode)
                self.handle_key_down(e.scancode)

            for e in pygame.event.get(pygame.KEYUP):
                if e.scancode in [KEY_CTRL, KEY_SHIFT]:
                    if e.scancode in self.modifiers:
                        self.modifiers.remove(e.scancode)
                self.handle_key_up(e.scancode)

            for e in pygame.event.get(pygame.MOUSEBUTTONDOWN):
                if e.button == LMB:
                    self.lmb_presed = True
                    self.handle_lmb_down(e.pos)

                if e.button == RMB:
                    self.rmb_pressed = True
                    self.handle_rmb_down(e.pos)

            for e in pygame.event.get(pygame.MOUSEMOTION):
                self.handle_mouse_moved(e.pos)

            for e in pygame.event.get(pygame.MOUSEBUTTONUP):
                if e.button == LMB:
                    self.lmb_presed = False
                    self.handle_lmb_up()

                if e.button == RMB:
                    self.rmb_pressed = False
                    self.handle_rmb_up()
        except KeyboardInterrupt:
            self.on_quit()
