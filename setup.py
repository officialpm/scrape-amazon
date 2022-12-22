import setuptools

with open("README.md", encoding="utf8") as readme_file:
    README = readme_file.read()

setuptools.setup(
    name="scrape_amazon",
    version="0.2.0",
    description="Scrape Amazon Reviews",
    url="http://github.com/officialpm/scrape-amazon",
    author="Parth Maniar",
    author_email="officialparthmaniar@gmail.com",
    license="MIT",
    long_description_content_type="text/markdown",
    long_description=README,
    download_url="https://pypi.org/project/scrape-amazon",
    packages=setuptools.find_packages(),
    keywords=["Amazon", "Scrape", "Reviews", "Scraper", "Products"],
    python_requires=">=3.6",
    classifiers=[
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
    ],
    install_requires=[
        "beautifulsoup4",
        "pandas",
        "p_tqdm",
        "my_fake_useragent",
        "requests",
        "datefinder"
    ],
    entry_points={
        "console_scripts": ["scrape-amazon=scrape_amazon.cli:get_reviews_cli"],
    },
)
