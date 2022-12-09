# Installs all dependencies and virtual environment for the project
install:
	poetry install
# a shortcut to start brain-games.py	
brain-games:
	poetry run brain-games
# a shortcut to start brain-even.py
brain-even:
	poetry run brain-even
# builds the source and wheels archives	
build:
	poetry build
# makes a dry-run of publish command	
publish:
	poetry publish --dry-run
# installs the package from dist directory	
package-install:
	python3 -m pip install --user dist/*.whl
# starts linting with flake8 on the whole project
lint:
	flake8 brain_games
