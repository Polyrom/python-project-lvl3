build:
	poetry build

lint:
	poetry run flake8 page_loader

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	poetry build
	python3 -m pip install --user --force-reinstall dist/*.whl

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=page_loader

test-coverage-xml:
	poetry run pytest --cov=page_loader --cov-report xml
