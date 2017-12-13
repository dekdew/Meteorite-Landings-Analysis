"""create chart of 45716 meteorites"""
import json
import gmplot
import pygal
from pygal.style import DarkStyle, RedBlueStyle

def call_data():
    """call data from data.json and return data"""
    with open('data.json') as data_file:
        data = json.load(data_file)
    return data

def clean_data():
    """clean data and return somethings to create chart"""
    data = call_data() # call data

    lat, lng = [], [] # Latitude and Longitude
    found_lat, found_long = [], [] # meteorite found's Latitude and Longitude
    fail_lat, fail_long = [], [] # meteorite fail's Latitude and Longitude
    found, fail = 0, 0 # count meteorite fall
    years = {0:0} # count meteorite in each years 0 is unknown
    mass = {'0-10':0 , '10-100':0 , '100-1000':0 , '1000-10k':0 , '10K-100K':0 , '100K-1M':0 , '1M-10M':0 , '10M-100M':0, 'unknown':0} # count meteorite in each mass (g)

    for i in data:
        # Latitude and Longitude
        try:
            rlat = i['geolocation']['coordinates'][1]
            rlng = i['geolocation']['coordinates'][0]
            if (rlat not in lat) and (rlng not in lng):
                lat.append(rlat)
                lng.append(rlng)
        except:
            print('', end='')

        # found and fail Latitude and Longitude
        try:
            rlat = i['geolocation']['coordinates'][1]
            rlng = i['geolocation']['coordinates'][0]
            fall = i['fall']
            if (rlat not in found_lat) and (rlng not in found_long) and (fall == 'Found'):
                found_lat.append(rlat)
                found_long.append(rlng)
            elif (rlat not in fail_lat) and (rlng not in fail_long) and (fall == 'Fell'):
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

    return found, fail, years, mass, lat, lng, found_lat, found_long, fail_lat, fail_long

def create_chart():
    # get data from clean_data function
    found, fail, years, mass, lat, lng, found_lat, found_long, fail_lat, fail_long = clean_data()

    # all meteorites maps
    gmap = gmplot.GoogleMapPlotter(0, 0, 2)
    gmap.scatter(lat, lng, 'red', size=50000, marker=False)
    gmap.draw("../templates/map.html")

    # found meteorites maps
    gmap = gmplot.GoogleMapPlotter(0, 0, 2)
    gmap.scatter(found_lat, found_long, '#00134d', size=50000, marker=False)
    gmap.draw("../templates/found_map.html")

    # fail meteorites maps
    gmap = gmplot.GoogleMapPlotter(0, 0, 2)
    gmap.scatter(fail_lat, fail_long, '#4d0000', size=50000, marker=False)
    gmap.draw("../templates/fail_map.html")

    # create meteorite found and fail chart
    fall_chart = pygal.Pie(style=DarkStyle)
    fall_chart.title = "Meteorite found and fail"
    fall_chart.add('Found', found)
    fall_chart.add('Fail', fail)
    fall_chart.render_to_file('../static/img/fall.svg')

    # create meteorites classified by years chart
    years_chart = pygal.Bar(style=RedBlueStyle)
    years_chart.title = "Meteorites classified by years"
    for i in sorted(years):
        if i == 0:
            years_chart.add('unknown', years[i])
        else:
            years_chart.add(str(i), years[i])
    years_chart.render_to_file('../static/img/years.svg')

    # create meteorites classified by mass chart
    mass_chart = pygal.HorizontalBar(style=DarkStyle)
    mass_chart.title = "Meteorites classified by mass"
    for i in mass.keys():
        mass_chart.add(i, mass[i])
    mass_chart.render_to_file('../static/img/mass.svg')

create_chart()
