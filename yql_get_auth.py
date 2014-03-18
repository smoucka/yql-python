import requests, csv
from requests_oauthlib import OAuth1
from urlparse import parse_qs

vals = {}	#dict of vals to be returned
with open('auth.csv', 'rb') as f:
	f_iter = csv.DictReader(f)
	vals = f_iter.next()

req_token_url = 'https://api.login.yahoo.com/oauth/v2/get_request_token'
base_auth_url = 'https://api.login.yahoo.com/oauth/v2/request_auth'
access_token_url = 'https://api.login.yahoo.com/oauth/v2/get_token'
callback = 'oob'

oauth = OAuth1(vals['consumer_key'],
				client_secret=vals['consumer_secret'],
				callback_uri=callback)
r = requests.post(url=req_token_url, auth=oauth)

creds = parse_qs(r.content)

resource_owner_key = creds.get('oauth_token')[0]
resource_owner_secret = creds.get('oauth_token_secret')[0]

authorize_url = base_auth_url + '?oauth_token='
authorize_url = authorize_url + resource_owner_key
print 'Please go here and authorize,', authorize_url
verifier = raw_input('Please input the verifier, ')

oauth = OAuth1(vals['consumer_key'],
				client_secret=vals['consumer_secret'],
				resource_owner_key=resource_owner_key,
				resource_owner_secret=resource_owner_secret,
				verifier=verifier)

r = requests.post(url=access_token_url, auth=oauth)
creds =  parse_qs(r.content)
resource_owner_key = creds.get('oauth_token')[0]
resource_owner_secret = creds.get('oauth_token_secret')[0]

with open('res_auth.csv', 'wb') as a:
	writer = csv.writer(a, delimiter=',')
	writer.writerow(['resource_owner_key', 'resource_owner_secret'])
	writer.writerow([resource_owner_key, resource_owner_secret])
