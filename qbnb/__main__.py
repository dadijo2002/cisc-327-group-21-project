from qbnb import app
from qbnb.models import *
from qbnb.controllers import *

"""
This file runs the server at a given port
"""

FLASK_PORT = 8081

if __name__ == "__main__":
    app.run(debug=True, port=FLASK_PORT)
