import math
import re
import datefinder
import pandas as pd
from bs4 import BeautifulSoup
from p_tqdm import p_map

from .urlFunctions import get_URL


def flatten(list):
    return [item for sublist in list for item in sublist]


def get_all_review_page_url(res: str) -> str:
    productPage = BeautifulSoup(res.text, "html.parser")
    path: str = productPage.find("a", {"data-hook": "see-all-reviews-link-foot"})[
        "href"
    ]
    return path


def extractPage(url: str) -> str:
    r = get_URL(url)
    pageNotLoaded = True
    productPage = BeautifulSoup(r.text, "html.parser")
    checkReviewLen = len(productPage.findAll("i", {"class": "review-rating"}))
    if checkReviewLen > 0:
        pageNotLoaded = False
    while pageNotLoaded:
        r = get_URL(url)
        productPage = BeautifulSoup(r.text, "html.parser")
        checkReviewLen = len(productPage.findAll("i", {"class": "review-rating"}))
        if checkReviewLen > 0:
            pageNotLoaded = False
    reviewers = []
    ratings = []
    ratingsDate = []
    reviewDescriptions = []
    reviewTitles = []
    reviewrsSpan = productPage.findAll("span", {"class": "a-profile-name"})
    reviewDate = productPage.findAll("span", {"class": "review-date"})
    ratingsSpan = productPage.findAll("i", {"class": "review-rating"})
    reviewTitlesSpan = productPage.findAll("a", {"class": "review-title-content"})
    reviewDescriptionSpan = productPage.findAll(
        "span", {"class": "review-text-content"}
    )

    # Loop is initiated from 2 because we have to exclude the Top Positive and
    # Top Critical Review which otherwise will get repeated.
    for i in range(2, len(reviewrsSpan)):
        reviewers.append(reviewrsSpan[i].get_text())
        ratings.append(int(ratingsSpan[i].get_text()[0]))
        matches = datefinder.find_dates(reviewDate[i].get_text())
        ratingsDate.append(list(matches)[0].strftime("%m/%d/%Y"))

    for i in range(0, len(reviewTitlesSpan)):
        reviewTitles.append(reviewTitlesSpan[i].get_text())
        reviewDescriptions.append(reviewDescriptionSpan[i].get_text())

    reviewDescriptions[:] = [
        i.lstrip("\n").rstrip("\n").strip() for i in reviewDescriptions
    ]
    reviewTitles[:] = [i.lstrip("\n").rstrip("\n") for i in reviewTitles]

    return {
        "reviewers": reviewers,
        "ratings": ratings,
        "reviewTitles": reviewTitles,
        "reviewDescriptions": reviewDescriptions,
        "date": ratingsDate,
    }


def extractTotalPages(url):
    r = get_URL(url)
    productPage = BeautifulSoup(r.text, "html.parser")
    pageSpanText = productPage.findAll(
        "span", {"class": "a-size-base a-color-secondary"}
    )[0].get_text()
    totalReviews = int(re.findall(r"\d+", pageSpanText.replace(",", ""))[0])
    return (
        math.ceil(totalReviews / 10),
        productPage.find("title").get_text(),
        totalReviews,
    )


def scrape_reviews(url):
    totalPages, pageTitle, totalReviews = extractTotalPages(url)
    print(f"[scrape-amazon]  - {pageTitle}")
    print(f"[scrape-amazon] Total Pages - {totalPages}")
    print(f"[scrape-amazon] Total Reviews - {totalReviews}\n")
    urlsToFetch = []
    for page in range(1, totalPages + 1):
        urlToFetch = url + f"?pageNumber={page}"
        urlsToFetch.append(urlToFetch)

    results = p_map(extractPage, urlsToFetch)
    res = {}
    for k in results:
        for list in k:
            if list in res:
                res[list] += k[list]
            else:
                res[list] = k[list]

    productReviewsData = pd.DataFrame()

    # # Adding Information

    productReviewsData["Reviewer"] = res["reviewers"]
    productReviewsData["Rating"] = res["ratings"]
    productReviewsData["Title"] = res["reviewTitles"]
    productReviewsData["Description"] = res["reviewDescriptions"]
    productReviewsData["Date"] = res["date"]
    # productReviewsData["link"] = url
    # productReviewsData["Product Title"] = pageTitle

    return productReviewsData
