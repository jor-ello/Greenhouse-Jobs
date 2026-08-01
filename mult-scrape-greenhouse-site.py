#pulled from https://stackoverflow.com/questions/67504953/how-to-get-full-job-descriptions-from-indeed-using-python-and-beautifulsoup

from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import re
import json
from pprint import pprint

companies = ['affirm','gitlab']

for company in companies:

   url = 'https://boards-api.greenhouse.io/v1/boards/'+ company  + '/jobs' # url to scrape from? In single quotes, eg 'url.com'

   response = requests.get(url)
   data = response.text

   data_json = json.loads(data)
   jobs_list = data_json['jobs']

   #data.close()
   #pprint(d)

   for posting in jobs_list:
      #print('Company: ', posting['company_name'], '\nJob Title: ', posting['title'], '\nURL: ', posting['absolute_url'], '\n' )
      posting_url = 'https://boards-api.greenhouse.io/v1/boards/'+ company  + '/jobs/' + str(posting['id'])  #Job Specific Posting
      posting_response = requests.get(posting_url)
      posting_data = posting_response.text

      current = json.loads(posting_data)

      desc_html = current['content']
      desc_text = BeautifulSoup(desc_html, "html.parser").get_text()

      print('Company: ', current['company_name'], '\nJob Title: ', current['title'], '\nURL: ', current['absolute_url'], '\nContent: ',  desc_text)
      #print('Company: ', current['company_name'], '\nJob Title: ', current['title'], '\nURL: ', current['absolute_url'])
      #print(posting_url + '\n')

      
