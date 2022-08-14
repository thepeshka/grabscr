import subprocess
import tkinter
import tkinter.filedialog
from datetime import datetime
from io import BytesIO
from pathlib import Path

from Xlib import X
from Xlib.display import Display
import numpy as np
import pygame_hide_prompt
import pygame


def bgra2rgb(rgba):
    rgba = rgba.reshape((rgba.shape[0] // 4, 4))
    rgb = np.zeros((rgba.shape[0], 3), dtype=np.uint8)
    b, g, r = rgba[:, 0], rgba[:, 1], rgba[:, 2]
    rgb[:, 0] = r
    rgb[:, 1] = g
    rgb[:, 2] = b
    return rgb.flatten().tobytes()


def write_surface_to_clipboard(surface: pygame.Surface):
    buffer = BytesIO()
    pygame.image.save(surface, buffer, ".png")
    cmd = subprocess.Popen(
        ["xclip", "-sel", "clip", "-t", "image/png"],
        stdin=subprocess.PIPE
    )
    cmd.stdin.write(buffer.getvalue())


def save_surface(surface: pygame.Surface, file=None):
    pygame.image.save(
        surface,
        file or Path(f"~/Pictures/Screenshot from {datetime.now():%Y-%m-%d %H-%M-%S}.png").expanduser()
    )


def save_surface_as(surface: pygame.Surface):
    top = tkinter.Tk()
    top.withdraw()
    file_name = tkinter.filedialog.asksaveasfilename(
        parent=top,
        defaultextension='.png',
        filetypes=[
            ("PNG", '*.png'),
            ("JPG", '*.jpg'),
            ("BMP", '*.bmp'),
            ("TGA", '*.tga'),
        ],
        title="Choose path to save screenshot"
    )
    top.destroy()
    if not file_name:
        return
    save_surface(surface, file_name)


def crop_surface(surface: pygame.Surface, bbox):
    cropped = pygame.Surface(bbox[1])
    cropped.blit(surface, (0, 0), bbox)
    return cropped


def bbox_xy_to_xywh(bbox):
    return bbox[0], [bbox[1][0] - bbox[0][0], bbox[1][1] - bbox[0][1]]


def get_screenshot_image():
    xdisplay = Display().screen().root
    geometry = xdisplay.get_geometry()
    width, height = geometry.width, geometry.height
    return pygame.image.frombuffer(
        bgra2rgb(
            np.frombuffer(
                xdisplay.get_image(0, 0, width, height, X.ZPixmap, 0xffffffff).data,
                np.uint8
            )
        ),
        (width, height),
        "RGB"
    ), (width, height)
