# You can manually adjust this code to call a json file containing the links to multiple companies and the code
# will get the data for all of them, examples of how the json file should look can be found in folder companyLists

from main import Main
import json

with open('companyLists/giants.json') as json_file:
    data = json.load(json_file)
    for x in range(23, 25):
        Main.getData(data['companies'][x]['link'].rstrip(".htm") + "_P", data['companies'][x]['file'], 100)

# for company in list:
#    Main.getData(company[0].rstrip(".htm")+"_P", company[1], company[2])
