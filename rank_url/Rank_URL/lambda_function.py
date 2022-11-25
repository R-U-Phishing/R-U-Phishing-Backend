import json
import pymysql
import rds_config

def lambda_handler(event, context):
    # TODO implement
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
    
    with conn.cursor() as cur:
        cur.execute('select * from rank_url order by count desc')
        result = cur.fetchall()
    
    return json.loads(json.dumps(result, default=str))
