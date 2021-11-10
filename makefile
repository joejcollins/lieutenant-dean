venv: .venv/touchfile

.venv/touchfile: requirements.txt
	export PIP_USER=false
	test -d .venv || virtualenv .venv
	. .venv/bin/activate; pip install --upgrade pip setuptools
	. .venv/bin/activate; pip install -Ur requirements.txt
	# Script to start flask
	@echo "#\!/bin/bash" > .venv/flask.sh
	@echo ". .venv/bin/activate" >> .venv/flask.sh
	@echo "export FLASK_APP=rest_api.flask_app" >> .venv/flask.sh
	@echo "export FLASK_ENV=development"  >> .venv/flask.sh
	@echo "flask run"  >> .venv/flask.sh
	chmod u+x .venv/flask.sh
	# Script to start celery
	@echo "#\!/bin/bash" > .venv/celery.sh
	@echo ". .venv/bin/activate" >> .venv/celery.sh
	@echo "watchmedo auto-restart --directory=./task_queue/ --pattern=*.py --recursive -- \\" >> .venv/celery.sh
	@echo "celery --workdir=task_queue --app=celery_app worker --hostname worker1@%n --loglevel=INFO --queues text_queue,number_queue" >> .venv/celery.sh
	chmod u+x .venv/celery.sh
	# Script to start flower
	@echo "#\!/bin/bash" > .venv/flower.sh
	@echo ". .venv/bin/activate" >> .venv/flower.sh
	@echo "celery --workdir=task_queue --app=celery_app flower" >> .venv/flower.sh
	chmod u+x .venv/flower.sh
	# Done now
	touch .venv/touchfile

test: venv
	. .venv/bin/activate; pytest

clean:
	rm -rf .venv
	find . -name "*.pyc" -exec rm -f {} \;
	find . -type f -name "*.py[co]" -delete -or -type d -name "__pycache__" -delete