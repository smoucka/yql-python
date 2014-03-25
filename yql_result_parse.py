from bs4 import BeautifulSoup
import json

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

with open('result_test.txt', 'rb') as f:
	xmldata = f.read()

soup = BeautifulSoup(xmldata)

# rename 'name' tags to not confuse .name method
for name_tag in soup.find_all('name'):
	name_tag.name = 'name_'

result_array = []
	
teams = soup.league.scoreboard.matchups.find_all('team')

for each in teams:
	team_dict = {}
	team_dict['name'] = each.name_.string
	
	for st in each.find_all('stat'):
		if category_lookup[st.stat_id.string] in ['FTs', 'FGs']:
			team_dict[category_lookup[st.stat_id.string]] = st.value.string
		else:
			team_dict[category_lookup[st.stat_id.string]] = float(st.value.string)
	
	result_array.append(team_dict)

json_output = json.dumps(result_array)
print json_output