try:
    import win32clipboard
except ImportError:
    raise RuntimeError("pywin32 is not installed")

CLIPBOARD_TYPE = "bmp"


def copy(data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data[14:])
    win32clipboard.CloseClipboard()
