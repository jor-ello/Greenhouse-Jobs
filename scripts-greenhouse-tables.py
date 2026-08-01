#####################################
#
# Schemas and Scripts for Greenhouse Tables
#
#####################################

# Table 1 (companies): company_id (serial pk), company_name (str)
#
#
# Table 2 (jobs): job_id (serial pk), company_id (linked), job_title,
#                 location, posted_date, updated_date, salary_low, salary_high, url
#
#
# Table 3 (skills): skill_id (serial pk), skill_name
#
#
# Table 4 (job_skills): job_id (linked), skill_id (linked)
#





#####################################
#
# Creation Scripts
#
#####################################

create_companies = '''CREATE TABLE IF NOT EXISTS companies(                  
                          company_id       SERIAL           PRIMARY KEY ,                     
                          company_name     VARCHAR(100)     NOT NULL )'''

create_jobs = '''CREATE TABLE IF NOT EXISTS jobs(
                          job_id       SERIAL         PRIMARY KEY ,
                          company_id   INTEGER        REFERENCES companies(company_id) ,
                          job_title    VARCHAR(200)   NOT NULL ,
                          location     VARCHAR(200)   NOT NULL , 
                          posted_date  TIMESTAMP      NOT NULL ,
                          updated_date TIMESTAMP , 
                          salary_low   INTEGER , 
                          salary_high  INTEGER ,
                          url          VARCHAR(100)   NOT NULL )'''

create_skills = '''CREATE TABLE IF NOT EXISTS skills(
                          skill_id     SERIAL         PRIMARY KEY , 
                          skill_name   VARCHAR(100)   NOT NULL )'''

create_job_skills = '''CREATE TABLE IF NOT EXISTS job_skills(
                          job_id       INTEGER     REFERENCES jobs(job_id) , 
                          skill_id     INTEGER     REFERENCES skills(skill_id) )'''

#####################################
#
# Add/Update Row Scripts for Each Table
#
#####################################

add_company = ''

add_job = ''

add_skill = ''

add_jobskill = ''

update_company = ''

update_job = ''



#####################################
#
#
#
#####################################


#####################################
#
# Lists for Greenhouse Tables:
#
#####################################

greenhouse_table_names = ('companies','jobs','skills','jobskills')

fortune_500s = ()

remote_firsts = ()

skills_list = ()
