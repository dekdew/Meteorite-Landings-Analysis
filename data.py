"""meteorite-landings-analysis"""
import json
import pygal
from pygal.style import NeonStyle

with open('meteorite-landings.json') as data_file:
    data = json.load(data_file)

found, fail = 0, 0
for i in data:
    if i['fall'] == 'Found':
        found += 1
    else:
        fail += 1
print(found, fail)

pie_chart = pygal.Pie(fill=True, interpolate='cubic', style=NeonStyle)
pie_chart.add('Found', found, colors='#fff')
pie_chart.add('Fail', fail)
pie_chart.render_to_file('pie_chart.svg')