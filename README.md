# scrape-amazon 🚀

[![Downloads](https://img.shields.io/badge/dynamic/json?color=success&label=Dowloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fv2%2Fprojects%2Fscape-amazon&style=for-the-badge)](https://github.com/officialpm/scrape-amazon)
![](https://img.shields.io/pypi/v/scrape-amazon?label=Version&style=for-the-badge)
![](https://img.shields.io/pypi/pyversions/scrape-amazon?style=for-the-badge)



## Installation

```shell
pip3 install scrape-amazon
```

## Example

### Import as module

```python
from scrape_amazon import get_reviews

reviews = get_reviews('in','B078BNQ318') #returns dataframe
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

## Output

```shell
        Reviewer       Rating       Title       Description
0     Parth Maniar       4      Great but ...     I change ... 
1     Manpreet Singh     3      Delivers  ...     Great ph ... 
2     Aparna Uniyal      1      Battery/H ...     I have   ... 
3     Rahul              5      Great but ...     On the f ... 
```