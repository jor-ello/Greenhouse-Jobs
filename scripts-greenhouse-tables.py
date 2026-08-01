#####################################
#
# Schemas and Scripts for Greenhouse Tables
#
#####################################

# Table 1 (Companies): company_id (Serial?), name (str)
#
#
# Table 2 (Jobs): job_id, company_id (linked), job_title, location, posted_date, updated_date, salary_low, salary_high, url
#
#
# Table 3 (Skills): skill_id (serial?), skill_name
#
#
# Table 4 (JobSkills): job_id (linked), skill_id (linked)
#
#
#
#
#
#




#####################################
#
# Creation Scripts
#
#####################################

create_companies = '''CREATE TABLE IF NOT EXISTS companies(                  
                          company_id type1 ,                     
                          name type2 )'''

create_jobs = ''''''

create_skills = ''''''

create_jobskills = ''''''

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

fortune_500 = ()

remote_first = ()
