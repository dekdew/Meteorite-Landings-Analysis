import json
import pygal
from pygal.style import NeonStyle

def call_data():
    """call data from data.json and return data"""
    with open('data.json') as data_file:
        data = json.load(data_file)
    return data

def clean_data():
    count = 0
    data = call_data()
    for i in data:
        count += 1
    print(count)
clean_data()