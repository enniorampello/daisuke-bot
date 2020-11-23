from date_format import get_schedule
from scraper import Scraper
from lib import *


class Polito(Scraper):
    
    def __init__(self):
        Scraper.__init__(self)
        self.login()
        self.num_estm = 0
        self.num_sap = 0
        self.num_os = 0
        self.num_cn = 0

    def login(self):
        self.driver.get('https://idp.polito.it/idp/x509mixed-login')
        self.wait.until(presence_of_element_located((By.ID, 'j_username')))
        self.driver.find_element_by_id('j_username').send_keys(get_username())
        self.driver.find_element_by_id('j_password').send_keys(get_password())
        sleep(1)
        self.driver.find_element_by_id('usernamepassword').click()
        self.wait.until(presence_of_element_located((By.XPATH, '//*[@id="table_portali"]/div[2]/div/a')))
        self.driver.find_element_by_xpath('//*[@id="table_portali"]/div[2]/div/a').click()
        try:
            popup = self.driver.find_element_by_xpath('//*[@id="myModalRemindAbb"]/div/div/div[3]/a[4]')
        except NoSuchElementException:
            pass
        else:
            popup.click()
        sleep(5)

    def get_vc_page(self, sub: str):
        self.driver.find_element_by_xpath(subject_paths.get(sub)).click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/nav/div[2]/ul[2]/li[5]/a').click()
        sleep(2)
        if sub == 'estm':
            self.get_estm_vc()
        elif sub == 'sap':
            self.get_sap_vc()
        elif sub == 'os':
            self.get_os_vc()
        elif sub == 'cn':
            self.get_cn_vc()
        sleep(2)

    def get_os_vc(self):
        self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[4]/div/div[2]/angular-filemanager/div/div[2]/div/div[1]/ul/li/ul/li[3]/a').click()

    def get_estm_vc(self):
        self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/ul/li[2]/a/span').click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div[3]/div[2]/div[2]/div/div[2]/angular-filemanager/div/div[2]/div/div[1]/ul/li/ul/li[2]/a').click()
    
    def get_sap_vc(self):
        self.driver.find_element_by_xpath('//*[@id="portlet_corso_container"]/div[1]/div/ul/li[2]/a/span').click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div[3]/div[2]/div[2]/div/div[2]/angular-filemanager/div/div[2]/div/div[1]/ul/li/ul/li/a').click()
    
    def get_cn_vc(self):
        self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[4]/div/div[2]/angular-filemanager/div/div[2]/div/div[1]/ul/li/ul/li[3]/a').click()
    
    def check(self):
        if datetime.today().weekday == 5:
            return
        lectures = get_schedule()
        for sub in lectures.index:
            print('sub: ' + sub)
            vals = lectures.loc[sub]
            self.get_vc_page(sub)
            i = 1
            while True:
                print('reading...')
                try:
                    lesson_date = self.driver.find_element_by_xpath(f'/html/body/div[6]/div/div/div[3]/div/div[1]/div[1]/nav/div/div[2]/div/ul/li[{i}]/span').text
                    print(lesson_date)
                    i += 1
                except NoSuchElementException:
                    break
            self.driver.get('https://didattica.polito.it/pls/portal30/sviluppo.pagina_studente_2016.main') #portale main page
            sleep(4) #replace with wait

    def run():
        pass 

if __name__ == '__main__':
    poli = Polito()
    poli.check()