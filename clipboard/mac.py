try:
    import pasteboard
except ImportError:
    raise RuntimeError("pasteboard not found")

CLIPBOARD_TYPE = "png"


def copy(data):
    pasteboard.Pasteboard().set_contents(data, pasteboard.PNG)
