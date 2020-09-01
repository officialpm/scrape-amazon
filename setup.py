import setuptools

with open('README.md') as readme_file:
    README = readme_file.read()
    
setuptools.setup(name='scrape_amazon_reviews',
                 version='0.1.1',
                 description='Scrape Amazon Reviews',
                 url='http://github.com/officialpm/scrape-amazon-reviews',
                 author='Parth Maniar',
                 author_email='officialparthmaniar@gmail.com',
                 license='MIT',
                 long_description_content_type="text/markdown",
                 long_description=README,
                 download_url = "https://pypi.org/project/scrape-amazon-reviews",
                 packages=setuptools.find_packages(),
                 keywords=["Amazon", "Scrape", "Reviews", "Scraper"],
                 python_requires='>=3.6',
                 classifiers=[
                     "Programming Language :: Python :: 3",
                     "License :: OSI Approved :: MIT License",
                     "Operating System :: OS Independent",
                 ], install_requires=['beautifulsoup4', 'pandas', 'tqdm'])
