CWD = $(CURDIR)

PROJECT_NAME = lex
PROJECT_HOME =$(CWD)

PROJECT_CODE =$(PROJECT_HOME)/src

PROJECT_DOC =$(PROJECT_HOME)/docs
PROJECT_HTML =$(PROJECT_DOC)/build/html
PROJECT_STATIC =$(PROJECT_HTML)/_static	

PROJECT_TEST =$(PROJECT_HOME)/tests

NEW_PYTHONPATH=$(PROJECT_CODE):$(PYTHONPATH)


clean:
	@echo "Cleaning up *.pyc files"
	@find . -name "*.pyc" -delete


setup:
	@echo "Installing dependencies..."
	@pip install -r $(PROJECT_HOME)/requirements.txt
	@pip install -r $(PROJECT_HOME)/requirements_test.txt
	@echo "Adding git hooks..."
	@cp ./helpers/git-hooks/pre-commit ./.git/hooks/pre-commit
	@chmod ug+x ./.git/hooks/pre-commit


doc:
	@cd $(PROJECT_DOC); make html

pep8:
	@echo "Checking source-code PEP8 compliance"
	@-pep8 $(PROJECT_CODE) --ignore=E501,E126,E127,E128


pep8_tests:
	@echo "Checking tests code PEP8 compliance"
	@-pep8 $(PROJECT_TEST) --ignore=E501,E126,E127,E128


lint:
	@# C0103: Invalid name - disabled because it expects any variable outside a class or function to be a constant
	@# C0301: Line too long
	@# R0904: Too many public methods - disabled due to Tornado's classes
	@# W0621: Redefining name %r from outer scope (line %s) - due to main if __name__ == '__main__'
	@# W0142: Used * or ** magic

	@echo "Running pylint"
	@pylint $(PROJECT_CODE)/$(PROJECT_NAME) --disable=C0301 --disable=R0904 --disable=C0103 --disable=W0621 --disable=W0142


style: pep8 pep8_tests lint


unit: clean pep8 pep8_tests
	@echo "Running pep8 and unit tests..."
	@nosetests -s  --cover-branches --cover-erase --with-coverage --cover-inclusive --cover-package=$(PROJECT_NAME) --tests=$(PROJECT_TEST)/unit --with-xunit


integration: clean pep8 pep8_tests
	@echo "Running pep8 and integration tests..."
	@nosetests -s  --cover-branches --cover-erase --with-coverage --cover-inclusive --cover-package=$(PROJECT_NAME) --tests=$(PROJECT_TEST)/integration --with-xunit

procfile:
	@echo "Checking if Procfile is valid"
	@honcho check
	@printf "\n"


tests: clean pep8 pep8_tests lint procfile
	@echo "Running unit and integration tests..."
	@nosetests -s  --cover-branches --cover-erase --with-coverage --cover-inclusive --cover-package=$(PROJECT_NAME) --tests=$(PROJECT_TEST) --with-xunit


run:
	@cd $(PROJECT_CODE); python $(PROJECT_NAME)/main.py --log_file_prefix=/tmp/logs/lex.log --log_to_stderr=true --template_path=$(PROJECT_HTML) --static_path=$(PROJECT_STATIC)


run_on_tsuru: # Called by Procfile
	@cd $(PROJECT_CODE); PYTHONPATH=. python $(PROJECT_NAME)/main.py --log_to_stderr=true --template_path=../docs/build/html --static_path=../docs/build/html/_static

deploy:

 