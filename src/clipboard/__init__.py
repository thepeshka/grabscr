import os
import platform

if os.name == 'nt' or platform.system() == 'Windows':
    from clipboard.windows import copy, CLIPBOARD_TYPE
elif os.name == 'mac' or platform.system() == 'Darwin':
    from clipboard.mac import copy, CLIPBOARD_TYPE
else:
    from clipboard.linux import copy, CLIPBOARD_TYPE
