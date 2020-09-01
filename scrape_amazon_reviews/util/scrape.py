from bs4 import BeautifulSoup
import re
import pandas as pd
from .urlFunctions import get_URL
import math
from tqdm.auto import tqdm

flatten = lambda l: [item for sublist in l for item in sublist]

def get_all_review_page_url(res: str) -> str:
    productPage = BeautifulSoup(res.text, 'html.parser')
    path : str = productPage.find("a", {"data-hook" : "see-all-reviews-link-foot"})['href']
    return path

def extractPage(url: str) -> str:
    r = get_URL(url)
    pageNotLoaded = True
    productPage = BeautifulSoup(r.text, 'html.parser')
    checkReviewLen= len(productPage.findAll("i", {"class" : "review-rating"}))
    if checkReviewLen > 0 : pageNotLoaded = False
    while pageNotLoaded:
        r = get_URL(url)
        productPage = BeautifulSoup(r.text, 'html.parser')
        checkReviewLen= len(productPage.findAll("i", {"class" : "review-rating"}))
        if checkReviewLen > 0 : pageNotLoaded = False
    reviewers = []
    ratings = []
    reviewDescriptions = []
    reviewTitles = []
    reviewrsSpan = productPage.findAll("span", {"class" : "a-profile-name"})
    ratingsSpan = productPage.findAll("i", {"class" : "review-rating"})
    reviewTitlesSpan = productPage.findAll("a", {"class" : "review-title-content"})
    reviewDescriptionSpan = productPage.findAll("span", {"class" : "review-text-content"})

    for i in range(2,len(reviewrsSpan)):     # Loop is initiated from 2 because we have to exclude the Top Positive and Top Critical Review which otherwise will get repeated.
        reviewers.append(reviewrsSpan[i].get_text())
        ratings.append(int(ratingsSpan[i].get_text()[0]))

    for i in range(0,len(reviewTitlesSpan)):
        reviewTitles.append(reviewTitlesSpan[i].get_text())
        reviewDescriptions.append(reviewDescriptionSpan[i].get_text())

    reviewDescriptions[:] = [i.lstrip('\n').rstrip('\n').strip() for i in reviewDescriptions]
    reviewTitles[:] = [i.lstrip('\n').rstrip('\n') for i in reviewTitles]

    return reviewers, ratings, reviewTitles, reviewDescriptions

def extractTotalPages(url):
  r = get_URL(url)
  productPage = BeautifulSoup(r.text, 'html.parser')
  pageSpanText = productPage.find("span", {"data-hook" : "cr-filter-info-review-count"}).get_text()
  regex = re.compile('of ([0-9]*)')
  totalReviews = int (regex.findall(pageSpanText.replace(",",""))[0])
  return math.ceil(totalReviews/10), productPage.find("title").get_text(), totalReviews

def scrape_reviews(url):
    totalReviewers = []
    totalRatings = []
    totalReviewDescriptions = []
    totalReviewTitles = []
    totalPages, pageTitle, totalReviews = extractTotalPages(url)
    print(f"[scrape-amazon-reviews]  - {pageTitle}")
    print(f"[scrape-amazon-reviews] Total Pages - {totalPages}")
    print(f"[scrape-amazon-reviews] Total Reviews - {totalReviews}\n")
    for page in tqdm(range(1,totalPages+1)):

        urlToFetch = url+f"?pageNumber={page}"
        reviewers, ratings, reviewTitles, reviewDescriptions = extractPage(urlToFetch)
        totalReviewers.append(reviewers)
        totalRatings.append(ratings)
        totalReviewDescriptions.append(reviewDescriptions)
        totalReviewTitles.append(reviewTitles)

    totalReviewers = flatten(totalReviewers)
    totalRatings = flatten(totalRatings)
    totalReviewDescriptions = flatten(totalReviewDescriptions)
    totalReviewTitles = flatten(totalReviewTitles)
    
    productReviewsData = pd.DataFrame()
    
    # Adding Information    

    productReviewsData["Reviewer"] = totalReviewers
    productReviewsData["Rating"] = totalRatings
    productReviewsData["Title"] = totalReviewDescriptions
    productReviewsData["Description"] = totalReviewDescriptions
    # productReviewsData["link"] = url
    # productReviewsData["Product Title"] = pageTitle
    
    return productReviewsData
    
    