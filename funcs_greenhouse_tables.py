# Outline taken from https://www.youtube.com/watch?v=M2NzvnfS-hI

from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import re
import json
from pprint import pprint
import psycopg2 as pg2
import psycopg2.extras as pg2x
import config

#############################
#
# Import Local Files
#
#############################

import scripts_greenhouse_tables as sgt


def Init_Job_Tables():
   # Need to provide these details in a config file
   hostname = config.hostname
   username = config.username
   database = config.database
   pwd = config.pwd
   port_id = config.port_id
   conn = None
   cur = None

   try:
      conn = pg2.connect(
          host = hostname,
          dbname = database,
          user = username,
          password = pwd,
          port = port_id)

      cur = conn.cursor()

      create_companies = sgt.create_companies
      create_jobs = sgt.create_jobs
      create_skills = sgt.create_skills
      create_job_skills = sgt.create_job_skills
      
      cur.execute(create_companies)
      cur.execute(create_jobs)
      cur.execute(create_skills)
      cur.execute(create_job_skills)

      conn.commit()

   except Exception as error:
       print(error)
   finally:
       if cur is not None:
           cur.close()
       if conn is not None:
           conn.close()
           
def Clear_Job_Tables():
   # Need to provide these details in a config file                                                                                                                                                                   
   hostname = config.hostname
   username = config.username
   database = config.database
   pwd = config.pwd
   port_id = config.port_id
   conn = None
   cur = None

   try:
      conn = pg2.connect(
          host = hostname,
          dbname = database,
          user = username,
          password = pwd,
          port = port_id)

      cur = conn.cursor()

      greenhouse_table_names = sgt.greenhouse_table_names

      for table_name in greenhouse_table_names:
           delete_script = 'DROP TABLE IF EXISTS ' + table_name + ' CASCADE'
           cur.execute(delete_script)

      conn.commit()

   except Exception as error:
       print(error)
   finally:
       if cur is not None:
           cur.close()
       if conn is not None:
           conn.close()


##################################
#
# Rudimentary Method for Loading Skills onto the skills table
#
##################################

def Load_Skills_Table():

   # Need to provide these details in a config file 

   hostname = config.hostname
   username = config.username
   database = config.database
   pwd = config.pwd
   port_id = config.port_id
   conn = None
   cur = None

   try:
      conn = pg2.connect(
          host = hostname,
          dbname = database,
          user = username,
          password = pwd,
          port = port_id)

      cur = conn.cursor()

      skills_list = sgt.skills_list
      add_skill = sgt.add_skill

      for skill in skills_list:
         cur.execute(add_skill,skill)

   except Exception as error:
      print(error)
   finally:
      if cur is not None:
          cur.close()
      if conn is not None:
          conn.close()

def Reset_Job_Tables():
   Clear_Greenhouse_Tables()
   Init_Greenhouse_Tables()
   Load_Skills_Table()
   
