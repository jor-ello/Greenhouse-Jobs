#pulled from https://stackoverflow.com/questions/67504953/how-to-get-full-job-descriptions-from-indeed-using-python-and-beautifulsoup
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import re

url = #url to scrape from? In single quotes, eg 'url.com'

response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'html.parser') #this line is meant to parse the html into something more reasonable
soup_list = soup.find_all('div',{'class':'^jobsearch-HeaderContainer'}) #meant to find all the divs with the specific class



for job in soup_list:
        #print('here') # debugging line to ensure we've entered loop
        title = job.find('a',{'class':'jobtitle'}).text
        link1 = job.find('a',{'class':'jobtitle'}).get('href')
        link = 'https://www.indeed.com' + link1

        #for each JOB's webpage, you need to connect to the link first:
        job_response = requests.get(link)
        job_data = job_response.text
        job_soup = BeautifulSoup(job_data, 'html.parser')

        job_description_tag = job_soup.find('div',{'id':'jobDescriptionText'})
        job_description = job_description_tag.text if job_description_tag else "N/A"
        print('Job Title:', title, '\nLink:', link, '\nJob Description:', job_description, '\n---')
