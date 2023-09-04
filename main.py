from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")

CHROME_DRIVER_PATH = "/app/chromedriver"
#SERVICE = Service(CHROME_DRIVER_PATH)
DRIVER = webdriver.Chrome(options=options)

class Getinfo:
    def getTitle(self):
        DRIVER.get("https://www.parks.org.il/newsflash/")
        mivzak = DRIVER.find_elements(By.CLASS_NAME, "article_content")
        for i in mivzak:
            print(i.text)
info = Getinfo()
info.getTitle()
