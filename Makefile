message = "travail du $$(date)"

push:
	git add .
	git commit -m $(message)
	git push

update:
	./update.sh

