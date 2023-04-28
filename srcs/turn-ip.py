# Turn/IP
# Claire-lex - 2023
# Main file

from sys import argv
# Internal
from ui import CLI, TUI
from db import MongoDB

if len(argv) < 2:
    interface = TUI()
else:
    interface = CLI()

interface.run(argv[1:] if len(argv) > 1 else None)
