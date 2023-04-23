# Consistent set of make tasks.
.DEFAULT_GOAL:= help  # because it's is a safe task.

clean:  # Remove all build, test, coverage and Python artifacts.
	find . -name "*.pyc" -exec rm -f {} \;
	find . -type f -name "*.py[co]" -delete -or -type d -name "__pycache__" -delete

compile:  # Compile the requirements files using pip-tools.
	cd flask_api_v1; . .venv/bin/activate; python -m pip install pip-tools
	cd flask_api_v1; . .venv/bin/activate; python -m piptools compile --output-file=requirements.txt

.PHONY: docs  # because there is a directory called docs.
docs:  # Build the mkdocs documentation.
	python -m mkdocs build --clean

flask:  # Run the Flask API server.
	cd flask_api_v1; . .venv/bin/activate; python -m gunicorn main:APP --config gunicorn_conf.py $(ARGS)

fastapi:  # Run the FastAPI server.
	. ./fastapi_api_v2/.venv/bin/activate; python -m hypercorn ./fastapi_api_v2/main:APP --config file:./fastapi_api_v2/hypercorn_conf.py $(ARGS)

.PHONY: help
help: # Show help for each of the makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

requirements:  # Install the requirements for Python, Ansible Galaxy and the logs.
	cd flask_api_v1; pyenv install --skip-existing
	cd flask_api_v1; python -m venv .venv
	cd flask_api_v1; . .venv/bin/activate; python -m pip install --upgrade pip setuptools
	cd flask_api_v1; . .venv/bin/activate; python -m pip install -r requirements.txt

test:  # Run the unit tests.
	. .venv/bin/activate; pytest

venv:
	pyenv install --skip-existing 
	python -m venv .venv
	. .venv/bin/activate; python -m pip install --upgrade pip setuptools 
	. .venv/bin/activate; python -m pip install -Ur requirements.txt