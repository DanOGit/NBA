import requests

NBA_TEAMS_URL = 'http://data.nba.net/10s//prod/v2/2018/teams.json'

r = requests.get(NBA_TEAMS_URL)

# print(r.content)

fullData = r.json()
teams = fullData['league']['standard']


for item in teams:
    if item['isNBAFranchise']:
        print (item['fullName'])

print(teams)
