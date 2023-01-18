# Created: 2020-05-01 16:00:00
venv:
	pyenv install --skip-existing 
	python -m venv .venv
	. .venv/bin/activate; python -m pip install --upgrade pip setuptools 
	. .venv/bin/activate; python -m pip install -Ur requirements.txt

test:
	. .venv/bin/activate; pytest

clean:
	rm -rf .venv
	find . -name "*.pyc" -exec rm -f {} \;
	find . -type f -name "*.py[co]" -delete -or -type d -name "__pycache__" -delete