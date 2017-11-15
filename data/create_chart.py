"""create chart of 45716 meteorites"""
import json
import pygal
from pygal.style import NeonStyle

def call_data():
    """call data from data.json and return data"""
    with open('data.json') as data_file:
        data = json.load(data_file)
    return data

def clean_data():
    """clean data and return somethings to create chart"""
    data = call_data() # call data
    print(data[0]['year'][:4])

    found, fail = 0, 0 # count meteorite fall
    years = {0:0} # count meteorite in each years 0 is unknown
    mass = {'0':0 , '1':0 , '2':0 , '3':0 , '4':0 , '5':0 , '6':0 , '7':0} # count meteorite in each mass (g)
    # '0' is 0-10, '1' is 10-100, '2' is 100-1000, '3' is 1000-10K, '4' is 10K-100K, '5' is 100K-1M, '6' is 1M-10M, '7' is 10M-100M

    for i in data:
        # count meteorite fall
        if i['fall'] == 'Found':
            found += 1
        else:
            fail += 1

        # count meteorite in each years
        try:
            year = int(i[u'year'][:4].strip('-'))
            if year in years: # check if year is already in dict years
                years[year] += 1 # value of this year + 1
            else: # check if year is not in dict years then create key year
                years[year] = 1 # value of this year = 1
        except KeyError: # check if year is no data
            years[0] += 1 # value of unknown + 1

    print(found, fail, found+fail)
    print(sorted(years), sum(years.values()))

clean_data()