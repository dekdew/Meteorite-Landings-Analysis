import json

def call_data():
    """call data from data.json and return data"""
    with open('data.json') as data_file:
        data = json.load(data_file)
    return data

def call(met):
    data = call_data() # get data from call_data function

    met = met.replace('+', ' ') # get meteorite's name from user input

    # set variable as n/a
    m_class, mass, fall, year, geolocation, lat, lon = 'n/a', 'n/a', 'n/a', 'n/a', 'n/a', 0, 0

    # find meteorite from dataset
    for i in data:
        if met.lower() == i['name'].lower(): # check if name is matched
            # set meteorite's class
            try:
                m_class = i['recclass']
            except KeyError: # check if no data
                m_class = 'n/a'

            # set meteorite's mass
            try:
                mass = i['mass']
            except KeyError: # check if no data
                mass = 'n/a'

            # set meteorite's fall
            try:
                fall = i['fall']
            except KeyError: # check if no data
                fall = 'n/a'

            # set meteorite's year
            try:
                year = i['year'][:4].strip('-')
            except KeyError: # check if no data
                year = 'n/a'

            # set meteorite's location
            try:
                geolocation = i['geolocation']['coordinates']
            except KeyError: # check if no data
                location = 'n/a'

            # set meteorite's lat
            try:
                lat = float(i['reclat'])
            except KeyError:
                lat = 0

            # set meteorite's long
            try:
                lon = float(i['reclong'])
            except KeyError:
                lon = 0


    return m_class, mass, fall, year, geolocation, lat, lon
