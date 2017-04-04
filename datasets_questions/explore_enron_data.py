#/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

item = enron_data["SKILLING JEFFREY K"]
count = 0
for key in enron_data:
	print(key)
	if enron_data[key]["poi"] == 1:
		#print(count)
		count += 1
import math
salaryCount = 0
emailCount = 0
for key in enron_data:
    for key2 in enron_data[key]:
        print '%s - %s: %s' % (key, key2, enron_data[key][key2])

for key in enron_data:
    #for key2 in enron_data[key]:
    if enron_data[key]["poi"] == 1:
        salaryCount += 1

print salaryCount


# print(enron_data["SKILLING JEFFREY K"]["total_payments"])
# print(enron_data["FASTOW ANDREW S"]["total_payments"])
# print(enron_data["LAY KENNETH L"]["total_payments"])
# print(count)
# print(len(item))
# print(len(enron_data))
