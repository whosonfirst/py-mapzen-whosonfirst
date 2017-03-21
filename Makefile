build: deps bump

bump:
	scripts/bump-version.py

deps:
	scripts/build-mapzen-requires.py --strict --out MAPZEN.REQUIRES.json

refresh:
	git pull origin master
	sudo pip install --upgrade -r requirements.txt --process-dependency-links
