# lambda_function
from URL.Short_URL.Short_url import *
from URL.Check_URL.Check_url import *
from URL.Details_URL.Details_url import *

import json
import pymysql
import rds_config

def lambda_handler():
    # url = event['queryStringParameters']['url-short']
    url = "https://naver.com"

    short_url = Check_Short(url)
    check_url = Check_URL(url)
    details_url = Detail_URL(url)

    return short_url, check_url, details_url

print(lambda_handler())
