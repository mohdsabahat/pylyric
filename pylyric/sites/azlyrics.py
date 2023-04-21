from pylyric.sites.base import Lyric
from pylyric import utils


class AZLyrics(Lyric):

    sitename='AZLyrics'
    search_url = 'https://search.azlyrics.com/search.php?q={query}&w=lyrics&p={page}&x=266d470caa76da35b4c2d31349d089ccec9e1fa58f770c6c35261bae134ee8e6'

    @classmethod
    def search(cls, query):

        resp = utils.get(cls.search_url.format(
            query = query, page = 1))
        soup = utils.soupify(resp)
        table = soup.find('table')
        rows = table('tr')[1:-2]
        for row in rows:
            anchor = row.find('a')
            title  = anchor.find('b').text
            author = anchor('b')[1].text
            print(title,',' , author)
