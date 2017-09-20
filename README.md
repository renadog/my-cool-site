# my-cool-site
[![Build Status](https://travis-ci.org/renadog/my-cool-site.svg?branch=develop)](https://travis-ci.org/renadog/my-cool-site) [![codecov](https://codecov.io/gh/renadog/my-cool-site/branch/develop/graph/badge.svg)](https://codecov.io/gh/renadog/my-cool-site)

This is a million dollars, i can feel it

## Getting Started
```
virtualenv -p python3 .venv
source .venv/bin/activate
pip3 install -r requirements.txt

python3 server.py
```

## Testing
```
py.test --ignore=regression_tests --cov=coolsite .
```

or if you have the `chromedriver` in your path

```
py.test --cov=coolsite .
```
