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


#####################################
#
# Lists of Companies
#
#####################################



fortune_500s_california = [
    'Live Nation Entertainment',
    'Walt Disney',
    'Monster Beverage',
    'Ross Stores',
    'A-Mark Precious Metals',
    'Gilead Sciences',
    'TD Synnex',
    'Lam Research',
    'Ingram Micro',
    'Molina Healthcare',
    'Netflix',
    'Skechers U.S.A.',
    'Meta',
    'KLA',
    'Sandisk',
    'Alphabet',
    'Intuit',
    'Concentrix',
    'Pacific Life',
    'Chipotle Mexican Grill',
    'PG&E',
    'Block',
    'Broadcom',
    'HP',
    'Workday',
    'Equinix',
    'Edison International',
    'Qualcomm',
    'LPL Financial',
    'Sempra',
    'Wells Fargo',
    'Uber',
    'Salesforce',
    'Visa',
    'Gap',
    'DoorDash',
    'Airbnb',
    'Prologis',
    'Cisco Systems',
    'PayPal',
    'Adobe',
    'Super Micro Computer',
    'Ebay',
    'Western Digital',
    'Sanmina',
    'Franklin Resources',
    'Nvidia',
    'Intel',
    'Advanced Micro Devices',
    'Applied Materials',
    'ServiceNow',
    'Palo Alto Networks',
    'Arista Networks',
    'Marvell Technology',
    'Intuitive Surgical',
    'Synopsys',
    'Amgen',
    'Farmers Insurance Exchange']

remote_companies = [
    'Lockheed Martin',
    'Marsh McLennan Agency',
    'Marriott International',
    'SAIC',
    'Humana',
    'Verizon',
    'Optum',
    'AECOM',
    'State of Michigan',
    'WSP',
    'Compass',
    'Centene',
    'PNC Financial',
    'Conduent',
    'Amentum',
    'Elevance Health',
    'Amgen',
    'Amazon.',
    'GE Healthcare',
    'CIBC',
    'Concentrix',
    'Banner Health',
    'Northrop Grumman',
    'DoorDash',
    'Google',
    'CVS Health',
    'ServiceNow',
    'Stantec',
    'Oracle',
    'Leidos',
    'Alberta Health',
    'Workday',
    'Allstate Insurance',
    'Cognizant Technology',
    'Meta',
    'S&P Global',
    'IQVIA',
    'Morgan Stanley',
    'Tetra Tech',
    'Honeywell',
    'Tenet Healthcare',
    'Cardinal Health',
    'Capital One',
    'Johnson & Johnson',
    'Wells Fargo',
    'ADP',
    'Cisco',
    'Thermo Fisher Scientific',
    'Northwestern Mutual',
    'Coldwell Banker',
    'TELUS',
    'Mercer',
    'General Dynamics (IT)',
    'Ascension',
    'Abbott',
    'FedEx Logistics',
    'Thomson Reuters',
    'Comcast',
    'Microsoft',
    'GEICO',
    'Children’s Mercy',
    'DXC Technology',
    'M&T Bank',
    'Warner Bros Discovery',
    'Visa',
    'Raytheon',
    'John Deere',
    'Ford Motor',
    'Baxter Woodman',
    'Cushman & Wakefield',
    'Kaiser Permanente',
    'Truist',
    'Best Buy',
    'State Street',
    'Aramark',
    'Motorola Solutions',
    '3M',
    'Coldwell Banker Schmidt',
    'EPAM Systems',
    'SAP',
    'Fidelity Investments',
    'UnitedHealthcare',
    'NBCUniversal',
    'UST',
    'Mastercard',
    'Marsh McLennan (corp)',
    'T‑Mobile',
    'TD',
    'AT&T',
    'Pfizer',
    'GE Aerospace',
    'JLL',
    'Spectrum',
    'Gartner',
    'AbbVie',
    'Mondelēz International',
    'Medtronic',
    'FIS',
    'Scotiabank',
    'Bell Canada']

remote_firsts = [
    '10up',
    '37signals',
    'Automattic',
    'AwesomeMotive',
    'BairesDev',
    'Bandcamp',
    'BandLab',
    'Buffer',
    'Bunny.net',
    'Canonical',
    'Chef',
    'chess.com',
    'Cloudbeds',
    'Cloudbees',
    'Codelathe',
    'ConsenSys',
    'Crossover',
    'DataDog',
    'DataRobot',
    'Deel',
    'Doist',
    'Dribbble',
    'DuckDuckGo',
    'Elastic',
    'End Point Dev',
    'Envato',
    'Eyeo',
    'Fireflies.ai',
    'Gatsby',
    'Genuitec',
    'Ghost',
    'GitLab',
    'Gradle',
    'Grafana Labs',
    'Help Scout',
    'Hubstaff',
    'Igalia',
    'Jackson River',
    'Jitbit Software',
    'Kentik',
    'Kraken',
    'Lullabot',
    'madewithlove',
    'MailerLite',
    'MarsBased',
    'Mobile Jazz',
    'Mozilla',
    'Netlify',
    'Olark',
    'Original Eight',
    'Percona',
    'Platform.sh',
    'Pythian',
    'RedHat',
    'Redox',
    'Remote',
    'SaasGroup',
    'ScyllaDB',
    'Shogun',
    'Shopify',
    'Sonatype',
    'Sourcegraph',
    'Spotify',
    'Square',
    'Superside',
    'Time Doctor',
    'Toggl',
    'Toptal',
    'Turing',
    'Upwork',
    'Vercel',
    'Wikimedia',
    'X-team',
    'Xapo',
    'XWP',
    'You Need A Budget',
    'Zapier',
    'Zyte']

greenhouse_companies = [
    'affirm',
    'consensys',
    'netlify',
    'cloudbeds',
    'elastic',
    'datadog',
    'turing',
    'wikimedia',
    'upwork',
    'gradle',
    'vercel',
    'airbnb',
    'gitlab',
    'mozilla',
    'saasgroup',
    'kentik',
    'canonical',
    'eyeo',
    'ghost',
    'block',
    'remote' ]

skills_list = []
