import subprocess
import tkinter
import tkinter.filedialog
from datetime import datetime
from io import BytesIO
from pathlib import Path

import numpy as np
import pygame_hide_prompt
import pygame
from mss import mss

import clipboard


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
    pygame.image.save(surface, buffer, "." + clipboard.CLIPBOARD_TYPE)
    clipboard.copy(buffer.getvalue())


def save_surface(surface: pygame.Surface, file=None):
    pygame.image.save(
        surface,
        file or Path(f"~/Pictures/Screenshot from {datetime.now():%Y-%m-%d %H-%M-%S}.png").expanduser()
    )


def save_surface_as(surface: pygame.Surface):
    top = tkinter.Tk()
    top.withdraw()
    tkinter.filedialog.SaveAs()
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
    if bbox[0][0] > bbox[1][0]:
        x_min, x_max = bbox[1][0], bbox[0][0]
    else:
        x_min, x_max = bbox[0][0], bbox[1][0]
    if bbox[0][1] > bbox[1][1]:
        y_min, y_max = bbox[1][1], bbox[0][1]
    else:
        y_min, y_max = bbox[0][1], bbox[1][1]
    return (x_min, y_min), (x_max - x_min, y_max - y_min)


def get_screenshot_image():
    with mss() as sct:
        screenshot = sct.grab(sct.monitors[0])

        return pygame.image.frombuffer(
            screenshot.rgb,
            screenshot.size,
            "RGB"
        ), screenshot.size
