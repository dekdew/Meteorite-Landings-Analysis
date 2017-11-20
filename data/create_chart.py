"""create chart of 45716 meteorites"""
import json
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

    found, fail = 0, 0 # count meteorite fall
    years = {0:0} # count meteorite in each years 0 is unknown
    mass = {'unknown':0,'0-10':0 , '10-100':0 , '100-1000':0 , '1000-10k':0 , '10K-100K':0 , '100K-1M':0 , '1M-10M':0 , '10M-100M':0} # count meteorite in each mass (g)

    for i in data:
        # count meteorite fall
        if i['fall'] == 'Found':
            found += 1
        else:
            fail += 1

        # count meteorite in each years and mass
        try:
            year = int(i['year'][:4].strip('-'))
            if year in years: # check if year is already in dict years
                years[year] += 1 # value of this year + 1
            else: # check if year is not in dict years then create key year
                years[year] = 1 # value of this year = 1
        except KeyError: # check if year is no data
            years[0] += 1

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
        except:
            mass['unknown'] += 1

    #print(found, fail, found+fail)
    #print(sorted(years), sum(years.values()))
    #print(mass)
    return found, fail, years, mass

def create_chart():
    found, fail, years, mass = clean_data()

    fall_chart = pygal.Pie(style=DarkStyle)
    fall_chart.add('Found', found)
    fall_chart.add('Fail', fail)
    fall_chart.render_to_file('../static/img/fall.svg')

    years_chart = pygal.Bar(style=DarkStyle)
    for i in sorted(years):
        if i == 0:
            years_chart.add('unknown', years[i])
        else:
            years_chart.add(str(i), years[i])
    years_chart.render_to_file('../static/img/years.svg')

    mass_chart = pygal.HorizontalBar(style=CleanStyle)
    for i in mass.keys():
        mass_chart.add(i, mass[i])
    mass_chart.render_to_file('../static/img/mass.svg')
create_chart()