import requests, csv
from requests_oauthlib import OAuth1
from urlparse import parse_qs

vals = {}	#dict of vals to be returned
with open('auth.csv', 'rb') as f:
	f_iter = csv.DictReader(f)
	vals = f_iter.next()
	
with open('res_auth.csv', 'rb') as a:
	a_iter = csv.DictReader(a)
	res_vals = a_iter.next()

test_rest_query = "http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20fantasysports.leagues.standings%20where%20league_key%3D'322.l.26670'&diagnostics=true"
test_url = "http://fantasysports.yahooapis.com/fantasy/v2/leagues;league_keys=322.l.26670/standings"

data = {'q': "select * from fantasysports.leagues.scoreboard where league_key='322.l.26670' and week='12'",
		'format': 'json'}

oauth = OAuth1(vals['consumer_key'],
				client_secret=vals['consumer_secret'],
				resource_owner_key=res_vals['resource_owner_key'],
				resource_owner_secret=res_vals['resource_owner_secret'])

r = requests.get(url=test_url, params=data, auth=oauth)

print 'RESULTS BELOW'
print r
print r.content