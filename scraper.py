from lib import Chrome, ChromeOptions, WebDriverWait, get_chromedriver_path, sleep

class Scraper:

    def __init__(self):
        self.options = ChromeOptions()
        #self.options.add_argument('--headless')
        self.driver = Chrome(get_chromedriver_path(), options=self.options)
        self.wait = WebDriverWait(self.driver, 20)
    
    def refresh(self):
        self.driver.refresh()
        sleep(5)