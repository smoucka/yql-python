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

weekly_scoreboard_url = "http://fantasysports.yahooapis.com/fantasy/v2/league/322.l.26670/scoreboard;week=1"

oauth = OAuth1(vals['consumer_key'],
				client_secret=vals['consumer_secret'],
				resource_owner_key=res_vals['resource_owner_key'],
				resource_owner_secret=res_vals['resource_owner_secret'])

r = requests.get(url=weekly_scoreboard_url, auth=oauth)

with open('result_test.txt', 'w') as w:
	w.write(r.content)

print 'RESULTS BELOW'
print r.content
