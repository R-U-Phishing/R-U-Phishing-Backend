# Short_URL
import json
import re
import ssl
from urllib.request import urlopen
from .Patterns import *

def Check_Short(url):
    context = ssl._create_unverified_context()
    long_url = urlopen(url, context=context).geturl()
    match = re.search(short_url, url)
    
    if match :
        return long_url
    else :
        if 'www.' in url :
            return url
        else :
            if 'https://' in url :
                url = url.replace('https://','https://www.')
                return url
        
            elif 'http://' in url :
                url = url.replace('http://','http://www.')
                return url