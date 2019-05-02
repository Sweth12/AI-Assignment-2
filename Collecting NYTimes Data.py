import sys, csv, json
import requests

class APIKeyException(Exception):
    def __init__(self, message): self.message = message 

class InvalidQueryException(Exception):
    def __init__(self, message): self.message = message 

class ArchiveAPI(object):
    def __init__(self, key=None):
        """
        Initializes the ArchiveAPI class. Raises an exception if no API key is given.
        :param key: New York Times API Key
        """
        self.key = key
        self.root = 'https://newsapi.org/v2/everything?' 
        if not self.key:
            nyt_dev_page = 'http://developer.nytimes.com/docs/reference/keys'
            exception_str = 'Warning: API Key required. Please visit {}'
            raise NoAPIKeyException(exception_str.format(nyt_dev_page))

    def query(self, year=None, month=None, key=None,):
        if not key: key = self.key
        if (year < 1882) or not (0 < month < 13):
            exception_str = 'Invalid query: See http://developer.nytimes.com/archive_api.json'
            raise InvalidQueryException(exception_str)
        url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=e0f0ba5521d14cac9db232682e5e202e')
        r = requests.get(url)
        return r.json()

# Replace below key with your key
api = ArchiveAPI('e0f0ba5521d14cac9db232682e5e202e')

years = [2016,2015,2014,2013,2012,2011,2010,2009,2008,2007]
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for year in years:
    for month in months:
        mydict = api.query(year, month)
        file_str = r'C:\Users\sweth\Desktop\lor\i20\booksnew\text books\cs664\spam 2\New folder' + str(year) + '-' + '{:02}'.format(month) + '.json'
        with open(file_str, 'w') as fout:
            json.dump(mydict, fout)
        fout.close()
        

    
