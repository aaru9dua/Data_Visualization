from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import time
import random
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import re


# Selenium 4:

from selenium import webdriver

# Starting/Stopping Driver: can specify ports or location but not remote access
from selenium.webdriver.chrome.service import Service as ChromeService


# Manages Binaries needed for WebDriver without installing anything directly
from webdriver_manager.chrome import ChromeDriverManager
option= webdriver.ChromeOptions()


# Going undercover:
option.add_argument("--incognito")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                         options=option)


# Allows searchs similar to beautiful soup: find_all
from selenium.webdriver.common.by import By

# Try to establish wait times for the page to load
from selenium.webdriver.support.ui import WebDriverWait

# Wait for specific condition based on defined task: web elements, boolean are examples
from selenium.webdriver.support import expected_conditions as EC

# Used for keyboard movements, up/down, left/right,delete, etc
from selenium.webdriver.common.keys import Keys

# Locate elements on page and throw error if they do not exist
from selenium.common.exceptions import NoSuchElementException




# Set the job title and location
job_ = 'Game+Developer'
location = 'United States'
entry_level = 'entry'

# Construct the URL
url = f'https://www.indeed.com/jobs?q={job_}&l={location}&explvl={entry_level}'


# Open the URL
driver.get(url)


job_page = driver.find_element(By.ID,"mosaic-jobResults")
jobs = job_page.find_elements(By.CLASS_NAME,"job_seen_beacon") 




job_titles=[]
job_links=[]
job_ids=[]
job_companies=[]
job_locations=[]
job_salary=[]
job_jd=[]

# # The next button is defined.
# next_button_xpath = '//*[@id="jobsearch-JapanPage"]/div/div/div[5]/div[1]/nav/div[6]/a'

job_page = driver.find_element(By.ID,"mosaic-jobResults")
jobs = job_page.find_elements(By.CLASS_NAME,"job_seen_beacon")
num_jobs_scraped = 0



for i in range(0,25):
    driver.get(url.format(job_,location,i*10))
    
    
    time.sleep(2)

    job_page = driver.find_element(By.ID,"mosaic-jobResults")
    jobs = job_page.find_elements(By.CLASS_NAME,"job_seen_beacon") 
    for jj in jobs:
        
        job_title = jj.find_element(By.CLASS_NAME, "jobTitle").text
        job_titles.append(job_title)
        
        job_links.append(jj.find_element(By.CSS_SELECTOR,"a").get_attribute("href"))
        job_ids.append(jj.find_element(By.CSS_SELECTOR,"a").get_attribute("id"))
        
        
        company_name = jj.find_element(By.CSS_SELECTOR, ".css-1x7z1ps").text
        job_companies.append(company_name)

        # Extract job location
        location = jj.find_element(By.CSS_SELECTOR, ".css-t4u72d").text
        job_locations.append(location)
        
        #location = jj.find_element(By.CLASS_NAME, "companyLocation").text
        #job_locations.append(location)
        
        
        try: 
            job_salary.append(jj.find_element(By.CLASS_NAME,"salary-snippet-container").text)

        except: 
            try: 
                job_salary.append(jj.find_element(By.CLASS_NAME,"estimated-salary").text)
            except:
                job_salary.append(None)
                
                
        time.sleep(1) 
        # Click on the job listing to view the details
        jj.click()
        time.sleep(5)  # Add a short delay to allow the page to load
        # Switch to the right pane
      
        try:
            job_jd.append(driver.find_element(By.ID, "jobDescriptionText").text)
        except:
            job_jd.append(None)
            

        # Print or store the information
        print(f"Job Title: {job_title}")
        print()
        
#         # We press the next button. 
#         driver.find_element(By.XPATH,next_button_xpath).click()


        # The button element is updated to the 7th button instead of the 6th.
#         next_button_xpath = '//*[@id="jobsearch-JapanPage"]/div/div/div[5]/div[1]/nav/div[7]/a'
#         print(f"Company Name: {company_name}")
#         print(f"Location: {location}")


job_name_list = ['Game Developer']*len(job_titles)
level=['entry']*len(job_titles)
indeed_df = pd.DataFrame({
    'job_id': job_ids,
    'job_type': job_name_list,
    'job_title': job_titles,
    'company_name': job_companies, 
    'company_location': job_locations,
    'job_description': job_jd,
    'job_link': job_links,
    'job_salary': job_salary,
    'ExperienceLevel':level
   
})

job="Game_Developer"
indeed_df.to_csv(f"{job}"+"_full_"+"_26.04.23.csv")