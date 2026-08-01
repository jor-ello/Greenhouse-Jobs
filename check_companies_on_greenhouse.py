#pulled from https://stackoverflow.com/questions/67504953/how-to-get-full-job-descriptions-from-indeed-using-python-and-beautifulsoup

from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import re
import json
from pprint import pprint
import scripts_greenhouse_tables as sgt

companies = sgt.fortune_500s_california + sgt.remote_companies + sgt.remote_firsts

# Lowercase and remove spaces from elements of list
companies = list(map(str.lower , companies))
companies = [x.strip(' ') for x in companies]
#companies = [x.strip('.com') for x in companies]
#companies = [x.strip('.') for x in companies]

# Remove Duplicate Companies
companies = list(set(companies))


greenhouse_companies = []



for company in companies:

   url = 'https://boards-api.greenhouse.io/v1/boards/'+ company  + '/jobs' # url to scrape from? In single quotes, eg 'url.com'

   response = requests.get(url)
   data = response.text

   try:
      data_json = json.loads(data)
      try:
         jobs_list = data_json['jobs']
         greenhouse_companies.append(company)
      except:
         print(company, ' does NOT have a greenhouse api site')
   except:
      print(company, ' does NOT have a greenhouse api site, and has weird data')
         
print('\n\n')

for company in greenhouse_companies:
   print(company)
