all: unittest test
	@echo "All done..."

unittest:
	pytest -v test_hvert.py

test:
	@cat 1.in | python hvert.py | diff - 1.ans
	@cat 2.in | python hvert.py | diff - 2.ans
	@cat hvert1.in | python hvert.py | diff - hvert1.ans
	@cat hvert2.in | python hvert.py | diff - hvert2.ans
	@echo "All Local Tests Passed..."

style-check:
	flake8 .

type-check:
	mypy --strict .

kattis:
	@kattis -f hvert.py -p hvert

style-fix:
	autopep8 --in-place --recursive --aggressive --aggressive .