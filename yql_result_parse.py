from bs4 import BeautifulSoup

with open('result_test.txt', 'rb') as f:
	xmldata = f.read()

soup = BeautifulSoup(xmldata)

for name_tag in soup.find_all('name'):
	name_tag.name = 'name_'
	print name_tag

#matchups = soup.league.scoreboard.matchups.find_all('team')

#print matchups[0].name.string
#print matchups[0].team_key.string
'''
for each in matchups:
	print each.name.string, each.team_stats
	print '-------------------------------------------'
'''