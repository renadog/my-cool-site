from flask import render_template

from coolsite import app, utils

@app.route('/')
@app.route('/<name>')
def hello(name='World'):
    message = utils.say_hello(name)
    return render_template('index.html', msg=message)