import requests
import json

COLORS = {
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




def get_pokemon(id: int) -> dict:
    req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}/")
    data = json.loads(req.content)
    name = data['name']
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
