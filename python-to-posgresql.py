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

   # For a dictionary cursor, we can use the pg2x DictCursor:
   # cur = conn.cursor(cursor_factory=pg2x.DictCursor)

   ###########################################
   #
   # Using the 'with' clause in python and pg2
   #
   ############################################
   
   # with psycopg2.connect(
   #    host = hostname,
   #    dbname = database,
   #    user = username,
   #    password = pwd,
   #    port = port_id) as conn
   # with conn.cursor() as cur:
   #
   # # The with clause will close cursor for you
   # # with clause will also auto-commit any scripts
   # # You STILL need to close connection.
   

   #####################################
   #
   # Type the script to run on sql below
   #
   ####################################
   
   sql_script = '.'
   cur.execute(sql_script)

   #################################
   #
   # Examples of what Scritps to run:
   #
   ##################################
   
   # create_script = '''CREATE TABLE IF NOT EXISTS table_name(
   #                       field_name1 type1 restrictions1,
   #                       field_name2 type2 restructions2)'''

   # # To insert into above table: 
   # insert_script = 'INSERT INTO table_name(field_name1, field_name2) VALUES(%s,%s)'
   # # The %s is a placeholder value
   # insert_value = (val1, val2)
   # cur.execute(insert_script, insert_value)

   # # To drop a table entirely:
   # cur.execute('DROP TABLE IF EXISTS table_name')

   # # To Select from table:
   # cur.execute('SELECT * FROM table_name')
   # print(cur.fetchall()) # fetchall() returns a tuple of records/rows
   # from the table taken from the above script

   # # To update table records:
   # update_script = 'UPDATE table_name SET field_name1 = new_val1'

   # # To delete table records indivisually:
   # delete_script = 'DELETE FROM table_name WHERE field_name1 = %s'
   # delete_record = (old_val1,) # a list of vakues to replace each %s with
   # cur.execute(delete_script,delete_record)

   #########################################
   #
   # commit any scripts above to sql/pgAdmin
   #
   #########################################
   
   conn.commit()
   

   #Syntax for SQL will be the same here
   

except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

