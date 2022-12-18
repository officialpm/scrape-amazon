"""Defines various scraper functions."""
from types import ModuleType

from .util.scrape import scrape_reviews
from .util.urlFunctions import construst_reviews_URL


def get_reviews(domain: str, product_id: str) -> ModuleType:
    print(f"[INFO] Scraping Reviews of Amazon ProductID - {product_id}")
    """Scraper
    Args:
        product_id: Amazon Product ID.
    Returns:
        Scraped Dataframe
    """
    all_reviews_url = construst_reviews_URL(domain, product_id)
    return scrape_reviews(all_reviews_url, domain)
