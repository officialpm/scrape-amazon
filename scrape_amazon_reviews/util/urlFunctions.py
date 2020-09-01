import requests

url_prefix = "https://www.amazon.in"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

def construst_reviews_URL(product_id: str) -> str:
    """Constructs review URL.
    Args:
        product_id
    Returns:
        Constructed URL.
    """
    return f"{url_prefix}/dp/product-reviews/{product_id}"

def get_URL(url: str) -> str:
    """Gets the contents of a remote url.
    Args:
        url
    Returns:
        The content fetched from remote url.
    """
    content: str = requests.get(url,headers=headers)
    return content