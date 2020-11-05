#This class takes individual reviews and scrapes them for the information

from review import Review

class Scrape:
    def scrape_review(review):
        date = review.find("time", "date").text

        summary = review.find("h2", "summary").text.strip('"') #abstract
        summary = Scrape.clean(summary) #call function clean to remove bad characters and line breaks in the text

        rating = review.find("span", "rating").find("span")["title"] #overall rating

        #subratings
        workLifeBalance = None
        cultureAndValues = None
        careerOpportunities = None
        compensationAndBenefits = None
        seniorManagement = None
        # I wrapped this part in a try because not all reviews have sub ratings
        try:
            subRating = review.find("div", "subRatings").find_all("li")
            workLifeBalance = subRating[0].find("span")["title"]
            cultureAndValues = subRating[1].find("span")["title"]
            careerOpportunities = subRating[2].find("span")["title"]
            compensationAndBenefits = subRating[3].find("span")["title"]
            seniorManagement = subRating[4].find("span")["title"]
        except Exception:
            subRating = None

        authorJobTitle = review.find("span", "authorJobTitle").text
        authorJobTitle = Scrape.clean(authorJobTitle) #call function clean to remove bad characters and line breaks in the text

        mainText = review.find("p", "mainText").text
        mainText = Scrape.clean(mainText) #call function clean to remove bad characters and line breaks in the text

        info = review.find_all("div", "v2__EIReviewDetailsV2__fullWidth") # both con and pro stored in info

        pro = info[0].find("p", "v2__EIReviewDetailsV2__bodyColor").text
        pro = Scrape.clean(pro) #call function clean to remove bad characters and line breaks in the text

        con = info[1].find("p", "v2__EIReviewDetailsV2__bodyColor").text
        con = Scrape.clean(con) #call function clean to remove bad characters and line breaks in the text

        #returns all the information for the review, storing it in a Review object to make it easier to access later
        return Review(date, summary, rating, workLifeBalance, cultureAndValues, careerOpportunities,
                      compensationAndBenefits, seniorManagement, authorJobTitle, mainText, pro, con)

    def clean(text):
        return text.replace("\n", " ").replace("\r", " ").strip("-")
