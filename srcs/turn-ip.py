# Turn/IP
# Claire-lex - 2023
# Main file
# pylint: disable=invalid-name

"""Turn/IP simplifies the research process on industrial network protocols'
security.

The tool stores protocols-related data and provide features to automate some
research phases:
- Give information and resources to understand and start testing a protocol
- Automatically extract information about protocols from trusted sources
- Generate protocols' documentation
- Run utilities to set up the test environment
"""

from sys import argv
from curses import wrapper
# Internal
from ui import CLI, TUI, TUIError, ERROR

try:
    if len(argv) < 2:
        wrapper(TUI().run)
    else:
        CLI().run()
except KeyboardInterrupt:
    pass
except TUIError as tuie:
    ERROR(tuie)
