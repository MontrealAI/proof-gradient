.PHONY: demo serve test pytest validate pages clean

demo:
	proof-gradient demo --tenant demo --json

serve:
	proof-gradient api --host 127.0.0.1 --port 8000

pytest:
	pytest

test:
	python -m unittest discover -s tests -v

validate:
	python scripts/check_no_paid_artifacts.py
	python scripts/validate_goalos_catalog.py
	python scripts/validate_docs_tables_figures.py
	python scripts/validate_goalos_public_site.py

pages:
	python scripts/build_pages.py
	python scripts/verify_pages.py dist

clean:
	rm -rf .pytest_cache .ruff_cache .skillos dist build *.egg-info
