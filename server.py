"""
My million dollar app.

Copyright 2017 Blake Grotewold <blake@fox.io>
"""

from flask import Flask
from coolsite import utils

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name='World'):
    return utils.say_hello(name)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)