# VonObenScraper

A scraper for the metadata (titel, info-text) for the project [Wien von oben](https://www.wien.gv.at/spezial/vonoben/)

## Instructions

Install dependencies with poetry:

```
poetry install
```

Scrape and save results in a JSON:

```
scrapy crawl vonobenspider -o vonoben.json
```
