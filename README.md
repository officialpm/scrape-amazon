<div align="center">

# scrape-amazon 🚀 

[![Downloads](https://img.shields.io/badge/dynamic/json?color=success&label=downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fv2%2Fprojects%2Fscrape-amazon&style=flat-square)](https://github.com/officialpm/scrape-amazon)
![versions](https://img.shields.io/pypi/v/scrape-amazon?label=version&style=flat-square&color=ffd05b)
![pyVersions](https://img.shields.io/pypi/pyversions/scrape-amazon?style=flat-square&color=f58b1b)
![Stars](https://img.shields.io/github/stars/officialpm/scrape-amazon?color=e6e87d)
![Forks](https://img.shields.io/github/forks/officialpm/scrape-amazon?color=3efac5)
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

reviews = get_reviews('com','B085BCWJV6') #returns dataframe
#SrNo.,Reviewer,ReviewerURL,VerifiedPurchase,HelpfulCount,Rating,Title,Description,Date
```

### CLI

#### How to use
```shell
❯ scrape-amazon [domain] [product_id] [output_path].csv
```

#### Positional Arguments:
```shell
domain       Amazon Domain (in/com)
product_id   product id for scraping (B085BCWJV6)
output_path  output_path for saving (B085BCWJV6.csv)
```

#### Example
```shell
❯ scrape-amazon com B085BCWJV6 B085BCWJV6.csv
```

## Output

```shell
|SrNo.|Reviewer      |ReviewerURL                                                             |VerifiedPurchase|HelpfulCount|Rating|Title                    |Description        |Date      |
|:---:|:------------:|:----------------------------------------------------------------------:|:--------------:|:----------:|:----:|:-----------------------:|:-----------------:|:--------:|
|  0  |  Miss Brea   |https://amazon.com/gp/profile/amzn1.account.AFCGYZNNVKNA4VXFGYO5YTVUUTFA|      YES       |     0      |  5   |          Great          |   I used it ...   |12/10/2022|
|  1  |Basil Saunders|https://amazon.com/gp/profile/amzn1.account.AE3ZIBJKBIJE3V3ALSXENXCJI6TA|      YES       |     0      |  5   |     Lovely product      | It smooths my ... |12/13/2022|
|  2  |  Jessie E.   |https://amazon.com/gp/profile/amzn1.account.AETVQOAZ4NOVB23Y6ZXZEAQDQAUQ|      YES       |     5      |  5   |     So easy to ...      |  I make cold...   |10/02/2022|
|  3  |elizabeth todd|https://amazon.com/gp/profile/amzn1.account.AFGXB32V7ATUEWJJK2IOFU4MZGHQ|      YES       |     0      |  5   |  Amazing cocoa butter   |This Cocoa butter w|11/10/2022|
|  4  |    PRPro     |https://amazon.com/gp/profile/amzn1.account.AEKBNIYENZ5QUXFTJZFHV2K6XG6Q|      YES       |     8      |  5   |     Great for scars     |There used to ...  |09/07/2022|
|  5  | Megan Cooper |https://amazon.com/gp/profile/amzn1.account.AHUERNG2V5IUSQ3ZFRLPFAKGE2ZA|      YES       |     0      |  5   |    Good quality but     |The smell is extr..|10/29/2022|


```
## Want to contribute?
To get more information on contributing, go to the 
[CONTRIBUTING.md](https://github.com/officialpm/scrape-amazon/blob/master/CONTRIBUTING.md)

Also read the [CODE_OF_CONDUCT.md](https://github.com/officialpm/scrape-amazon/blob/master/CODE_OF_CONDUCT.md)
