import requests, csv, json
from requests_oauthlib import OAuth1
from urlparse import parse_qs
from bs4 import BeautifulSoup

vals = {}	#dict of vals to be returned
with open('auth.csv', 'rb') as f:
	f_iter = csv.DictReader(f)
	vals = f_iter.next()
	
with open('res_auth.csv', 'rb') as a:
	a_iter = csv.DictReader(a)
	res_vals = a_iter.next()

weekly_scoreboard_url = "http://fantasysports.yahooapis.com/fantasy/v2/league/322.l.26670/scoreboard;week="
#weekly_scoreboard_url = "http://fantasysports.yahooapis.com/fantasy/v2/league/322.l.26670/settings"

oauth = OAuth1(vals['consumer_key'],
				client_secret=vals['consumer_secret'],
				resource_owner_key=res_vals['resource_owner_key'],
				resource_owner_secret=res_vals['resource_owner_secret'])

category_lookup = {'9004003': 'FGs',
	'5': 'FGP',
	'9007006': 'FTs',
	'8': 'FTP',
	'10': '3pt',
	'12': 'Pts',
	'15': 'Rbs',
	'16': 'Ast',
	'17': 'Stl',
	'18': 'Blk',
	'19': 'TOs'}				

result_array = []
	
for week in range(1,5):
	r = requests.get(url=weekly_scoreboard_url+str(week), auth=oauth)
	'''
	with open('result_test.txt', 'w') as w:
		w.write(r.content)

	print 'RESULTS BELOW'
	'''	
	soup = BeautifulSoup(r.content)

	# rename 'name' tags to not confuse .name method
	for name_tag in soup.find_all('name'):
		name_tag.name = 'name_'

	data_dict = {}
	data_dict['week'] = week
	data_dict['data'] = []
	
	teams = soup.league.scoreboard.matchups.find_all('team')

	for each in teams:
		team_dict = {}
		team_dict['name'] = each.name_.string
	
		for st in each.find_all('stat'):
			if category_lookup[st.stat_id.string] in ['FTs', 'FGs']:
				team_dict[category_lookup[st.stat_id.string]] = st.value.string
			else:
				team_dict[category_lookup[st.stat_id.string]] = float(st.value.string)
	
		data_dict['data'].append(team_dict)
	
	result_array.append(data_dict)

json_output = json.dumps(result_array)
print json_output
