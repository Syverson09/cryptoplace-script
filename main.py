from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os, time

user_email = "Your Email HERE" #input("Enter CryptoPlace Email: ")
user_password = "Your Password Here" #input("Enter CryptoPlace Password: ")

while True:	
	cwd = os.getcwd()
	path = cwd + "/chromedriver.exe"

	options = webdriver.ChromeOptions()
	options.add_argument("--headless")

	driver = webdriver.Chrome(path, chrome_options=options)
	
	driver.get("https://cryptoplace.cloud/cabinet")
	os.system("clear")
	print("================================================================")
	print("\x1b[0;30;42m" + "          Cryptoplace Auto Claim Bonus by PHC-MakiBoT            " + "\x1b[0m")
	print("================================================================")
	print("Loading Page . . .")

	element = driver.find_element(By.XPATH, "//div[@class=\"col-11 col-md-4 col-xl-3 d-flex flex-column align-items-center\"]//a[@class=\"origin-color go\"]")
	actions = ActionChains(driver).move_to_element(element).perform()

	for i in range(3):
		print("Moving to elements in " + str(i), end="\r")
		time.sleep(1)

	element.click()

	for i in range(3):
		print("Toggle login in " + str(i), end="\r")
		time.sleep(1)

	email_box = driver.find_element_by_name("username").send_keys(str(user_email))
	password_box = driver.find_element_by_id("InputPassword").send_keys(str(user_password))
	print("Putting Information. . .")

	submit_button = driver.find_element(By.XPATH, "//form[@id=\"login\"]//button[@class=\"btn btn-style-form w-100\"]").click()

	for i in range(3):
		print("Signing In on " + str(i), end="\r")
		time.sleep(1)

	driver.get("https://cryptoplace.cloud/cabinet/bonuses")

	for i in range(3):
		print("Claiming bonuses in " + str(i), end="\r")
		time.sleep(1)

	claim = driver.find_element(By.XPATH, "//button[@id=\"get-bonus\"]").click()


	for i in range(3):
		print("Succesfully claim in " + str(i), end="\r")
		time.sleep(1)


	navbar = driver.find_element(By.XPATH, "//nav[@class=\"navbar navbar-expand-lg navbar-light w-100 px-sm-0\"]//button[@data-toggle=\"collapse\"]").click()
	logout_button = driver.find_element_by_link_text("Exit").click()

	for i in range(3):
		print(str(i))
		time.sleep(1)

	for i in range(3):
		print("Succesfull logout in " + str(i), end="\r")
		time.sleep(1)

	driver.quit()

	os.system("clear")

	print("================================================================")
	print("\x1b[0;30;42m" + "          Script Cracked & Translated by PHC-MakiBoT            " + "\x1b[0m")
	print("================================================================")

	for i in range(1860):
		print(str(i) + " Seconds until next claim!", end="\r")
		time.sleep(1)
