from weibo import APIClient
import webbrowser

APP_KEY = '3307315251'
APP_SECRET = '0b08d0aa9557b57f9c8781299f82e774'
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'  
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)

url=client.get_authorize_url() 
webbrowser.open_new(url)  

print 'input text after code: '
#code = raw_input()

#r = client.request_access_token(code)
access_token = '2.00NYjZ9C4mJpbDbd81d65c3dMqpTvC'
expires_in = 1536865199

##print(access_token)
##print(expires_in)

client.set_access_token(access_token, expires_in)
statuses = client.users__show(screen_name='alpacatuotuo')

length = len(statuses)
print length

for i in range(0,length):
    print 'Username: '+statuses[i]['screen_name']
    print 'Info: '+statuses[i]['description']
    print 'Location: '+statuses[i]['location']
    print 'Weibo: '+statuses[i]['status']['text']
