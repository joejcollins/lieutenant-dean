venv: .venv/touchfile

.venv/touchfile: requirements.txt
	export PIP_USER=false
	test -d .venv || virtualenv .venv
	. .venv/bin/activate; pip install --upgrade pip setuptools
	. .venv/bin/activate; pip install -Ur requirements.txt
	touch .venv/touchfile

test: venv
	. .venv/bin/activate; pytest

clean:
	rm -rf .venv
	find . -name "*.pyc" -exec rm -f {} \;
	find . -type f -name "*.py[co]" -delete -or -type d -name "__pycache__" -delete