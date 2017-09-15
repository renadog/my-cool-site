"""
My million dollar app.

Copyright 2017 Blake Grotewold <blake@fox.io>
"""
import os

from coolsite import app

import coolsite.controller


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
