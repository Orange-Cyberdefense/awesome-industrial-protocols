# Turn/IP
# Claire-lex - 2023
# Interface to search for CVE (Common Vulnerabilities and Exposures)

"""Search for CVE related to a protocol."""

# Internal
from config import cvelist as c
from db import Protocol, find
from . import SearchException, get_api_json

#-----------------------------------------------------------------------------#
# Constants                                                                   #
#-----------------------------------------------------------------------------#

ERR_BADRET = "Invalid format for result."

#-----------------------------------------------------------------------------#
# CVE search classes                                                          #
#-----------------------------------------------------------------------------#

class CVE(object):
    """Object representing data about a CVE."""
    raw = None

    def __init__(self, raw:dict):
        self.raw = raw
        self.id = raw["id"]
        self.description = ""
        for descr in raw["descriptions"]:
            if descr["lang"] == "en":
                self.description = descr["value"].strip()
        self.url = c.nvd_detail + self.id
                
    def __str__(self):
        return "*** {0}: {1} ***\nDescription:\n{2}".format(self.id, self.url,
                                                            self.description)
                
class CVEList(object):
    """Interface to CVE Lit APIs."""

    def __init__(self):
        pass

    def search_by_keywords(self, protocol: Protocol) -> list:
        """Search CVE based on keywords."""
        results = []
        for name in protocol.names:
            search_url = c.api_keywords_search.format(name)
            cvelist = get_api_json(search_url)
            if not "vulnerabilities" in cvelist.keys():
                raise SearchException(ERR_BADRET)
            if not len(cvelist["vulnerabilities"]):
                continue
            for cve in cvelist["vulnerabilities"]:
                cve = CVE(cve["cve"])
                # We check that we don't have it already and that the keyword we
                # are looking for is in description to avoid false positives.
                if cve.id not in [x.id for x in results] and \
                   find(name, cve.description.split(" "), threshold=1):
                    results.append(cve)
        return sorted(results, key=lambda x: x.id)
