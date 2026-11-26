.PHONY: all validate readme links stars
all: validate readme
validate: ; python scripts/validate.py
readme: ; python scripts/build_readme.py
links: ; python scripts/check_links.py --md README.md docs/*.md CONTRIBUTING.md
stars: ; python scripts/fetch_stars.py && python scripts/build_readme.py
