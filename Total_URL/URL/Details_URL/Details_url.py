# Details_URL
import json
import re
import ssl
from urllib.request import urlopen
import requests
import socket
import whois
from bs4 import BeautifulSoup
from datetime import datetime as dt
from tld import get_tld

def Detail_URL(url):
    # # Replace url in 'www'
    # if 'www.' in input_url:
    #     url = input_url.replace('www.','')
    # else:
    #     url = input_url

    # Http_status_code & Title
    requests_url = requests.get(url, timeout=5)
    http_status_code = requests_url.status_code

    html = requests_url.text
    soup = BeautifulSoup (html, 'html.parser')
    title = soup.title.string.upper().split(' ')[0]

    # Subdomain, Domain                                              
    tld = get_tld(url, as_object=True)
    domain = tld.domain
    subdomain = tld.subdomain
    if not subdomain:
        subdomain = None

    # Ip_address                              
    if 'https://' in url:
        url = url.replace('https://', '')
        id_address = socket.gethostbyname(url)
    elif 'http://' in url:
        url = url.replace('http://', '')
        id_address = socket.gethostbyname(url)

    # Registration
    domain_info = whois.whois(url)
    init_date = domain_info["creation_date"]
    if isinstance(init_date, list):
        for init in init_date:
            Registration = init.date()
            date = Registration.strftime('%Y-%m-%d')
    else:
        Registration = init_date.date()
        date = Registration.strftime('%Y-%m-%d')

    json_object = {
        "url": url,
        "title": title,
        "id_address": id_address,
        "http_status_code": http_status_code,
        "domain": domain,
        "subdomain": subdomain,
        "Registration": date
    }

    json_string = json.loads(json.dumps(json_object, default=str))

    return json_string