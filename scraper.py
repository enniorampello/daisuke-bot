from lib import Chrome, ChromeOptions, WebDriverWait, get_chromedriver_path, sleep

class Scraper():
    options = ChromeOptions()
    options.add_argument('--headless')
    driver = Chrome(get_chromedriver_path(), options=options)
    wait = WebDriverWait(driver, 20)

    def __init__(self) -> None:
        pass
    
    def refresh(self):
        self.driver.refresh()
        sleep(5)
        pass