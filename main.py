# This is the main class, it is the one that will recieve the command and arguments,
# and it also creates and writes the csv file

from pages import Pages
import csv
import sys

# checks if command has enough arguments
if (len(sys.argv) < 3):
    raise (Exception("Not enough arguments in command"))

if len(sys.argv) > 3:  # checks if a limit on pages has been put
    results = Pages.getPages(sys.argv[1].rstrip(".htm") + "_P",
                             sys.argv[3])  # calls the function getPages from the file Pages
else:  # if not limit it will put the limit to 10000
    results = Pages.getPages(sys.argv[1].rstrip(".htm") + "_P",
                             10000)  # calls the function getPages from the file Pages

# creates csv file in this folder
with open(sys.argv[2], mode='w') as csv_file:
    # sets up csv file
    writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # creates columns
    writer.writerow(['date', 'abstract', 'rating', 'workLifeBalance', 'cultureAndValues', 'careerOpportunities',
                     'compensationAndBenefits', 'seniorManagement', 'authorJobTitle', 'tenure', 'pro', 'con'])

    # adds reviews
    for review in results:
        writer.writerow([review.date, review.summary, review.rating, review.workLifeBalance, review.cultureAndValues,
                         review.careerOpportunities, review.compensationAndBenefits, review.seniorManagement,
                         review.authorJobTitle, review.mainText, review.pro, review.con])
