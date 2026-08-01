#pulled from https://stackoverflow.com/questions/67504953/how-to-get-full-job-descriptions-from-indeed-using-python-and-beautifulsoup

from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import re
import json
from pprint import pprint

url = 'https://boards-api.greenhouse.io/v1/boards/affirm/jobs' # url to scrape from? In single quotes, eg 'url.com'

response = requests.get(url)
data = response.text

data_json = json.loads(data)
jobs_list = data_json['jobs']

#data.close()
#pprint(d)

for posting in jobs_list:
   print('Company: ', posting['company_name'], '\nJob Title: ', posting['title'], '\nURL: ', posting['absolute_url'], '\n' )
