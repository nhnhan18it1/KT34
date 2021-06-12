from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://nhav:dnport@localhost:5432/kttest"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

@app.route("/", methods=['GET'])
def index():
    return "hello"


if __name__ == '__main__':
    app.run(port=5555, debug=True)
