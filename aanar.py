from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from PIL import ImageGrab

driver = webdriver.Chrome(executable_path="./chromedriver")

home_urls = ['https://www.businesswritingservices.org/buy-business-research-proposal', 'https://www.businesswritingservices.org/buy-business-thesis', 'https://www.businesswritingservices.org/buy-business-dissertation-paper', 'https://www.businesswritingservices.org/buy-business-thesis-proposal', 'https://www.businesswritingservices.org/buy-business-coursework']
titles = ['Buy Business Research Proposal', 'Buy Business Thesis', 'Buy Business Dissertion Paper', 'Write My Business Research Summary', 'Buy Business Coursework']
descriptions = [
    'We will deliver a business research proposal by best writers when you seek our service. Our writers use persuasive language and present facts to support your reasons for choosing your project.',
    'Our service is comprehensive to help students through all aspects of writing a thesis. We help with choosing an appropriate topic, researching from different sources, and writing the paper according to guidelines by your institution.',
    'Businesswritingservices.org has become the top writer in writing a dissertation as we specialize in writing business assignments. It is only certified writers who work on buying a dissertation online orders.',
    'The experience by BusinessWritingServices.org is enough reason to buy a business thesis proposal online. We have for more than five years been writing theses and their proposals getting a complete understanding of research areas as well as gaps in business.',
    'Our choice to write business coursework is to provide the best writing service to our clients. We will assign you a seasoned writer with a complete understanding of this crucial assignment when we receive your request you buy business coursework online.'
    ]
meta_keywords = ['Buy Business Research Proposal', 'Writing Business Thesis', 'Writing a Dissertion Paper', 'Business Thesis Proposal', 'Write Business Coursework']

def ArithSum(str_arith):
    digits = [i for i in str_arith if i.isdigit()]
    s = 0 # sum
    for d in digits:
        s += int(d)
    return s


for i in range(len(home_urls)):
    home_url = 'http://ananar.com/submit.php?c=220&LINK_TYPE=1'
    driver.get(home_url)

    title = driver.find_element_by_xpath("//*[@id='TITLE']")
    title.send_keys(titles[i])

    site_url = driver.find_element_by_xpath("//*[@id='URL']")
    site_url.send_keys(home_urls[i])

    description = driver.find_element_by_xpath("//*[@id='DESCRIPTION']")
    description.send_keys(descriptions[i])

    owner_name = driver.find_element_by_xpath("//*[@id='OWNER_NAME']")
    owner_name.send_keys('Rose')

    owner_email = driver.find_element_by_xpath("//*[@id='OWNER_EMAIL']")
    owner_email.send_keys('onellvine@gmail.com')

    meta_desc = driver.find_element_by_xpath("//*[@id='META_DESCRIPTION']")
    meta_desc.send_keys("Professional Business Writing Services including academic, business and personal writing in all business topics")

    meta_key_words = driver.find_element_by_xpath("//*[@id='META_KEYWORDS']")
    meta_key_words.send_keys(meta_keywords[i])

    arithmetic = driver.find_element_by_css_selector("font[style='font-weight: bold; font-size: 14pt; color: red; margin-right: 10px;']").text
    answer = driver.find_element_by_xpath('//*[@id="DO_MATH"]')
    answer.send_keys(ArithSum(arithmetic))    

    driver.find_element_by_name('AGREERULES').click()

    driver.find_element_by_xpath("//*[@id='submitForm']/table/tbody/tr[12]/td/input").click()

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'msg')))
    sleep(10)
    ss = ImageGrab.grab()
    ss.save(f'aanar_{i}.png')

driver.quit()

