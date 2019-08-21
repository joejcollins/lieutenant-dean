# Unit Testing Celery Tasks

## WSL Ubuntu 18.04

WSL ends up trying to use the windows version of Python so you have to specify the executable directly

`pipenv install --python=/usr/bin/python3.6`

1. install redis
1. pipenv install
1. pipenv shell
    1. python test-harness.py
    1. python test-unittest.py
    1. pytest test-pytest.py
    1. celery -A tasks worker -l info
    1. flower -A tasks --port=5555
    1. python run.py


