from flask import Flask
from flask import render_template
from src.data import get_pokemon
from time import sleep


app = Flask(__name__, template_folder="src/templates", static_folder="src/static")

@app.route("/")
@app.route("/<int:limit>")
def main(limit=50):
    html = []
    for i in range(1, limit+1):
        data = get_pokemon(i)
        html.append(data)
    return render_template("index.html", items=html)


if __name__ == "__main__":
    app.run()