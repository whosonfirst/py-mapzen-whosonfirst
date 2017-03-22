install:
	sudo pip install -r requirements.txt --process-dependency-links

refresh:
	git pull origin master
	sudo pip install --upgrade -r requirements.txt --process-dependency-links
