

import logging

logger = logging.getLogger(__name__)

class Lyric:

    """
    Base class for all lyrics classes.
    Parameters
    ----------
    query: string
        lyric search query
    Attributes
    ----------
    sitename: str
        name of the site
    title: str
        Title of the lyric
    meta: dict
        metadata about the lyric. [Can be empty]
    """

    sitename = ''
    metadata = dict()

    def __init__(self):
        pass

    @classmethod
    def search(cls, query):
        """
        Search searches for the lyrics using the query given.
        Parameters
        ----------
        query: str
            query is the query keyword to be searched.
        Returns
        -------
        list
            List of :py:class:`~anime_downloader.sites.anime.SearchResult`
        """
        return
