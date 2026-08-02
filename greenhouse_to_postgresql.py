from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import re
import json
import psycopg2 as pg2
import psycopg2.extras as pg2x


####################
#
# Local file imports
#
####################

import funcs_greenhouse_tables as fgt
import scripts_greenhouse_tables as sgt
import config

#############################################
#
# Initialize Lists, Connecting to Database, and Initializing Tables if not already created
#
#############################################

fgt.Clear_Job_Tables()
fgt.Init_Job_Tables()

companies = sgt.greenhouse_companies

# Need to provide these details in a config file

hostname = config.hostname
username = config.username
database = config.database
pwd = config.pwd
port_id = config.port_id
conn = None
cur = None

add_company = sgt.add_company
add_job = sgt.add_job
add_job_skill = sgt.add_job_skill

try:
   
   conn = pg2.connect(
       host = hostname,
       dbname = database,
       user = username,
       password = pwd,
       port = port_id)

   cur = conn.cursor(cursor_factory=pg2x.DictCursor)

   for company in companies:

      #Debug Line to tell we're in this line:
      print('Checking company: ', company)

      company_url = [
                     'https://boards-api.greenhouse.io/v1/boards/'
                     + company
                     + '/jobs' ]# url to scrape from, single quotes, eg 'url.com' 
                    
      response = requests.get(company_url[0])
      data = response.text

      data_json = json.loads(data)

      jobs_list = data_json['jobs']
      
      try:
          jobs_list = data_json['jobs']
          cur.execute(add_company , (company,))
          curr_company_id = cur.fetchone()[0]
          conn.commit()
          print(curr_company_id)
          # jobs_list = []
      except:
          jobs_list = []
          print('Cannot pull jobs from ', company)
          
      for posting in jobs_list:
         
         # Debug Line to check loop iteration
         # print('Checking job title: ', posting['title'])

         # debug line
         # print('Company: ', posting['company_name'], '\nJob Title: ',
         #       posting['title'], '\nURL: ', posting['absolute_url'], '\n' )


         ###########################
         #
         # Job Specific posting url: Should include more specific data
         #
         ###########################

         
         posting_url = [
            'https://boards-api.greenhouse.io/v1/boards/'
            + company
            + '/jobs/' + str(posting['id'])]
         posting_response = requests.get(posting_url[0])
         posting_data = posting_response.text

         current_job = json.loads(posting_data)

         conn.commit()
         

         ##################################################################
         #
         # Add Job to Database or Update if it is Already on the Database 
         #
         ##################################################################

         # Debug Line to check loop iteration 
         # print('Checking job title: ', current_job['title'])

         try:
            
            job_title = current_job['title']
            gj_id = current_job['id']
            ij_id = current_job['internal_job_id']
            loc = current_job['location']['name']
            posted = current_job['first_published']
            updated = current_job['updated_at']
            url = current_job['absolute_url']

            cur.execute(add_job , (gj_id, ij_id, curr_company_id, job_title, loc, posted, updated, url))
            
            conn.commit()
         except:
            print('Error inserting: ' , current_job['title'])



         

         ####################################
         #
         # Processing Description (to add NLP)
         #
         # This section is meant to parse the meaty parts of the job posting for more useful information 
         # to be found regarding job qualifications, salary, benefits, etc
         #
         #
         ####################################

         # desc_html = current['content']
         # desc_text = BeautifulSoup(desc_html, "html.parser").get_text()

         # Debug print lines

         # print('Company: ', current['company_name'], '\nJob Title: ',
         #       current['title'], '\nURL: ', current['absolute_url'], '\nContent: ',  desc_text)
         # print('Company: ', current['company_name'], '\nJob Title: ',
         #       current['title'], '\nURL: ', current['absolute_url'])
         # print(posting_url + '\n')

except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
   
