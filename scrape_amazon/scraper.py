"""Defines various scraper functions."""
import sys

from .util.urlFunctions import construst_reviews_URL, get_URL
from .util.scrape import get_all_review_page_url, scrape_reviews
from types import ModuleType

def get_reviews(domain: str, product_id: str) -> ModuleType:
    print(f"[INFO] Scraping Reviews of Amazon ProductID - {product_id}")
    """Scraper
    Args:
        product_id: Amazon Product ID.
    Returns:
        Scraped Dataframe
    """
    all_reviews_url = construst_reviews_URL(domain,product_id)
    return scrape_reviews(all_reviews_url)
    


