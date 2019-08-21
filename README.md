# Testing Celery Tasks

Approach is to run tasks immediately, rather than have an instance of Celery available to run the tasks.
This allows the tasks to be debugged during testing.

Suggested by <https://www.distributedpython.com/2018/05/01/unit-testing-celery-tasks/>.

## WSL Ubuntu 18.04

Install Redis and Flower.

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install redis-server
redis-cli -v
    redis-cli 4.0.9
sudo service redis-server restart
```

WSL ends up trying to use the windows version of Python so you have to specify the executable directly

`pipenv install --python=/usr/bin/python3.6`


Then you can open the `pipenv shell`.

```bash
python test-harness.py
python test-unittest.py
pytest test-pytest.py
```

Or run with actual `celery` in two WSL Windows `celery -A tasks worker -l info` and `python run.py`


