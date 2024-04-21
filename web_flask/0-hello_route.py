#!/usr/bin/python3
""" starts a Flask web application"""

from flask  import Flask

app = Flask(__name__)

#Define a route for the  root URL '/'
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display "Hello HBNB! """
    return "Hello HBNB!"

if __name__ == "__main__":
    """start the Flask development server, Listen on
    default  network 0.0.0.0, and port  5000
    """
    app.run(host='0.0.0.0', port=5000)
