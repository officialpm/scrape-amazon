import requests
from my_fake_useragent import UserAgent

url_prefix = "https://www.amazon"

# random user-agent
ua = UserAgent(family="chrome", os_family="windows")
# ua = UserAgent(cache=False, use_cache_server=False, safe_attrs=("__injections__",))


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
    user_agent = ua.random()
    while True:
        content: str = requests.get(url, headers={"User-Agent": user_agent})
        if "api-services-support@amazon.com" in content.text:
            user_agent = ua.random()
            continue
        break

    return content
