def say_hello(name=''):
    if len(name) > 0:
        name = ', %s' % name
    return 'Hello%s!' % name
