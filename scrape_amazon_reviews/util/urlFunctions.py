import requests

url_prefix = "https://www.amazon"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
# random user-agent

from fake_useragent import UserAgent
ua = UserAgent(cache=False, use_cache_server=False)

def construst_reviews_URL(domain: str, product_id: str) -> str:
    """Constructs review URL.
    Args:
        product_id
    Returns:
        Constructed URL.
    """
    return f"{url_prefix}.{domain}/dp/product-reviews/{product_id}"

def get_URL(url: str) -> str:
    """Gets the contents of a remote url.
    Args:
        url
    Returns:
        The content fetched from remote url.
    """
    user_agent = ua.random
    while (True):
        content: str = requests.get(url, headers={'User-Agent': user_agent})
        if "api-services-support@amazon.com" in content.text:
            user_agent = ua.random
            continue
        break
        
    return content