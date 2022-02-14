####
####

help:
	@echo "Targets:"
	@echo "           sum: Git status"
	@echo "            ci: Check in codes"
	@echo "         build: build everything"
	@echo "    build-docs: Build documentations"
	@echo "   deploy-docs: Deploy documentations to the web"
	@echo "         clean: Remove all built files"

serve-docs:
	cd docs; pipenv run mkdocs serve -a localhost:12002

build-docs:
	cd docs; mkdocs build -d ../src/sqlite3ftse/static/docs

deploy-docs:
	cd docs; pipenv run mkdocs gh-deploy --force


build: build-docs

sum:
	git status

ci:
	@echo "// Bring repo up-to-date and push changes to repo"
	git pull; git commit -a -mupdate; git push

blue:
	@bin/blueplates

