import logging
import sys
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return ({"version": "1.0.0", "app": "preveil_test"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)