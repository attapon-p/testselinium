from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://mooc.chula.ac.th/courses/151"

driver = webdriver.Chrome()
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
print(i)
print(driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div/div/div[2]/div[1]/div[1]/button['+str(i)+']/span').text)

print(driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div/div/div[2]/div[3]/div[1]/div[2]/div/div[1]/div[2]/span').text)

