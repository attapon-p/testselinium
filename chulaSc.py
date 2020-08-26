from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

def Travel(urlss):
    url = urlss

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)

    driver.get(url)

    # check status of course
    if not('none' in (driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div/div/div[2]/div[1]/div[1]/button[1]').get_attribute('style'))):
        i = 1
    elif not('none' in (driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div/div/div[2]/div[1]/div[1]/button[2]').get_attribute('style'))):
        i = 2
    elif not('none' in (driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div/div/div[2]/div[1]/div[1]/button[3]').get_attribute('style'))):
        i = 3
    else:
        i = 0 # for error

    # show status of course
    # Loop for scrape name, begin date, finish date
    print(url)
    print(driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div/div/div[2]/div[1]/div[1]/div/h1').text)
    if i != 0:
        print(i)
        print(driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div/div/div[2]/div[1]/div[1]/button['+str(i)+']/span').text)
    else:
        print('')
        print('')

    print(driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div/div/div[2]/div[3]/div[1]/div[2]/div/div[1]/div[2]/span').text)

    driver.close()




##################################################    

url = 'https://mooc.chula.ac.th/courses'

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)

driver.get(url)

while(True):
    try:
        driver.implicitly_wait(5)
        driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div/div/div[3]/button/span').click()
        driver.implicitly_wait(5)
        
    except:
        break


# Store each subjedt    
list_of_subject = []
for a in driver.find_elements_by_xpath('//*[@id="app"]/div/main/div/div/div/div[3]/div[2]/a'):
    list_of_subject.append(a.get_attribute('href'))

# Cut off series link
for i in list_of_subject:
    if 'serie' not in i:
        Travel(i)



driver.quit()





    
    


