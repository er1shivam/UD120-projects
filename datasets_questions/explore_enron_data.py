#!/usr/bin/python

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

# print enron_data

length_enron = len(enron_data)
no_of_poi = len([1 for k in enron_data.values() if k["poi"] == 1])


print "No of persons ", length_enron
print "No of features", [len(v) for v in enron_data.values()][0]

print "No of Person of Interest " , no_of_poi

poi_names = open("../final_project/poi_names.txt").read().split('\n')

print "No of persons in text file " ,len([1 for val in poi_names if ('(y)' in val or '(n)' in val)])


print "Total value of stock(James Prentice)", enron_data["PRENTICE JAMES"]["total_stock_value"]

print "No of emails from Wesley Colwell ", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

print "Stock option excercised by Jeffrey K Skilling", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

keys = ["SKILLING JEFFREY K","FASTOW ANDREW S", "LAY KENNETH L" ]
who_money = {k : enron_data[k]["total_payments"] for k in keys}
print "Max payment taken home is ", max(who_money.values()) , "by ", [k for k in who_money.keys() if who_money[k] == max(who_money.values())][0]

print "No of quatified salary " , len([1 for i in enron_data if enron_data[i]["salary"] != "NaN"])
print "No of known email add  " , len([1 for i in enron_data if enron_data[i]["email_address"] != "NaN"])

no_of_total_payment_nan = len([1 for i in enron_data if enron_data[i]["total_payments"] == "NaN"])
print "no of nan payments", no_of_total_payment_nan
print "percentage of NaN in total payments" , no_of_total_payment_nan / float(length_enron) * 100 

#percentage of poi in the dataset having NaN for total payments
no_of_poi_nan = len([1 for i in enron_data if enron_data[i]["poi"]==1 if enron_data[i]["total_payments"] == "NaN"])
print "No of poi with nan", no_of_poi_nan
print "Percentage of poi having NaN total payments " ,no_of_poi_nan / no_of_poi * 100
