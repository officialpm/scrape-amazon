<div align="center">

# scrape-amazon 🚀 

[![Downloads](https://img.shields.io/badge/dynamic/json?color=success&label=downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fv2%2Fprojects%2Fscrape-amazon&style=flat-square)](https://github.com/officialpm/scrape-amazon)
![](https://img.shields.io/pypi/v/scrape-amazon?label=version&style=flat-square&color=ffd05b)
![Versions](https://img.shields.io/pypi/pyversions/scrape-amazon?style=flat-square&color=f58b1b)
![Stars](https://img.shields.io/github/stars/officialpm/scrape-amazon?color=e6e87d)
![License](https://img.shields.io/github/license/officialpm/scrape-amazon)
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=officialpm.scrape-amazon)


</div>

## Installation

```shell
❯ pip install scrape-amazon
```

## Example

### Import as module

```python
from scrape_amazon import get_reviews

reviews = get_reviews('in','B078BNQ318') #returns dataframe
#Reviewer, Rating, Title, Description
```

### CLI

#### How to use
```shell
❯ scrape-amazon [domain] [product_id] [output_path].csv
```

#### Positional Arguments:
```shell
domain       Amazon Domain (in/com)
product_id   product id for scraping (B078BNQ318)
output_path  output_path for saving (B078BNQ318.csv)
```

#### Example
```shell
❯ scrape-amazon in B078BNQ318 B078BNQ318.csv
```

## Output

```shell
        Reviewer       Rating       Title       Description
0     Parth Maniar       4      Great but ...     I change ... 
1     Manpreet Singh     3      Delivers  ...     Great ph ... 
2     Aparna Uniyal      1      Battery/H ...     I have   ... 
3     Rahul              5      Great but ...     On the f ... 
```


[CODE_OF_CONDUCT.md](https://github.com/officialpm/scrape-amazon/blob/master/CODE_OF_CONDUCT.md)