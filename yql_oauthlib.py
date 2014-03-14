import csv
from requests_oauthlib import OAuth1Session

vals = {}	#dict of vals to be returned
with open('auth.csv', 'rb') as f:
	f_iter = csv.DictReader(f)
	vals = f_iter.next()

req_token_url = 'https://api.login.yahoo.com/oauth/v2/get_request_token'
base_auth_url = 'https://api.login.yahoo.com/oauth/v2/request_auth'
callback = 'oob'

oauth_session = OAuth1Session(vals['consumer_key'], client_secret=vals['consumer_secret'], callback_uri=callback)
fetch_response = oauth_session.fetch_request_token(req_token_url)

res_owner_key = fetch_response.get('oauth_token')
res_owner_secret = fetch_response.get('oauth_token_secret')

auth_url = oauth_session.authorization_url(base_auth_url)
print 'Go here and authorize, ', auth_url

redirect_response = raw_input('Paste redirect URL here: ')
oauth_response = oauth_session.parse_authorization_response(redirect_response)

print oauth_response

# http://requests-oauthlib.readthedocs.org/en/latest/oauth1_workflow.html