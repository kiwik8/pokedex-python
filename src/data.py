import requests_cache
import json
import re

COLORS = {
    "steel": "#5E6F6F",
    "dark": "#354141",
    "ice": "#98E6F1",
    "ghost": "#D6DBE6",
	"fire": '#FDDFDF',
	"grass": '#DEFDE0',
	"electric": '#FCF7DE',
	"water": '#DEF3FD',
	"ground": '#f4e7da',
	"rock": '#d5d5d4',
	"fairy": '#fceaff',
	"poison": '#98d7a5',
	"bug": '#f8d5a3',
	"dragon": '#97b3e6',
	"psychic": '#eaeda1',
	"flying": '#F5F5F5',
	"fighting": '#E6E0D4',
	"normal": '#F5F5F5'
}




def get_pokemon(id: int, session: requests_cache.CachedSession) -> dict:
    req = session.get(f"https://pokeapi.co/api/v2/pokemon/{id}/")
    data = json.loads(req.content)
    name = data['name']
    if "-" in name:
        reg = re.search("\-(.*)", name).group(0)
        reg = len(reg)
        name = name[:-reg]
    type = data["types"][0]["type"]["name"]
    color = COLORS[type]
    picture = data["sprites"]["front_default"]
    element_style = f"background-color: {color}"
    formatted_id = str(id).zfill(3)
    data = {
        'name': name,
        'type': type,
        'element_style': element_style,
        'picture': picture,
        'formatted_id': formatted_id,
    }
    return data


def get_all_pokemons(limit: int):
    html = []
    session = requests_cache.CachedSession("cache")
    for i in range(1, limit+1):
        data = get_pokemon(i, session)
        html.append(data)
    return html