.PHONY: help demo api serve test validate pages clean

help:
	@printf '%s\n' \
		'Proof Gradient developer commands:' \
		'  make demo      Run the local customer-response proof demo' \
		'  make api       Start the FastAPI app on 127.0.0.1:8000' \
		'  make test      Run the Python test suite with pytest' \
		'  make validate  Run public-safe GoalOS documentation/site validators' \
		'  make pages     Build the generated GitHub Pages site' \
		'  make clean     Remove local build, cache, and SQLite artifacts'

demo:
	python -m proof_gradient demo --json

api:
	python -m proof_gradient api --host 127.0.0.1 --port 8000

serve: api

test:
	pytest

validate:
	python scripts/check_no_paid_artifacts.py
	python scripts/validate_goalos_catalog.py
	python scripts/validate_docs_tables_figures.py
	python scripts/validate_goalos_public_site.py

pages:
	python scripts/build_pages.py

clean:
	rm -rf .pytest_cache .ruff_cache dist build *.egg-info proof_gradient.db
