"""Defines various scraper functions."""
import sys

from .util.urlFunctions import construst_reviews_URL, get_URL
from .util.scrape import get_all_review_page_url, scrape_reviews
from types import ModuleType
import pandas as pd

import argparse


parser = argparse.ArgumentParser(description='Scrape Amazon Product Reviews')
parser.add_argument('domain', type=str,
                help='amazon domain')
parser.add_argument('product_id', type=str,
                help='product id for scraping')
parser.add_argument('output_path', type=str,
                help='output_path for saving')

def get_reviews_cli() -> ModuleType:

    args = parser.parse_args()
    print(f"[INFO] Scraping Reviews of Amazon ProductID - {args.product_id}")
    """Scraper
    Args:
        product_id: Amazon Product ID.
    Returns:
        Scraped Dataframe
    """
    all_reviews_url = construst_reviews_URL(args.domain,args.product_id)
    reviews = scrape_reviews(all_reviews_url)
    reviews.to_csv(args.output_path)