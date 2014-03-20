from bs4 import BeautifulSoup

category_lookup = {'9004003': 'FGs',
					'5': 'FG%',
					'9007006': 'FTs',
					'8': 'FT%',
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

teams = soup.league.scoreboard.matchups.find_all('team')

for each in teams:
	print each.name_.string
	for st in each.find_all('stat'):
		print category_lookup[st.stat_id.string]
		print st.value.string