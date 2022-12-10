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

# player_name = response['response'][1]['player'][0]['name']
# player_photo = response['response'][0]['players'][0]['photo']
# print(player_name, 'sofjhoshf')
# print('team name: ', team_name)
# print('team logo: ', team_logo)

print(type(response['response'][1]['players'][0]))
print(type(response['response'][1]['players'][0]['player']))
print(type(response['response'][1]['players'][0]['player']['name']))




# print(team_name, 'hi')
# for k, v in response.items():
# 	print(k, ' : ', v, '--------------------******************#################')


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