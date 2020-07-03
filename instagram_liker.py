from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

username = input("Enter your username: ")
password = input("Enter your password: ")
target = input("Enter the username of the account you wanna like: ")
counter = 2

driver = webdriver.Chrome()
driver.get("https://instagram.com")
sleep(5)
driver.find_element_by_name("username").send_keys(username)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_name("password").send_keys(Keys.ENTER)
sleep(3)

# Click "not now" if the dialog box comes up 
try:
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
    
except NoSuchElementException as e:
    print(f"No Dialog Box")
sleep(3)
# turn off Notification Popup 
try:
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()

except NoSuchElementException as e:
    print(f"No Popup :D")
sleep(3)

#search anything 
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div/span[1]').click()
search = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search.send_keys(target)
sleep(2)
#click the 1st search result 

search_results = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]')
search_results.click()
sleep(3)
#first image Like
def highlights():
    #path = '//*[@id="react-root"]/section/main/div/div[1]/div'
    path = '//*[@id="react-root"]/section/main/div/div[1]/div/div/div/ul/li[3]'
    try:
        driver.find_element_by_xpath(path)
        return True
    except NoSuchElementException:
        return False

if highlights()==True:
    counter=counter+1   
first_thumbnail = driver.find_element_by_xpath(f'//*[@id="react-root"]/section/main/div/div[{counter}]/article/div[1]/div/div[1]/div[1]/a/div')
first_thumbnail.click()
    
sleep(3)
try:
    while True:
        #Pressing Like 
        like_button = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
        like_button.click()
        #Next Image 
        driver.find_element_by_link_text('Next').click()
        sleep(5)
        
except NoSuchElementException:
        print("No More Post Left to Like :-P")

