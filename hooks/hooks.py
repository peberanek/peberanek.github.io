from datetime import datetime


def on_config(config):
    # How to add the year automatically in the copyright part
    # https://github.com/squidfunk/mkdocs-material/discussions/4969
    year: str = str(datetime.now().year)
    config.copyright = config.copyright.format(year=year)
