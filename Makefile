####
#### 
####

help:
	@echo "Targets:"
	@echo "        build: build everything"
	@echo "   build-docs: Build documentations for release"
	@echo "    build-pkg: Build Python distribution package"
	@echo "   serve-docs: Serve documentations for devepment"
	@echo "  upload-test: Upload Python package to test.pypi.org"
	@echo ""
	@echo "          sum: Git status"
	@echo "           ci: Check in codes"
	@echo "        clean: Remove built files"


serve-docs:
	cd docs; mkdocs serve -a localhost:12001

build-docs:
	cd docs; mkdocs build -d ../src/lsutil/static/docs

build-pkg:
	@echo "// Updating build date in __init__.py"
	@grep -v ^__built__ src/lsutil/__init__.py > src/lsutil/.tmp/__init__.py
	@date +'__built__ = "%c %Z"' >> src/lsutil/.tmp/__init__.py
	@cp src/lsutil/.tmp/__init__.py src/lsutil/__init__.py
	@python3 -m build

build: build-docs build-pkg

sum:
	git status

upload-test:
	python3 -m twine upload --verbose --repository testpypi dist/*
upload-pypi:
	python3 -m twine upload --verbose dist/*

all: clean build upload-test

ci:
	git pull; git commit -a -mupdate; git push

clean:
	rm -rf ./dist

