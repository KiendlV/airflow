import requests
from dotenv import load_dotenv
from datetime import datetime
import os
#import matplotlib.pyplot as plt

load_dotenv()

current_date : str = datetime.today().strftime('%Y-%m-%d')

api_dict = { "lat" : 48.137154,
             "lon" : 11.576124,
             "dim" : 0.4,
             "date": current_date,
             "api_key": os.getenv("NASA_API")}


def get_data(URL : str):
    _data = requests.get(URL, params=api_dict)
    return _data
