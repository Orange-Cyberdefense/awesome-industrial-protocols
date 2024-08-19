# Turn/IP
# Claire-lex - 2023
# Interface to fetch CVE (Common Vulnerabilities and Exposures)
# pylint: disable=invalid-name,too-few-public-methods,no-self-use

"""Fetch CVE related to a protocol."""

# Internal
from config import cvelist as c, FETCH_MAXYEAR
from db import Protocol, search
from . import FetchException, get_api_json

#-----------------------------------------------------------------------------#
# Constants                                                                   #
#-----------------------------------------------------------------------------#

ERR_BADRET = "Invalid format for result."

#-----------------------------------------------------------------------------#
# CVE fetch classes                                                          #
#-----------------------------------------------------------------------------#

class CVE():
    """Object representing data about a CVE."""
    raw = None

    def __init__(self, raw: dict):
        self.raw = raw
        self.id = raw["id"]
        self.description = ""
        self.year = int(raw["published"][:4])
        for descr in raw["descriptions"]:
            if descr["lang"] == "en":
                self.description = descr["value"].strip()
        self.url = c.nvd_detail + self.id

    def __str__(self):
        return "{0}: {1}".format(self.id, self.url)

class CVEList():
    """Interface to CVE Lit APIs."""

    def __init__(self):
        pass

    def fetch_by_keywords(self, protocol: Protocol) -> list:
        """Fetch CVE based on keywords."""
        results = []
        for name in protocol.names:
            search_url = c.api_keywords_search.format(name)
            cvelist = get_api_json(search_url)
            if not "vulnerabilities" in cvelist.keys():
                raise FetchException(ERR_BADRET)
            if not cvelist["vulnerabilities"]:
                continue
            for cve in cvelist["vulnerabilities"]:
                # If the CVE is too old we skip it
                if int(cve["cve"]["published"][:4]) < FETCH_MAXYEAR:
                    continue
                cve = CVE(cve["cve"])
                # We check that we don't have it already and that the keyword we
                # are looking for is in description to avoid false positives.
                if cve.id not in [x.id for x in results] and \
                   search(name, cve.description.split(" "), threshold=1):
                    results.append(cve)
        return sorted(results, key=lambda x: x.year, reverse=True)
