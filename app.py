from dotenv import load_dotenv

load_dotenv()

from flask import Flask, render_template, request, jsonify
from ice_breaker_final import (
    ice_break_with_2,
)  # if __name__ == "__main__" is necessary in ice_breaker_final.py so that we can test/run the ice_break_with_2 function and see the output, but also so that when we import ice_break_with_2 from ice_break_final into app.py, the function call under if __name__ == "__main__" is not executed in app.py

app = Flask(__name__)


@app.route("/")  # the home/index route
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    summary, profile_pic_url = ice_break_with_2(name=name)
    return jsonify(
        {
            "summary_and_facts": summary.to_dict(),  # summary.to_dict() turns our summary object into a dictionary object for jsonify to use
            "picture_url": profile_pic_url,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

# Issue when inputting a name and clicking "submit", the loading circle spins indefinitely (most likely because profile picture url is of a type that causes issues, cannot be opened/viewed)
