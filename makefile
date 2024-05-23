# Consistent set of make tasks.
.DEFAULT_GOAL:= help  # because it's is a safe task.

celery-beat:  # Run the Celery beat scheduler.
	CELERY_CONFIG=beat .venv/bin/python -m celery --workdir=celery_redis --app=main beat

celery-flower:  # Run the Celery flower web-based tool for monitoring and administration.
	.venv/bin/python -m celery --workdir=celery_redis --app=main flower --conf=flower_config.py $(ARGS)

celery-worker-high:  # Run a Celery worker with a high concurrency.
	.venv/bin/python -m celery --workdir celery_redis --app main worker --config=worker_high_config.py  $(ARGS)

celery-worker-low:  # Run a Celery worker with a low concurrency.
	.venv/bin/python -m celery --workdir celery_redis --app main worker --config=worker_low_config.py $(ARGS)

clean:  # Remove all build, test, coverage and Python artifacts.
	rm -rf .venv
	rm -rf *.egg-info
	find . -name "*.pyc" -exec rm -f {} \;
	find . -type f -name "*.py[co]" -delete -or -type d -name "__pycache__" -delete

PIPTOOLS_COMPILE = .venv/bin/python -m piptools compile

compile:  # Compile the requirements files using pip-tools.
	rm -f requirements.*
	$(PIPTOOLS_COMPILE) --output-file=requirements.txt
	echo "# Add the entire project as a package." >> requirements.txt
	echo "-e ." >> requirements.txt
	$(PIPTOOLS_COMPILE) --allow-unsafe --extra=dev --output-file=requirements.dev.txt
	echo "# Add the entire project as a package." >> requirements.dev.txt
	echo "-e ." >> requirements.dev.txt

.PHONY: docs  # because there is a directory called docs.
docs:  # Build the mkdocs documentation.
	python -m mkdocs build --clean

flask:  # Run the Flask API server.
	.venv/bin/python -m gunicorn flask_app.main:APP --config ./flask_app/gunicorn_conf.py $(ARGS)

fastapi:  # Run the FastAPI server.
	.venv/bin/python -m hypercorn ./fastapi_app_v2/main:APP --config file:./fastapi_app_v2/hypercorn_conf.py $(ARGS)

.PHONY: help
help: # Show help for each of the makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

kill: # Kill the servers on ports 8090 to 8093 if they are still running.
	lsof -i tcp:8090-8093 | awk 'NR!=1 {print $$2}' | xargs kill 2>/dev/null || true

lint:  # Lint the code with ruff, yamllint and ansible-lint.
	# `ansible-lint` ignores the `ansible.cfg` so the `ANSIBLE_LIBRARY` and `ANSIBLE_ROLES_PATH` have to be set as environment variables.
	.venv/bin/python -m ruff .
	.venv/bin/python -m yamllint -c .yamllint.yml .

report:  # Report the python version and pip list.
	.venv/bin/python --version
	.venv/bin/python -m pip list -v

test:  # Run the unit tests.
	.venv/bin/python -m pytest ./tests

venv:  # Install the requirements for Python.
	python -m venv .venv
	.venv/bin/python -m pip install --upgrade pip setuptools
	.venv/bin/python -m pip install -r requirements.txt

venv-dev:  # Install the development requirements for Python.
	python -m venv .venv
	.venv/bin/python -m pip install --upgrade pip setuptools
	.venv/bin/python -m pip install -r requirements.dev.txt