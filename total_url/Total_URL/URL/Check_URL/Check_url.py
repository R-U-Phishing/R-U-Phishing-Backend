# Check_URL
from .Feature import total_feature
import pickle
import datetime
import json

with open('URL/Check_URL/randomtree.pkl', 'rb') as f :
    load_model = pickle.load(f)

def Check_URL(url):
    feature = total_feature(url)
    pre = load_model.predict(feature)
    now = datetime.datetime.now()
    
    json_object = {
        "check_date": now.strftime('%Y-%m-%d'),
        "result": pre[0]
    }
    json_string = json.loads(json.dumps(json_object, default=str))
    return json_string
