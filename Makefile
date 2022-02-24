####

help:
	@echo "Targets:"
	@echo "        build: build everything"
	@echo "   build-docs: Build documentations for release"
	@echo "    build-pkg: Build Python distribution package"
	@echo "   serve-docs: Serve documentations for devepment"
	@echo "  upload-pypi: Upload Python package to pypi.org"
	@echo ""
	@echo "          sum: Git status"
	@echo "           ci: Check in codes"
	@echo "        clean: Remove built files"
	@echo ""
	@echo "  upload-test: Upload Python package to test.pypi.org"


serve-docs:
	cd docs; mkdocs serve -a localhost:12001

build-docs:
	cd docs; mkdocs build -d ../src/lsutil/static/docs

build-pkg:
	@echo "// Updating version and build date in __init__.py"
	@bin/dev/update_version.py src/lsutil/__init__.py
	@rm -rf dist/*
	@python3 -m build
	@ls -hl dist

build: build-docs build-pkg

sum:
	git status

upload-test:
	python3 -m twine upload --verbose --repository testpypi dist/*

upload-pypi:
	python3 -m twine check dist/*
	python3 -m twine upload --verbose dist/*

all: clean build upload-pypi

ci:
	git pull; git commit -a -mupdate; git push

clean:
	rm -rf ./dist
