dev:
	sphinx-autobuild docs docs/_build/html

html:
	cd docs && make html

clean:
	rm -r docs/_build
