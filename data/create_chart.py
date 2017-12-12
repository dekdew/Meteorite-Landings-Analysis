"""create chart of 45716 meteorites"""
import json
import gmplot
import pygal
from pygal.style import DarkStyle, CleanStyle

def call_data():
    """call data from data.json and return data"""
    with open('data.json') as data_file:
        data = json.load(data_file)
    return data

def clean_data():
    """clean data and return somethings to create chart"""
    data = call_data() # call data

    lat, lng = [], []
    found_lat, found_long = [], []
    fail_lat, fail_long = [], []
    found, fail = 0, 0 # count meteorite fall
    years = {0:0} # count meteorite in each years 0 is unknown
    mass = {'0-10':0 , '10-100':0 , '100-1000':0 , '1000-10k':0 , '10K-100K':0 , '100K-1M':0 , '1M-10M':0 , '10M-100M':0, 'unknown':0} # count meteorite in each mass (g)

    for i in data:
        # lat long
        try:
            rlat = i['geolocation']['coordinates'][1]
            rlng = i['geolocation']['coordinates'][0]
            if (rlat not in lat) and (rlng not in lng):
                lat.append(rlat)
                lng.append(rlng)
        except:
            print('', end='')

        # found fail lat long
        try:
            rlat = i['geolocation']['coordinates'][1]
            rlng = i['geolocation']['coordinates'][0]
            fall = i['fall']
            if fall == 'Found':
                found_lat.append(rlat)
                found_long.append(rlng)
            elif fall == 'Fell':
                fail_lat.append(rlat)
                fail_long.append(rlng)    
        except:
            print('', end='')


        # count meteorite fall
        if i['fall'] == 'Found':
            found += 1
        else:
            fail += 1

        # count meteorite in each years
        try:
            year = int(i['year'][:4].strip('-'))
            if year in years: # check if year is already in dict years
                years[year] += 1 # value of this year + 1
            else: # check if year is not in dict years then create key year
                years[year] = 1 # value of this year = 1
        except KeyError: # check if year is no data
            years[0] += 1

        # count meteorite in each mass
        try:
            m_mass = float(i['mass'])
            if 0 <= m_mass < 10:
                mass['0-10'] += 1
            elif 10 <= m_mass < 100:
                mass['10-100'] += 1
            elif 100 <= m_mass < 1000:
                mass['100-1000'] += 1
            elif 1000 <= m_mass < 10000:
                mass['1000-10k'] += 1
            elif 10000 <= m_mass < 100000:
                mass['10K-100K'] += 1
            elif 100000 <= m_mass < 1000000:
                mass['100K-1M'] += 1
            elif 1000000 <= m_mass < 10000000:
                mass['1M-10M'] += 1
            else:
                mass['10M-100M'] += 1
        except KeyError:
            mass['unknown'] += 1

    #print(found, fail, found+fail)
    #print(sorted(years), sum(years.values()))
    #print(mass)
    return found, fail, years, mass, lat, lng, found_lat, found_long, fail_lat, fail_long

def create_chart():
    found, fail, years, mass, lat, lng, found_lat, found_long, fail_lat, fail_long = clean_data()

    gmap = gmplot.GoogleMapPlotter(0, 0, 2)
    gmap.scatter(lat, lng, 'red', size=50000, marker=False)
    gmap.draw("map.html")

    gmap = gmplot.GoogleMapPlotter(0, 0, 2)
    gmap.scatter(found_lat, found_long, '#00134d', size=50000, marker=False)
    gmap.draw("found_map.html")

    gmap = gmplot.GoogleMapPlotter(0, 0, 2)
    gmap.scatter(fail_lat, fail_long, '#4d0000', size=50000, marker=False)
    gmap.draw("fail_map.html")

    fall_chart = pygal.Pie(style=DarkStyle)
    fall_chart.title = "Meteorite flasks"
    fall_chart.add('Found', found)
    fall_chart.add('Fail', fail)
    fall_chart.render_to_file('../static/img/fall.svg')

    years_chart = pygal.Bar(style=DarkStyle)
    years_chart.title = "Years found"
    for i in sorted(years):
        if i == 0:
            years_chart.add('unknown', years[i])
        else:
            years_chart.add(str(i), years[i])
    years_chart.render_to_file('../static/img/years.svg')

    mass_chart = pygal.HorizontalBar(style=CleanStyle)
    mass_chart.title = "Mass's flasks"
    for i in mass.keys():
        mass_chart.add(i, mass[i])
    mass_chart.render_to_file('../static/img/mass.svg')

    print(found_lat)
    print(fail_lat)
create_chart()
