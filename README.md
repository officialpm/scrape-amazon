# scrape-amazon-reviews 🚀

![](https://img.shields.io/pypi/v/scrape-amazon-reviews?label=Version&style=for-the-badge) 
![](https://img.shields.io/pypi/pyversions/scrape-amazon-reviews?style=for-the-badge)
![](https://img.shields.io/pypi/dm/scrape-amazon-reviews?style=for-the-badge)
![](https://img.shields.io/pypi/l/scrape-amazon-reviews?style=for-the-badge)

## Installation

```shell
pip3 install scrape-amazon-reviews
```

## Example
### Import as module

```python
from get_reviews import scrape-amazon-reviews

reviews = get_reviews('B078BNQ318') #returns dataframe

```

### CLI

```shell
scrape_amazon_review in B078BNQ318 B078BNQ318.csv
```
```shell
Positional Arguments:

domain       Amazon Domain (in/com)
product_id   product id for scraping (B078BNQ318)
output_path  output_path for saving (B078BNQ318.csv)
```