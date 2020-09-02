# scrape-amazon 🚀

![](https://img.shields.io/pypi/v/scrape-amazon?label=Version&style=for-the-badge)
![](https://img.shields.io/pypi/pyversions/scrape-amazon?style=for-the-badge)
![](https://img.shields.io/pypi/dm/scrape-amazon?style=for-the-badge)
![](https://img.shields.io/pypi/l/scrape-amazon?style=for-the-badge)

## Installation

```shell
pip3 install scrape_amazon
```

## Example

### Import as module

```python
from get_reviews import scrape-amazon

reviews = get_reviews('B078BNQ318') #returns dataframe
#Reviewer, Rating, Title, Description
```

### CLI

```shell
scrape-amazon in B078BNQ318 B078BNQ318.csv
```

```shell
Positional Arguments:

domain       Amazon Domain (in/com)
product_id   product id for scraping (B078BNQ318)
output_path  output_path for saving (B078BNQ318.csv)
```
