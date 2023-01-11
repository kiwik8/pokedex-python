from flask import Flask
from flask import render_template
from src import data
from time import sleep



app = Flask(__name__, template_folder="src/templates", static_folder="src/static")

@app.route("/")
@app.route("/<int:limit>")
def main(limit=50):
    html = data.get_all_pokemons(limit)
    return render_template("index.html", items=html)





if __name__ == "__main__":
    app.run()