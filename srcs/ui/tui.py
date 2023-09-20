# Turn/IP
# Claire-lex - 2023
# Terminal user interface
# pylint: disable=invalid-name,too-many-instance-attributes,too-many-arguments
# pylint: disable=attribute-defined-outside-init,no-self-use

"""Terminal user interface
"""

import curses
from enum import Enum, IntEnum
from bson.objectid import ObjectId
# Internal
from config import tui as t, protocols as p, packets as pk, mongodb
from config import TOOL_TITLE
from db import MongoDB, DBException
from db import Protocols, Links, Packets

#-----------------------------------------------------------------------------#
# Constants                                                                   #
#-----------------------------------------------------------------------------#

class Screen(Enum):
    """ID to select screens."""
    MAIN = 1
    PROT = 2

# Main screen focus
class Focus(IntEnum):
    """ID to change focus on screen items."""
    MAIN_LIST = 0
    MAIN_MENU = 1

ERR_TERMSIZE = "Terminal is to small to display user interface."

#-----------------------------------------------------------------------------#
# TUI classes                                                                 #
#-----------------------------------------------------------------------------#

class TUIError(Exception):
    """Exception class for curses-related errors."""

class TUI():
    """Terminal User Interface main class.

    Important note: y = lines & x = cols. y comes first in curses.
    """
    __loop = False
    cursors = None # Dictionary of current cursors' positions in lists
    focus = None # List currently focused
    height = None
    search = None # Search buffer
    startpos = None # Dictionary of current starting positions for displays
    width = None

    db = None
    protocols = None
    links = None
    packets = None

    def __filter_list(self, ilist: list) -> list:
        """Returned a filtered list according to parameters search and filter."""
        olist = []
        search = "".join(self.search).lower().strip()
        for item in ilist:
            if search in item.lower():
                olist.append(item)
        return olist
    
    @property
    def filtered_list(self):
        """List filtered according to the values of search and filter."""
        return self.__filter_list([x.name for x in self.protocols.all_as_objects])

    # tmp
    def nop(self):
        """Does nothing, will be removed."""

    #--- Init ----------------------------------------------------------------#

    def __init__(self):
        self.__init_content()
        self.search = []
        self.focus = Focus.MAIN_LIST
        self.cursors = {
            Focus.MAIN_LIST: 0,
            Focus.MAIN_MENU: 0
        }
        self.startpos = {
            Focus.MAIN_LIST: 0,
            Focus.MAIN_MENU: 0
        }

    def __init_content(self):
        """Extract required data from the database."""
        try:
            self.db = MongoDB()
        except DBException as dbe:
            raise TUIError(dbe) from None
        self.protocols = Protocols()
        self.links = Links()
        self.packets = Packets()

    def __init_menu(self):
        """Prepare the main menu with appropriate actions."""
        self.menu = {
            t.menu_view: self.__view_protocol,
            t.menu_edit: self.nop,
            t.menu_quit: self.__end_loop
        }

    def __init_color(self):
        """Init curses internal features."""
        curses.start_color()
        curses.use_default_colors()
        curses.curs_set(0) # Invisible cursor

    #--- Run -----------------------------------------------------------------#

    def run(self, screen):
        """Display init and main loop."""
        self.__screen = screen
        self.__loop = True
        self.__init_color()
        self.__init_menu()
        self.__run_screen(Screen.MAIN)
        while self.__loop:
            if self.__out_of_bounds():
                raise TUIError(ERR_TERMSIZE)
            self.__screen.refresh()
            self.__process_events(self.__screen.getch())
            self.__run_screen()

    def __run_screen(self, screen: int = None) -> None:
        """Display the current screen or screen passed as argument."""
        if screen: # If screen not empty, we set a new screen
            self.screen = screen
        # Load the appropriate screen
        if self.screen == Screen.MAIN:
            self.__set_main_screen()
        elif self.screen == Screen.PROT:
            self.__set_prot_screen()

    def __run_menu(self):
        """Run the appropriate operation according to the selected menu item."""
        if self.cursors[Focus.MAIN_MENU] in range(len(self.menu)):
            list(self.menu.values())[self.cursors[Focus.MAIN_MENU]]()

    def __view_protocol(self):
        """Switch to protocol view according to protocol under cursor."""
        if self.cursors[Focus.MAIN_LIST] < len(self.filtered_list):
            self.protocol = self.filtered_list[self.cursors[Focus.MAIN_LIST]]
            self.__run_screen(Screen.PROT)

    #--- Events --------------------------------------------------------------#

    def __process_events(self, key) -> None:
        """Associate events to actions depending on the current screen."""
        if self.screen == Screen.MAIN:
            self.__process_events_main(key)
        elif self.screen == Screen.PROT:
            self.__process_events_prot(key)
        # Events common to all screens
        if key in (curses.KEY_DOWN, curses.KEY_RIGHT):
            self.__move_cursor(1)
        elif key in (curses.KEY_UP, curses.KEY_LEFT):
            self.__move_cursor(-1)

    def __process_events_main(self, key) -> None:
        """Process events on the main screen."""
        # ENTER
        if key in (curses.KEY_ENTER, 10, 13):
            if self.focus == Focus.MAIN_LIST: # Switch to protocol page
                self.__view_protocol()
            elif self.focus == Focus.MAIN_MENU:
                self.__run_menu()
        # ESCAPE
        elif key == 27:
            self.__end_loop()
        # TEXT (search)
        elif 20 <= key < 127:
            self.search.append(chr(key))
        elif key == curses.KEY_BACKSPACE:
            self.search = self.search[:-1]
        elif key == 9: # TAB
            self.__switch_focus()

    def __process_events_prot(self, key) -> None:
        """Process events on protocols screens."""
        # ESCAPE
        if key == 27:
            self.__run_screen(Screen.MAIN)

    def __move_cursor(self, value: int) -> None:
        """Move the cursor of the focused vertical list."""
        max_value = {
            Focus.MAIN_LIST: len(self.filtered_list) - 1,
            Focus.MAIN_MENU: len(self.menu) - 1
        }
        if self.cursors[self.focus] + value < 0:
            self.cursors[self.focus] = max_value[self.focus]
        elif self.cursors[self.focus] + value > max_value[self.focus]:
            self.cursors[self.focus] = 0
        else:
            self.cursors[self.focus] += value

    def __switch_focus(self):
        """Change the focus depending on the list of available focuses."""
        focus = [x.value for x in Focus]
        ct = 0 if self.focus + 1 >= len(focus) else self.focus + 1
        self.focus = focus[ct]

    def __display_list(self, window, w: int, h: int, content: list, focus: int):
        """Display the list on the screen, rotate if the list is too big to display.

        self.cursors[focus] = Current position of the cursor in the list
        self.startpos[focus] = Position to display the list from
        """
        max_pos = h - 3
        fmt = " {{0: <{0}}}".format(w - 3)
        if self.cursors[focus] - self.startpos[focus] >= max_pos:
            self.startpos[focus] = self.cursors[focus] - max_pos
        if self.cursors[focus] < self.startpos[focus]:
            self.startpos[focus] = self.cursors[focus]
        # start_pos = pos - max_pos if pos > max_pos else 0
        for i in range(len(content)):
            if i >= h - 2:
                break
            if self.focus == focus and self.cursors[focus] == i + self.startpos[focus]:
                window.addstr(
                    i + 1, 1, fmt.format(content[i + self.startpos[focus]][:w - 4]),
                    curses.A_STANDOUT
                )
            else:
                window.addstr(
                    i + 1, 1, fmt.format(content[i + self.startpos[focus]][:w - 4])
                )

    #--- Main screen ---------------------------------------------------------#

    def __set_main_screen(self) -> None:
        """Displays the components of the main screen."""
        self.__screen.clear()
        self.height, self.width = self.__screen.getmaxyx()
        curses.setsyx(0, 0)
        # Calculate subwindows' sizes
        # search = 2/3 width, filter = 1/3 width
        h_search, w_search = 3, self.width - int(self.width / 3) - 2
        h_filter, w_filter = 3, int(self.width / 3) - 2
        # menu = 1/3 width ; notes = 2/3 width
        h_menu, w_menu = int(self.height / 4), int(self.width / 3) - 2
        h_note, w_note = h_menu, self.width - int(self.width / 3) - 2
        # list = 1/3 width ; info = 2/3 width
        h_list, w_list = self.height - h_search - h_menu - 5, int(self.width / 3) - 2
        h_info, w_info = h_list, int(self.width - self.width / 3) - 2
        # Create subwindows
        self.__f_header(0, 0, TOOL_TITLE)
        self.__f_search(h_search, w_search, 2, 1, t.title_search)
        self.__f_filter(h_filter, w_filter, 2, self.width - w_filter - 1, t.title_filter)
        self.__f_list(h_list, w_list, 6, 1, t.title_list_prot,
                      self.filtered_list, Focus.MAIN_LIST)
        self.__f_info_prot(h_info, w_info, 6, self.width - w_info - 1, t.title_info_prot)
        self.__f_info_note(h_note, w_note - 1, self.height - h_menu - 1,
                           self.width - w_note, t.title_info_note)
        self.__f_list(h_menu, w_menu, self.height - h_menu - 1, 1, t.title_menu,
                      list(self.menu.keys()), Focus.MAIN_MENU)
        self.__f_footer(self.height - 1, 0,
                        t.footer_fmt.format(self.cursors[Focus.MAIN_LIST] + 1,
                                            self.protocols.count))
        self.__screen.refresh()

    #--- Protocol screen -----------------------------------------------------#

    def __set_prot_screen(self) -> None:
        """displays the components of the protocol screens."""
        self.__screen.clear()
        self.height, self.width = self.__screen.getmaxyx()
        curses.setsyx(0, 0)
        self.__f_header(0, 0, self.protocol)
        # TODO
        self.__screen.refresh()

    #--- Screen items --------------------------------------------------------#

    def __f_header(self, y: int, x: int, title: str) -> None:
        """Header line with title."""
        format_header = "{{0: ^{0}}}".format(str(self.width))
        self.__screen.addstr(y, x, format_header.format(title.upper()),
                             curses.A_STANDOUT)

    def __f_footer(self, y: int, x: int, footer) -> None:
        """Footer line with text."""
        format_footer = "{{0: >{0}}} ".format(str(self.width - 2))
        self.__screen.addstr(y, x, format_footer.format(footer))

    def __f_search(self, h: int, w: int, y: int, x: int, title: str) -> None:
        """Search bar, text can be written to it."""
        winsearch = self.__screen.subwin(h, w, y, x)
        winsearch.border()
        winsearch.addstr(0, 1, " {0} ".format(title))
        if self.search:
            for i in range(0, len(self.search)):
                winsearch.addstr(1, i + 2, self.search[i])
        winsearch.refresh()

    # TODO
    def __f_filter(self, h: int, w: int, y: int, x: int, title: str) -> None:
        """Filter bar, can only contain a list of preset values."""
        winfilter = self.__screen.subwin(h, w, y, x)
        winfilter.border()
        winfilter.addstr(0, 1, " {0} ".format(title))
        winfilter.refresh()

    def __f_list(self, h: int, w: int, y: int, x: int, title: str,
                 dlist: list, focus: int) -> None:
        """Vertical list of items."""
        winlist = self.__screen.subwin(h, w, y, x)
        winlist.border()
        winlist.addstr(0, 1, " {0} ".format(title))
        self.__display_list(winlist, w, h, dlist, focus)
        winlist.refresh()

    # TODO: REFACTO
    def __f_info_prot(self, h: int, w: int, y: int, x: int, title: str) -> None:
        """Text box to display information."""
        fmt = "{0: <20}: {1}"
        max_len = w - 20 - 6 # Size of key + size of border
        winprotoinfo = self.__screen.subwin(h, w, y, x)
        winprotoinfo.border()
        winprotoinfo.addstr(0, 1, " {0} ".format(title))
        # Display content
        if self.cursors[Focus.MAIN_LIST] in range(len(self.filtered_list)):
            protocol = self.filtered_list[self.cursors[Focus.MAIN_LIST]]
            protocol = self.protocols.get(protocol).to_dict()
            line = 1
            for k, v in protocol.items():
                # Format
                if k == mongodb.id or not v:
                    continue
                if k in p.ALL_FIELDS:
                    k = p.NAME(k)
                elif k in pk.FIELDS.keys(): # Packets
                    k = pk.FIELDS[k]
                else:
                    k = k.capitalize()
                if isinstance(v, list) and isinstance(v[0], ObjectId):
                    # self.__print_ids(table_format, k, v)
                    continue
                if isinstance(v, list):
                    v = ", ".join(v)
                if isinstance(v, str):
                    v = [v[i:i + max_len] for i in range(0, len(v), max_len)]
                # Display
                if isinstance(v, list):
                    for e in v:
                        winprotoinfo.addstr(line, 2, fmt.format(k, e))
                        k = ""
                        line += 1
        winprotoinfo.refresh()

    # TODO
    def __f_info_note(self, h: int, w: int, y: int, x: int, title: str) -> None:
        """Text box to display information."""
        # max_len = w - 6 # Size of key + size of border
        winnoteinfo = self.__screen.subwin(h, w, y, x)
        winnoteinfo.border()
        winnoteinfo.addstr(0, 1, " {0} ".format(title))
        # Display content
        winnoteinfo.refresh()

    #--- Helpers -------------------------------------------------------------#

    def __out_of_bounds(self) -> bool:
        """Check the size of the screen."""
        return self.height < t.min_height or self.width < t.min_width

    def __end_loop(self)-> None:
        self.__loop = False
