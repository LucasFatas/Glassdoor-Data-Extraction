# This class goes through the pages and breaks them up into individual reviews

import bs4
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from scrape import Scrape


class Pages:
    def getPages(url, maxPages):

        # this list will be used to store the reviews
        list = []

        # this driver is what controls google chrome
        driver = webdriver.Chrome(ChromeDriverManager().install())

        # tracks the page numbers
        pageNumber = 0

        # this counter is used to check if the page is empty because of a glitch that sometime occurs
        # if three empty pages are found the code assumes that no reviews are left
        emptyPages = 0

        while pageNumber >= 0 and pageNumber < int(maxPages) and emptyPages < 3:

            # increments page number
            pageNumber += 1

            # goes to page using the url and page number
            driver.get(url + str(pageNumber) + ".htm")

            # sets up the page to be parsed
            html = driver.page_source
            soup = bs4.BeautifulSoup(html, 'html.parser')

            # finds every review on the page and saves it to the list review
            reviews = soup.find_all("li", "empReview")

            # checks if pages has reviews
            if not reviews:
                emptyPages += 1  # increments empty page count since there are no reviews on page
            else:
                emptyPages = 0  # resets empty page counter in case last page was empty

                # this for loop goes through the list of reviews
                for review in reviews:
                    # call the function scrape_review for each review from the class Scrape and then adds
                    # the reviews to the list at the beginning of this class
                    list.append(Scrape.scrape_review(review))

        driver.close()  # closes the chrome tab

        return list  # returns the list of reviews
