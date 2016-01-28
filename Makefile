build: deps bump

bump:
	scripts/bump-version.py

deps:
	scripts/build-mapzen-requires.py --strict --out MAPZEN.REQUIRES.json
