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
# Internal
from ui import CLI, TUI

if len(argv) < 2:
    interface = TUI()
else:
    interface = CLI()

interface.run()
