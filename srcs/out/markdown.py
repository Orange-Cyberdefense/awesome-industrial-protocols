# Turn/IP
# Claire-lex - 2023
# Markdown text generator

"""Markdown text generator."""

from os.path import join, exists
from re import sub
# Internal
from config import markdown as m, LIST_TITLE, LIST_DESCRIPTION, LIST_LOGO
from db import Protocols, Protocol

#-----------------------------------------------------------------------------#
# Constants                                                                   #
#-----------------------------------------------------------------------------#

ERR_NOTEMFILE = "Template file '{0}' does not exist."

H1 = lambda x: "# {0}".format(x)
H2 = lambda x: "## {0}".format(x)
H3 = lambda x: "### {0}".format(x)

LINK_FORMAT = lambda x: sub('[^0-9a-zA-Z]+', '', x.lower().strip())

LINK = lambda x: "[{0}](#{1})".format(x, LINK_FORMAT(x))
IMG = lambda x, y: "![{0}]({1})".format(x, y)


#-----------------------------------------------------------------------------#
# Markdown class                                                              #
#-----------------------------------------------------------------------------#

class MDException(Exception):
    pass

class Markdown(object):
    """Class to convert data to Markdown."""
    alist_template = None
    ppage_template = None
    protocols = None
    
    def __init__(self):
        self.alist_template = join(m.templates_path, m.awesomelist_template)
        self.ppage_template = join(m.templates_path, m.protocolpage_template)
        # Check files
        for md in [self.alist_template, self.ppage_template]:
            if not exists(md):
                raise MDException(ERR_NOTEMFILE.format(md))

    #--- Public --------------------------------------------------------------#
    
    def awesome_list(self, protocols: Protocols, stdout=False) -> str:
        """Convert protocols to a nice awesome list in Markdown."""
        self.protocols = protocols.all_as_objects
        keywords = {
            m.f_title: self.__f_title,
            m.f_description: self.__f_description,
            m.f_logo: self.__f_logo,
            m.f_toc: self.__f_toc,
            m.f_content: self.__f_content
        }
        final = []
        for line in self.__read(self.alist_template):
            if line in keywords.keys():
                line = keywords[line]()
            final.append(line)
        print("\n".join(final))

    def protocol_pages(self, protocols: Protocols, stdout=False) -> str:
        """Convert all protocols to a set of protocol pages in Markdown."""
        all_path = []
        for protocol in protocols.all_as_objects:
            path = self.protocol_page(protocol, stdout)
            all_path.append(path)
        return all_path

    def protocol_page(self, protocol: Protocol, stdout=False) -> str:
        """Convert a protocol object to a nice protocol page in Markdown."""
        raise NotImplementedError("protocol_page")
    
    #--- Private -------------------------------------------------------------#

    def __read(self, template_file: str) -> str:
        with open(template_file, 'r') as fd:
            for line in fd:
                yield line.strip()

    def __f_title(self) -> str:
        return H1(LIST_TITLE)
                
    def __f_description(self) -> str:
        return LIST_DESCRIPTION

    def __f_logo(self) -> str:
        return IMG(LIST_TITLE, LIST_LOGO)

    def __f_toc(self) -> str:
        toc = [H2(m.t_toc)+"\n"]
        for protocol in self.protocols:
            toc.append("- "+LINK(protocol.name))
        return "\n".join(toc)

    def __f_content(self) -> str:
        content = []
        for protocol in self.protocols:
            current = [H2(protocol.name)]
            content.append("\n".join(current))
        return "\n".join(content)
