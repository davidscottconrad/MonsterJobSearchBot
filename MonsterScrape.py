import math
import os
import sys
import time
import mysql.connector

import functools 
import operator

import requests
from selenium import webdriver
from bs4 import BeautifulSoup

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


"""
URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=California'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
print(results.prettify())

job_elems = results.find_all('section', class_='card-content')

for job_elems in job_elems:
    title_element = job_elems.find('h2', class_='title')
    company_element = job_elems.find('div', class_='company')
    location_element = job_elems.find('div', class_='location')
    if None in (title_element, company_element, location_element):
        continue
    print(title_element.text.strip(), company_element.text.strip(), location_element.text.strip(), end='\n__________________________________________________________________________________________________________________\n')
"""
url_link = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=California'
def page_loader(url_link): #Opens a URL and Scrolls to the bottom of an infinite scroll page
    driver = webdriver.Chrome('C:\Program Files\chromedriver')
    driver.get(url_link);
    
    time.sleep(2)
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(1)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                # If heights are the same it will exit the function
                break   
            last_height = new_height
#load_more = find_element_by_xpath('//*[@id="loadMoreJobs"]').click()
    #time.sleep(5)
    
    url1 = driver.current_url #gets URL after exiting loop and finished scrolling
    return url1
    driver.quit()

def soup_results(URL):
    
    #grabs everything on the page, sends it back
    page = requests.get(URL)    
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='ResultsContainer')
    job_elems = results.find_all('section', class_='card-content')
    print("the type of job_elems is ", type(job_elems))
    return job_elems

def URL_Array_Grab(URL, k): 
    driver1 = webdriver.Chrome('C:\Program Files\chromedriver')
    driver1.get(URL)
    time.sleep(1)
    URL_Array = [' ', ' ']
    for k in range(3, k):
        
        h = str(k)

        strMyXpath = "//*[@id='SearchResults']/section[" + h + "]"
        #strMyXpath = "//*[@id='SearchResults']/section[4]"
        #driver1.maximize_window()
        #mainmenu = driver1.find_element_by_xpath(strMyXpath)

        #driver1.find_element_by_id("SearchResults").click()

        #action = ActionChains(driver1)
        #action.
        g = k-2
        p = str(g * 103)
        inside_script = "window.scrollBy(0, " + p + ");"
        #action = ActionChains(driver1)
        #action.move_to_element(driver1.find_element_by_xpath(strMyXpath)).perform()
        #time.sleep(3)
        #action.move_to_element_with_offset(driver1.find_element_by_xpath(strMyXpath), 0, 0)
        
        #action.perform()
        ###########
        #element_to_hover_over = driver1.find_element_by_xpath(strMyXpath)

        '''action.move_to_element(element_to_hover_over).click_and_hold().move_by_offset(0,103).release(element_to_hover_over).build().perform()'''
        #hover.perform()
        time.sleep(3)
        '''try:
            element = WebDriverWait(driver1, 10).until(
            EC.presence_of_element_located((By.XPATH, strMyXpath))
        )
        finally: '''
        driver1.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver1.execute_script("window.scrollTo(0, 0);")
        driver1.execute_script(inside_script)
        
        #driver1.execute_script("arguments[0].click();", strMyXpath)
        
        #wait = WebDriverWait(driver1, 20)
        #wait.until(ExpectedConditions.invisibilityOfElementLocated(loadingImage))
        #element = wait.until(EC.element_to_be_clickable((By.XPATH, strMyXpath)))
    
        driver1.find_element_by_xpath(strMyXpath).click()#send_keys('\n')
        
        
        time.sleep(3)

       
        ##########
        #x = mainmenu.location
        #print(x)
        #mainmenu.scrollTo()
        #driver1.
        #move_to_element_with_offset(mainmenu, 0, 0).perform()
        #moveToElement
        #p = 103 * k
        #driver1.execute_script("window.scrollBy(0,103);")

        time.sleep(1)
        #actions.moveToElement(mainmenu)
        #actions.perform()
        #driver1.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});", mainmenu)
        #time.sleep(30)
        #driver1.implicitly_wait(10)
        #wait = WebDriverWait(driver, 10)
        #element2 = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))

        
        #submenu = wait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Introduction")))
        #submenu.click()

        URL_Array.insert(k, driver1.current_url)
        time.sleep(1)
        driver1.execute_script("window.history.go(-1)")
        time.sleep(1)

    driver1.quit()

    #grabs everything on the page, sends it back
    page = requests.get(URL)     
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='ResultsContainer')
    job_elems = results.find_all('section', class_='card-content')
    return job_elems        




def soup_printer(job_elems):
    i = 0
    for job_elems in job_elems:
        i = i + 1
        title_element = job_elems.find('h2', class_='title')
        company_element = job_elems.find('div', class_='company')
        location_element = job_elems.find('div', class_='location')
        if None in (title_element, company_element, location_element):
            continue
        print(i, '\n', title_element.text.strip(), '\n',company_element.text.strip(), '\n', location_element.text.strip(), end='\n__________________________________________________________________________________________________________________\n')
    return i

def MySQL_Insert(job_elems):

    con = mysql.connector.connect( #connecting to databse
        host = "127.0.0.1",
        user = "root",
        password = "!Ad@etrl1",
        database = "JobDatabase",
        port = 3306
    )
    print(con)

    cur = con.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS JobDatabase")
    cur.execute("CREATE TABLE IF NOT EXISTS JobTable (JobTitle VARCHAR(255), JobCompany Varchar(255), JobLocation Varchar(255))")
    #cur.execute("ALTER TABLE IF NOT EXISTS JobTable ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
    #cur.execute("SHOW DATABASES")
    #cur.execute("SHOW TABLES")

    #for x in cur: 
    #    print(x)
    #rows = cur.fetchall() #fetches all rows present
    #print("\n\n\n\n")
    #print(rows)
    
    
    
    for job_elems in job_elems:
        
        title_element = job_elems.find('h2', class_='title')
        company_element = job_elems.find('div', class_='company')
        location_element = job_elems.find('div', class_='location')

        #title_element_str = title_element.text.strip()
        #company_element_str = company_element.text.strip()
        #location_element_str = location_element.text.strip()
        if None in (title_element, company_element, location_element):
            continue

        sql = "INSERT INTO JobTable (JobTitle, JobCompany, JobLocation) VALUES (%s, %s, %s)"
        val = (title_element.text.strip(), company_element.text.strip(), location_element.text.strip())
        cur.execute(sql, val)
        con.commit()
        
    cur.execute("SELECT * FROM JobTable")
    mytableresult = cur.fetchall()
    for x in mytableresult:
        print(x)
        
def convertTuple(tup): #converts tuple to String by concatenating all char in tuple to string
    print("_____________________________")
    
    str = functools.reduce(operator.add, (tup)) 
    print("INSIDE CONVERT TUPLE")
    
    print("_____________________________")
    return str
    
j = 0
url_link = page_loader(url_link)
soup_information = soup_results(url_link)
j = soup_printer(soup_information)
soup_information = URL_Array_Grab(url_link, j)

#MySQL_Insert(soup_information)


