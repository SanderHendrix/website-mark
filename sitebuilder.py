import sys

from flask import render_template, request
from website import app, views
from flask_frozen import Freezer

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer = Freezer(app)
        freezer.freeze()
    else:
        app.run(debug=True, host="192.168.178.14", port=8000)
