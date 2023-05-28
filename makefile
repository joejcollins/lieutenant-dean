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
	find . -name "*.pyc" -exec rm -f {} \;
	find . -type f -name "*.py[co]" -delete -or -type d -name "__pycache__" -delete

compile:  # Compile the requirements files using pip-tools.
	.venv/bin/python -m pip install pip-tools
	.venv/bin/python -m piptools compile --output-file=requirements.txt
	echo "--editable ." >> requirements.txt

.PHONY: docs  # because there is a directory called docs.
docs:  # Build the mkdocs documentation.
	python -m mkdocs build --clean

flask:  # Run the Flask API server.
	.venv/bin/python -m gunicorn flask_api_v1.main:APP --config ./flask_api_v1/gunicorn_conf.py $(ARGS)

fastapi:  # Run the FastAPI server.
	.venv/bin/python -m hypercorn ./fastapi_api_v2/main:APP --config file:./fastapi_api_v2/hypercorn_conf.py $(ARGS)

.PHONY: help
help: # Show help for each of the makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

requirements:  # Install the requirements for Python, Ansible Galaxy and the logs.
	pyenv install --skip-existing 
	python -m venv .venv
	.venv/bin/python -m pip install --upgrade pip setuptools 
	.venv/bin/python -m pip install -r requirements.txt

test:  # Run the unit tests.
	.venv/bin/python -m pytest ./pytest_unit

test-tree:  # Build the directory structure for the tests.
	find . -type d -not -path "*/.*" \
	-not -path "*/__*" \
	-not -path "*/ansible_collections*" \
	-not -path "*/ansible_roles*" \
	-not -path "./base-images*" \
	-not -path "*.egg-info*" \
	-not -path "./docs*" \
	-not -path "./logs*" \
	-not -path "./pod*" \
	-not -path "./site*" \
	| xargs -I{} mkdir -p "./pytest_unit/{}"