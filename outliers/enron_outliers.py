#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop("TOTAL", None)
data = featureFormat(data_dict, features)

#print(data_dict)
### your code below
bonusOver4M = []
index = 0;
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )
    if(bonus > 4000000):
        bonusOver4M.append(point)


for key in data_dict.keys():
    if data_dict[key]['salary'] == 1072321:
        print(key)
    if data_dict[key]['salary'] == 1111258:
        print(key)
    
print(bonusOver4M)
matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

