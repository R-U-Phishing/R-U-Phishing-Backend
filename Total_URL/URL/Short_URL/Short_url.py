# Short_URL
import json
import re
import ssl
from urllib.request import urlopen
from .Patterns import *

def Check_Short(input_url):
    context = ssl._create_unverified_context()
    long_url = urlopen(input_url, context=context).geturl()
    match = re.search(short_url, input_url)
    
    if match :  # 단축 url 일때
        json_object = {
            "input_url": input_url,
            "long_url": long_url
        }
        json_string = json.loads(json.dumps(json_object, default=str))
        return json_string

    else :  # 단축 url이 아닐때
        if 'www.' in input_url :
            json_object = {
                "input_url": input_url,
                "long_url": long_url
            }
            json_string = json.loads(json.dumps(json_object, default=str))
            return json_string
        else :
            if 'https://' in input_url :
                long_url = input_url.replace('https://','https://www.')
                json_object = {
                    "input_url": input_url,
                    "long_url": long_url
                }
                json_string = json.loads(json.dumps(json_object, default=str))
                return json_string
        
            elif 'http://' in input_url :
                long_url = input_url.replace('http://','http://www.')
                json_object = {
                    "input_url": input_url,
                    "long_url": long_url
                }
                json_string = json.loads(json.dumps(json_object, default=str))
                return json_string
