# This class is used to temporarily store/organize review info during the scraping process
class Review:
    def __init__(self, date, summary, rating, workLifeBalance, cultureAndValues, careerOpportunities,
                 compensationAndBenefits, seniorManagement, authorJobTitle, mainText, pro, con):
        self.date = date
        self.summary = summary
        self.rating = rating
        self.workLifeBalance = workLifeBalance
        self.cultureAndValues = cultureAndValues
        self.careerOpportunities = careerOpportunities
        self.compensationAndBenefits = compensationAndBenefits
        self.seniorManagement = seniorManagement
        self.authorJobTitle = authorJobTitle
        self.mainText = mainText
        self.pro = pro
        self.con = con

