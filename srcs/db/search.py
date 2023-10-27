# Turn/IP
# Claire-lex - 2023
# Search functions
# pylint: disable=invalid-name

"""Functions to search things in other things."""

from re import sub
# Internal
from config import LEVENSHTEIN_THRESHOLD

# Credits:
# https://machinelearningknowledge.ai/ways-to-calculate-levenshtein-distance-edit-distance-in-python/
def levenshtein(s: str, t: str) -> int:
    """Levenshtein distance-based textual search.

    Returns the distance between strings s and t.
    """
    m = len(s)
    n = len(t)
    d = [[0] * (n + 1) for i in range(m + 1)]

    for i in range(1, m + 1):
        d[i][0] = i
    for j in range(1, n + 1):
        d[0][j] = j
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                cost = 0
            else:
                cost = 1
            d[i][j] = min(d[i - 1][j] + 1,        # deletion
                          d[i][j - 1] + 1,        # insertion
                          d[i - 1][j - 1] + cost) # substitution
    return d[m][n]

def format_for_search(value: str) -> str:
    """Standardize input to make case and character independent match."""
    if isinstance(value, str):
        return sub('[^0-9a-zA-Z]+', '', value.lower().strip())
    return value

def search(needle: str, haystack: object, threshold: int = LEVENSHTEIN_THRESHOLD) -> list:
    """Search for needle in haystack (a list or a string).

    The function uses the Levenshtein distance and may return several results.
    """
    results = []
    needle = format_for_search(needle)
    if isinstance(haystack, str):
        haystack = format_for_search(haystack)
        if levenshtein(needle, haystack) <= threshold:
            results.append(needle)
    elif isinstance(haystack, (list, tuple)):
        for entry in haystack:
            entry = format_for_search(entry)
            if levenshtein(needle, entry) <= threshold:
                results.append(entry)
    return results

def exact_search(needle: str, haystack: object) -> list:
    """Search for exact case-insensitive match."""
    needle = needle.lower()
    if isinstance(haystack, str):
        haystack = haystack.lower()
    elif isinstance(haystack, (list, tuple)):
        haystack = [x.lower() for x in haystack]
    return search(needle, haystack, 0)

def has_common_items(list1: str, list2: str) -> bool:
    """Returns true if at least one item for list1 is also in list2."""
    if not list1 or not list2:
        return False
    for item in list1:
        if exact_search(item, list2):
            return True
    return False
