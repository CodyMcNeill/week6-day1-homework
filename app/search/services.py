import requests

def get_poke_info(pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    response = requests.get(url)
    if response.ok:
            data = response.json()
            poke_dict = {}
            poke_dict['name'] = data['name']
            poke_dict['ability'] = data['abilities'][0]['ability']['name']
            poke_dict['base_xp'] = data['base_experience']
            poke_dict['front_shiny'] = data['sprites']['front_shiny']
            poke_dict['base_atk'] = data['stats'][1]['base_stat']
            poke_dict['base_hp'] = data['stats'][0]['base_stat']
            poke_dict['base_def'] = data['stats'][2]['base_stat']
            # print(poke_dict)
            return poke_dict
    else:
        return f'Please input a valid search term'

