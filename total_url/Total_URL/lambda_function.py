# lambda_function
from URL.Short_URL.Short_url import *
from URL.Check_URL.Check_url import *
from URL.Details_URL.Details_url import *

import json
import pymysql
import rds_config

rds_host  = "url-db.cdrxcthawoa3.ap-northeast-2.rds.amazonaws.com"
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name

try:
    conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name)
except pymysql.MySQLError as e:
    print("ERROR: Unexpected error: Could not connect to MySQL instance.")
    print(e)
    sys.exit

def lambda_handler(event, context):
    url = event['queryStringParameters']['url-checking']
    
    if 'http' not in url:
        url = 'http://' + url

    with conn.cursor() as cur:
        cur.execute('SELECT input_url, title, long_url, ip_address, http_status_code, domain, subdomain, check_date, result, Registration FROM url_table WHERE input_url LIKE "%{0}%"'.format(url))
        result = cur.fetchall()
        if not result :
            check_url = Check_URL(url)
            details_url = Detail_URL(url)
            if details_url['http_status_code'] >= 400:
                json_object = {
                    "input_url": url,
                    "long_url": None
                }
                short_url = json.loads(json.dumps(json_object, default=str))
            else :
                short_url = Check_Short(url)
            
            print("try insert")
            try :
                cur.execute(
                'INSERT INTO url_table VALUES("{0}", "{1}", "{2}", "{3}", "{4}", "{5}", "{6}", "{7}", "{8}", "{9}", "{10}")'.format(
                    details_url['url'], short_url['input_url'], details_url['title'], short_url['long_url'], details_url['ip_address'], details_url['http_status_code'],details_url['domain'], details_url['subdomain'], check_url['check_date'], check_url['result'], details_url['Registration'])
                )
                conn.commit()
                print("Success insert details")

                cur.execute('SELECT * FROM rank_url WHERE url LIKE "{0}"'.format(details_url['url']))
                result1 = cur.fetchall()
                if not result1 :
                    cur.execute('INSERT INTO rank_url VALUES("{0}", 1)'.format(details_url['url']))
                    conn.commit()
                else :
                    cur.execute('update rank_url set count = 1 where url="{0}"'.format(details_url['url']))
                    conn.commit() 

                cur.execute('SELECT input_url, title, long_url, ip_address, http_status_code, domain, subdomain, check_date, result, Registration FROM url_table WHERE input_url LIKE "%{0}%"'.format(url))
                result = cur.fetchall()

                return json.loads(json.dumps(result, default=str))
            except pymysql.err.IntegrityError as e:
                print("duplicate url")
                cur.execute('SELECT input_url, title, long_url, ip_address, http_status_code, domain, subdomain, check_date, result, Registration FROM url_table WHERE input_url LIKE "%{0}%"'.format(details_url['url']))
                result = cur.fetchall()
                
                cur.execute('update rank_url set count = count + 1 where url="{0}"'.format(details_url['url']))
                conn.commit()
                return json.loads(json.dumps(result, default=str))
        else :
            details_url = Detail_URL(url)
            cur.execute('update rank_url set count = count + 1 where url="{0}"'.format(details_url['url']))
            conn.commit()
            return json.loads(json.dumps(result, default=str))
