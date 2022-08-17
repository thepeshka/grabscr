import os
import subprocess
from shutil import which

CLIPBOARD_TYPE = "png"

if (
        os.environ.get("WAYLAND_DISPLAY") and
        which("wl-copy")
):
    def copy(data):
        cmd = subprocess.Popen(
            ["wl-copy", "-t", "image/png"],
            stdin=subprocess.PIPE
        )
        cmd.stdin.write(data)


elif which("xclip"):
    def copy(data):
        cmd = subprocess.Popen(
            ["xclip", "-sel", "clip", "-t", "image/png"],
            stdin=subprocess.PIPE
        )
        cmd.stdin.write(data)

else:
    raise RuntimeError("Clipboard library not found")
