import csv
from requests_oauthlib import OAuth1Session

vals = {}	#dict of vals to be returned
with open('auth.csv', 'rb') as f:
	f_iter = csv.DictReader(f)
	vals = f_iter.next()

req_token_url = 'https://api.login.yahoo.com/oauth/v2/get_request_token'
callback = 'oob'

oauth_session = OAuth1Session(vals['consumer_key'], client_secret=vals['consumer_secret'], callback_uri=callback)
fetch_response = oauth_session.fetch_request_token(req_token_url)

print fetch_response

# http://requests-oauthlib.readthedocs.org/en/latest/oauth1_workflow.html