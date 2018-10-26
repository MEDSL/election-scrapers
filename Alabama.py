from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



if __name__== "__main__":
	path = "ENTER_PATH"
	options = webdriver.ChromeOptions() 
	options.add_argument("download.default_directory=".format(path))
	driver = webdriver.Chrome() 
	url = "http://www2.alabamavotes.gov/electionnight/countyResultsByContest.aspx?cid=04&ecode=1001000"
	driver.get(url)
	wait = WebDriverWait(driver, 10)
	wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='hlnkExportData']"))).click()
	
	