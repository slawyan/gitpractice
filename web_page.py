from flask import flask
from new_feature_file import *

app = flask(__name__)

@app.route("/")
def index():
    return "Congratulation, it's a web app! Say hooray"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
    #calculate(10,20)