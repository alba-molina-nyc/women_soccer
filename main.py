import requests

url = "https://api-football-beta.p.rapidapi.com/fixtures/players"

querystring = {"fixture":"169080"}

headers = {
	"X-RapidAPI-Key": "33f1e04db2msh82bd5edcc89cedbp192013jsn519016419896",
	"X-RapidAPI-Host": "api-football-beta.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring).json()


team_name = response['response'][0]['team']['name']
team_logo = response['response'][0]['team']['logo']
player_name = response['response'][1]['players'][0]['player']['name']
player_photo = response['response'][1]['players'][0]['player']['photo']
player_position = response['response'][1]['players'][0]['statistics'][0]['games']['position']

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$ from here and above the code was working fine $$$$$$$$$$$$$$$$$$$$$$$$$$$$



# $$$$$$$$$$$$$$$$$$$$$$$$$$$$ was testing this and then I hit max API for the day $$$$$$$$$$$$$$$$$$$$$$$$$$$$

# response['response'][1]['players'][0]['statistics'][0]['games']['position']['shots']
# response['response'][1]['players'][0]['statistics'][0]['games']['position']['goals']
# response['response'][1]['players'][0]['statistics'][0]['games']['position']['passes']
# response['response'][1]['players'][0]['statistics'][0]['games']['position']['tackles']
# response['response'][1]['players'][0]['statistics'][0]['games']['position']['duels']
# response['response'][1]['players'][0]['statistics'][0]['games']['position']['dribbles']
# response['response'][1]['players'][0]['statistics'][0]['games']['position']['fouls']
# response['response'][1]['players'][0]['statistics'][0]['games']['position']['cards']
# response['response'][1]['players'][0]['statistics'][0]['games']['position']['penalty']
# response['response'][1]['players'][0]['statistics'][0]['games']['position']['offsides']

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$ was testing this and then I hit max API for the day $$$$$$$$$$$$$$$$$$$$$$$$$$$$


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$ JUNK AREA $$$$$$$$$$$$$$$$$$$$$$$$$$$$

# print(player_position)

# for k, v in dict1.items():
# 	print('$$$$$$$$$$$$$$$$$$$$', k, '::::::::::::::::::::', v, '$$$$$$$$$$$$$$$$$$$$')

# for k, v in response.items():
# 	print(k, ' : ', v, '--------------------******************#################')
# 	for k, v in response['response'].items():
# 		print('hi', k, v)



# print(response['response'][0], 'this is a dict')
# print(type(response['response'][0]))

# print(response['response'], 'hi')
# print(type(response['response']), 'this is a list')
# team = response['response']['team']['name']

# print(team)

# print(type(response))


# print(response)


# print('player name: ', player_name)
# print('player photo: ', player_photo)

# print(player_name, 'nameo')

# print(player_name, 'sofjhoshf')
# print('team name: ', team_name)
# print('team logo: ', team_logo)
# print('player photo: ', player_photo)

# print(type(response['response'][1]['players'][0]))
# print(type(response['response'][1]['players'][0]['player']))
# print(type(response['response'][1]['players'][0]['player']['name']))

# print(response['response'][1]['players'][0]['statistics'], 'statistics', type(response['response'][1]['players'][0]['statistics']), 'this is alist')
# print(response['response'][1]['players'][0]['statistics'][0],  type(response['response'][1]['players'][0]['statistics'][0]), 'this is a dict')
# print(player_position, type(response['response'][1]['players'][0]['statistics'][0]['games']), 'this is a dictionary')
# print(response['response'][1]['players'][0]['statistics'][0],  type(response['response'][1]['players'][0]['statistics'][0]), 'this is a dict')

# print(response['response'][1]['players'][0]['statistics'][0],  type(response['response'][1]['players'][0]['statistics'][0]), 'this is a dict')
# print(response['response'][1]['players'][0]['statistics'][0]['games']['position'],  type(response['response'][1]['players'][0]['statistics'][0]['games']['position']), 'this is a dict')

# https://www.api-football.com/documentation-beta#tag/Injuries

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$ JUNK AREA $$$$$$$$$$$$$$$$$$$$$$$$$$$$
