"""Defines various scraper functions."""
import argparse
from types import ModuleType

from .util.scrape import scrape_reviews
from .util.urlFunctions import construst_reviews_URL

parser = argparse.ArgumentParser(description="Scrape Amazon Product Reviews")
parser.add_argument("domain", type=str, help="amazon domain")
parser.add_argument("product_id", type=str, help="product id for scraping")
parser.add_argument("output_path", type=str, help="output_path for saving")


def get_reviews_cli() -> ModuleType:

    args = parser.parse_args()
    print(f"[INFO] Scraping Reviews of Amazon ProductID - {args.product_id}")
    """Scraper
    Args:
        product_id: Amazon Product ID.
    Returns:
        Scraped Dataframe
    """
    all_reviews_url = construst_reviews_URL(args.domain, args.product_id)
    reviews = scrape_reviews(all_reviews_url, args.domain)
    reviews.to_csv(args.output_path)
