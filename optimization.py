import requests
import setup

base_url = 'https://hackathon.kvanttori.fi'


def get_consumption(id):
    url = f'{base_url}/buildings/{id}/measurements'
    response = requests.get(url).json()
    return response['consumer']['consumption'][-1]['value']


def get_production(id):
    url = f'{base_url}/buildings/{id}/measurements'
    response = requests.get(url).json()
    sum_of_production = response['producer']['to_consumption'][-1]['value'] + response['producer']['to_grid'][-1][
        'value'] + response['producer']['to_storage'][-1]['value']
    return sum_of_production


# print(get_consumption())
# print(get_production())

def calculate_proportion_of_production_needed_for_consumption(id):
    consumption = get_consumption(id)
    print(f"needed consumption: {consumption}")
    production = get_production(id)
    print(f"supplyable production: {production}")
    delta = consumption - production
    print(f"Extra supply needed: {delta}")
    if production != 0:
        proportion = round(consumption / production, 2)
    else:
        proportion = 0.0

    return proportion, delta, consumption, production


# print(calculate_propotion_of_production_needed_for_consumption())


def set_production_allocations(consumption, grid, storage, id):
    url = f'https://hackathon.kvanttori.fi/buildings/{id}/allocations/production_allocation'
    data = {"to_consumption": consumption,
            "to_grid": grid,
            "to_storage": storage}

    response = requests.post(url, json=data)

    if response.status_code == 200:
        # print("Request was successful.")
        print(f"production allocations were adjusted to: consumption {consumption}, grid: {grid}, storage: {storage}")
        return data
    else:
        print(f"Request failed with status code {response.status_code}.")


def get_storage_charge(id):
    url = f'https://hackathon.kvanttori.fi/buildings/{id}/measurements/storage'
    response = requests.get(url).json()
    return response['charge'][-1]['value']


def set_storage_allocations(cons, grid, id):
    url = f'https://hackathon.kvanttori.fi/buildings/{id}/allocations/storage_allocation'
    data = {"to_consumption": cons,
            "to_grid": grid}

    response = requests.post(url, json=data)

    if response.status_code == 200:
        # print("Request was successful.")
        print(f"storage allocations:{data}")
    else:
        print(f"Request failed with status code {response.status_code}.")


total_kwH_covered = 0


def adjust_energy_allocations(id):
    global total_kwH_covered
    proportion, delta, consumption, production = calculate_proportion_of_production_needed_for_consumption(id)
    storage_charge = get_storage_charge(id)
    print(f"Proportion of consumption/production: {proportion}")
    print(f"Storage charge: {storage_charge}")

    if proportion <= 1:
        # consumption is lower than production
        # no need to feed from storage, so set it to 0,0
        total_kwH_covered += (consumption * proportion)

        set_storage_allocations(0, 0,id)
        if storage_charge < 250:
            # there is space in storage
            # use all production needed for consumption and send the rest to the storage
            set_production_allocations(proportion, 0, 1 - proportion, id)
        elif storage_charge == 250:
            # storage is full
            # use all production for consumption and send rest to grid because storage is full
            set_production_allocations(proportion, 1 - proportion, 0, id)
    else:
        total_kwH_covered += production
        # production is lower than consumption
        # use all of production for consumption
        set_production_allocations(1, 0, 0, id)
        # if there is storage feed all of the storage to the consumption
        if storage_charge != 0:
            set_storage_allocations(1, 0, id)
            # if there is more storage charge than delta between production and consumption add delta to total_kwH_covered
            if storage_charge > delta:
                total_kwH_covered += delta
            else:
                # if there is less or equal storage_charge to delta, then add storage charge amount to total_kwH_covered
                total_kwH_covered += storage_charge
        else:
            set_storage_allocations(0, 0, id)
