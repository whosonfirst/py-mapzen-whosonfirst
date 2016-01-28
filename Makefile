bump:
	if test -e VERSION; then cp VERSION VERSION.bak; fi
	scripts/bump-version.pt > VERSION

deps:
	scripts/build-mapzen-requires.py --strict --out MAPZEN.REQUIRES.json
