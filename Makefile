test:
	pytest tests/

mypy:
	mypy --config-file mypy.ini

flake:
	flake8 --config tox.ini