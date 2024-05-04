import requests

def setup(value):
    url = 'https://hackathon.kvanttori.fi/buildings/create'
    data = {'team_name': value}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        #print("Request was successful.")
        print(response.text)
        id = response.json()['id']
        team_name = response.json()['team_name']
        print(f"Happy new building of team '{team_name}' day, your building ID is: {id}.")
        print(f"Good news, your building is sustainable!")

        return id

    else:
        print(f"Request failed with status code {response.status_code}.")