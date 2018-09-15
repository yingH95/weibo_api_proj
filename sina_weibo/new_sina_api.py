from weibo import APIClient
import webbrowser

APP_KEY = '3307315251'
APP_SECRET = '0b08d0aa9557b57f9c8781299f82e774'
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'  
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)

#url=client.get_authorize_url() 
#webbrowser.open_new(url)  

#print 'input text after code: '
#code = raw_input()

#r = client.request_access_token(code)
#access_token = r.access_token
#expires_in = r.expires_in
access_token = '2.00xmlwlG4mJpbDe3ad46fd15odNhsD'
expires_in = 1694674233

print(access_token)
print(expires_in)

client.set_access_token(access_token, expires_in)
statuses = client.users__show(
	access_token='2.00xmlwlG4mJpbDe3ad46fd15odNhsD',uid=2254519653)

length = len(statuses)
print length


print 'id: '+statuses['idstr']
print 'Username: '+statuses['screen_name']
print 'Info: '+statuses['description']
print 'Location: '+statuses['location']
print 'Weibo: '+statuses['status']['text']
