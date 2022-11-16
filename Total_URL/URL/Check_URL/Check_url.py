# Check_URL
from .Feature import total_feature
import pickle

with open('URL/Check_URL/randomtree.pkl', 'rb') as f :
    load_model = pickle.load(f)

def Check_URL(url):
    feature = total_feature(url)
    pre = load_model.predict(feature)
       
    return pre[0]