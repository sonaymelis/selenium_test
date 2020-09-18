from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser=webdriver.Chrome("/Users/Sonay/Desktop/chromedriver")

browser.get("https://www.linkedin.com/")
browser.fullscreen_window()
time.sleep(2)

login=browser.find_element_by_xpath("/html/body/nav/a[3]")
login.click()
time.sleep(2)

email=browser.find_element_by_css_selector("#username")
password=browser.find_element_by_css_selector("#password")

email.send_keys("deneme@deneme.com")
password.send_keys("12345")

login_button=browser.find_element_by_css_selector("#app__container > main > div:nth-child(2) > form > div.login__form_action_container > button")
login_button.click()
time.sleep(2)


search_bar=browser.find_element_by_xpath("//*[@id='ember16']/input")
search_bar.send_keys("#python")
search_bar.send_keys(Keys.RETURN)
time.sleep(2)


contact=browser.find_element_by_xpath("//*[@id='ember23']")
contact.click()
time.sleep(5)


contact_button=browser.find_element_by_class_name("mn-community-summary__entity-info")
contact_button.click()
time.sleep(2)

for i in range(1,3):
	browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
	time.sleep(1)

followers=browser.find_elements_by_class_name("mn-connection-card__details")
followerList=[]

for follower in followers:
	followerList.append(follower.text)

with open("follower.txt","w",encoding="UTF-8") as file:
	for follower in followerList:
		file.write(follower)
		file.write("\n")
		file.write("\n")

time.sleep(5)

browser.quit()










