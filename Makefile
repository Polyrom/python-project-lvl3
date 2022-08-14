build:
	poetry build

lint:
	poetry run flake8 page_loader

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	poetry build
	python3 -m pip install --user --force-reinstall dist/hexlet_code-0.1.1-py3-none-any.whl	
