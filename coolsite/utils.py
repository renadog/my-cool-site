import random

from flask import url_for

picture_names = ['rena', 'brock', 'momo']


def say_hello(name=''):
    if len(name) > 0:
        name = ', %s' % name
    return 'Bye%s!' % name


def build_image_path_for(name):
    name = name.lower()
    return url_for('static', filename='img/' + name + '.png')


def check_for_valid_path(name):
    if name is not None and name.lower() in picture_names:
        return True
    return False


def pick_random_name():
    return random.choice(picture_names)
