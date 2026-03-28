from remoteok import RemoteOkScraper
from src.joblens.pipeline.storage import save_posting

SCRAPERS = [RemoteOkScraper("https://remoteok.com/api")]


def run_all_scrapers():
    for scraper in SCRAPERS:
        name = scraper.__class__.__name__
        print(f"{name} starting")

        try:
            postings = scraper.scrape()
            count = save_posting(postings)
            print(f"{count} postings saved")

        except Exception as e:
            print(f"{name} failed: ", e)


if __name__ == "__main__":
    run_all_scrapers()
