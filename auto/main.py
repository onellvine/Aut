from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome(executable_path="./chromedriver")
home_url = 'https://gainweb.org/submit.php'
driver.get(home_url)

driver.find_elements_by_css_selector("input[type='radio'][value='2']")[0].click()

title = driver.find_element_by_xpath("//*[@id='TITLE']")
title.send_keys('Hello world')

site_url = driver.find_element_by_xpath("//*[@id='URL']")
site_url.send_keys('https://mail.google.com')

category = Select(driver.find_element_by_xpath("//*[@id='CATEGORY_ID']"))
category.select_by_value('849')

description = driver.find_element_by_xpath("//*[@id='DESCRIPTION']")
description.send_keys("The quick brown fox jumped over the lazy dog.")

owner_name = driver.find_element_by_xpath("//*[@id='OWNER_NAME']")
owner_name.send_keys('Rose')

owner_email = driver.find_element_by_xpath("//*[@id='OWNER_EMAIL']")
owner_email.send_keys('onellvine@gmail.com')

meta_desc = driver.find_element_by_xpath("//*[@id='META_DESCRIPTION']")
meta_desc.send_keys("Lorem issym dolor")

meta_key_words = driver.find_element_by_xpath("//*[@id='META_KEYWORDS']")
meta_key_words.send_keys("Hello world Program")

driver.find_element_by_name('AGREERULES').click()

sleep(2)

driver.get_screenshot_as_file('submission_1.png')

sleep(2)

continue_btn = driver.find_element_by_xpath("//*[@id='submitForm']/table/tbody/tr[13]/td/input").click()

