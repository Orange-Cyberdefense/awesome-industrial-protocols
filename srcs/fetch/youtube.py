# Turn/IP
# Claire-lex - 2023
# Interface to fetch protocols-related videos on Youtube
# pylint: disable=invalid-name,import-error,too-few-public-methods

"""Fetch protocols-related videos on Youtube."""

from importlib.util import find_spec
try:
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
except ModuleNotFoundError as mnfe:
    pass
# Internal
from config import GOOGLE_API_KEY, youtube as y
from db import Protocol
from . import FetchException

#-----------------------------------------------------------------------------#
# Constants                                                                   #
#-----------------------------------------------------------------------------#

ERR_GAPI = "Youtube API not found (pip install google-api-python-client)"
ERR_YTAPI = "Invalid Youtube API object."
ERR_BADRET = "Invalid format for result."

#-----------------------------------------------------------------------------#
# Youtube classes                                                             #
#-----------------------------------------------------------------------------#

class Video(object):
    """Object representing a Youtube video."""
    raw = None
    title = None
    description = None
    year = None
    url = None
    channelId = None
    channel = None

    def __init__(self, raw: dict, youtube_api: object = None):
        self.raw = raw
        try:
            self.title = raw["snippet"]["title"]
            if youtube_api: # We can request the complete description.
                self.description = self.__get_description(youtube_api)
            else: # Truncated version
                self.description = raw["snippet"]["description"]
            self.year = raw["snippet"]["publishedAt"][:4] # Only keep the year
            self.url = y.watch_url + raw["id"]["videoId"]
            self.channelId = raw["snippet"]["channelId"]
            self.channel = y.selected_channels[self.channelId]
        except KeyError:
            raise FetchException(ERR_BADRET)

    def __str__(self):
        return "{0} @ {1} ({2})".format(
            self.title, self.channel, self.year)

    def __get_description(self, youtube_api: object) -> str:
        """Make another request to retrieve the complete description.
        If we don't do that the description we have is truncated.
        """
        if not youtube_api:
            raise FetchException(ERR_YTAPI)
        description = youtube_api.videos().list(
            id=self.raw["id"]["videoId"], part="snippet"
        ).execute()
        return description["items"][0]["snippet"]["description"]

class Youtube(object):
    """Interface to Google API to retrieve Youtube videos."""
    youtube_api = None

    def __init__(self):
        # It will raise an exception (not caught this time) if not installed.
        if not find_spec('googleapiclient'):
            raise FetchException(ERR_GAPI)
        self.youtube_api = build(y.api_service_name, y.api_version,
                                 developerKey=GOOGLE_API_KEY)

    def get_videos(self, protocol: Protocol) -> list:
        """Fetch videos about a protocol from selected Youtube channels.

        The list of channels can be modified from config.py.
        """
        candidates = []
        found_titles = []
        try:
            for channel in y.selected_channels:
                for name in protocol.names:
                    response = self.youtube_api.search().list(
                        q=name,
                        channelId=channel,
                        part="snippet"
                    ).execute()
                    for item in response["items"]:
                        if item["snippet"]["title"] not in found_titles:
                            try:
                                video = Video(item, self.youtube_api)
                            except FetchException:
                                pass # Video was invalid
                            else:
                                candidates.append(video)
                                found_titles.append(item["snippet"]["title"])
        except HttpError as he:
            raise FetchException(str(he)) from None
        return sorted(set(candidates), key=lambda x: x.year)
