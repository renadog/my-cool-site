from flask import render_template

from coolsite import app, utils


@app.route('/')
@app.route('/<name>')
def hello(name='World'):
    message = utils.say_hello(name)
    return render_template('index.html', msg=message)


@app.route('/picture/')
@app.route('/picture/<name>')
def picture(name=None):
    is_valid = utils.check_for_valid_path(name)
    if name is None or not is_valid:
        name = utils.pick_random_name()
    path = utils.build_image_path_for(name)
    return render_template('picture.html',
                           image_path=path,
                           image_alt=name,
                           is_valid=is_valid)
