import json

def call_data():
    """call data from data.json and return data"""
    with open('data.json') as data_file:
        data = json.load(data_file)
    return data

def call(met):
    data = call_data()

    m_class, mass, fall, year, geolocation = 'n/a', 'n/a', 'n/a', 'n/a', 'n/a'

    for i in data:
        if met.lower() == i['name'].lower():
            try:
                m_class = i['recclass']
            except KeyError: # check if no data
                m_class = 'n/a'

            try:
                mass = i['mass']
            except KeyError: # check if no data
                mass = 'n/a'

            try:
                fall = i['fall']
            except KeyError: # check if no data
                fall = 'n/a'

            try:
                year = i['year'][:4].strip('-')
            except KeyError: # check if no data
                year = 'n/a'

            try:
                geolocation = i['geolocation']['coordinates']
            except KeyError: # check if no data
                location = 'n/a'

    return m_class, mass, fall, year, geolocation
