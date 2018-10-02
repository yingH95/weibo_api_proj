from weibo import APIClient
from pymongo import MongoClient
import requests
import webbrowser

# APP_KEY = '3307315251'
# APP_SECRET = '0b08d0aa9557b57f9c8781299f82e774'
# CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'  
# client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
ACCESS_TOKEN = '2.00xmlwlG4mJpbDe3ad46fd15odNhsD'
URL = 'https://api.weibo.com/2/comments/by_me.json'
#url=client.get_authorize_url() 
#webbrowser.open_new(url)  

#print 'input text after code: '
#code = raw_input()

#r = client.request_access_token(code)
#access_token = r.access_token
#expires_in = r.expires_in
def getPage(pageurl):
	params = {
            'access_token': ACCESS_TOKEN
        }

        try:
        	response = requests.get(pageurl, params=params)
        	if response.status_code == 200:
					return response.json()
    	except requests.ConnectionError as e:
        	print('Error', e.args)

def run():


    while True:
        # request statuses__public_timeline
        comments = getPage(URL)

        length = len(comments['comments'])
        
        for key, value in comments.items(): 
        	print key, value

        comments = comments['comments']
        Monclient = MongoClient('localhost', 27017)
        db = Monclient['Weibo']
        WeiboData = db['HadSelected']

        # for i in range(0, length):
        i = 0
        created_at = comments[i]['created_at']
        id = comments[i]['user']['id']
        province = comments[i]['user']['province']
        city = comments[i]['user']['city']
        followers_count = comments[i]['user']['followers_count']
        friends_count = comments[i]['user']['friends_count']
        statuses_count = comments[i]['user']['statuses_count']
        url = comments[i]['user']['url']
        nickname = comments[i]['user']['screen_name']
        desc = comments[i]['user']['description']
        location = comments[i]['user']['location']
        text = comments[i]['text']

        
        WeiboData.insert_one({
            'created_at': created_at,
            'id': id,
            'nickname': nickname,
            'text': text,
            'province': province,
            'location': location,
            'description': desc,
            'city': city,
            'followers_count': followers_count,
            'friends_count': friends_count,
            'statuses_count': statuses_count,
            'url': url
            })

if __name__ == "__main__":
    run()