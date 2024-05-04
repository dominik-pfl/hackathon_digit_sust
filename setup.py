import requests

def setup(value):
    """
    Registers a new building for a given team by sending a POST request to a specified URL with the team name.
    If the request is successful, it prints and returns the building's unique ID and acknowledges the creation.
    If the request fails, it prints the failure status.

    Parameters:
        value (str): The name of the team for which a new building is being registered.

    Returns:
        int: The unique identifier for the new building if the request is successful. Otherwise, returns None.
    """
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