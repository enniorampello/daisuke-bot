from scraper import Scraper
from lib import *


class Polito(Scraper):
    material_urls = {
        'sap': 'https://didattica.polito.it/portal/pls/portal/sviluppo.pagina_corso.main?t=3&p_sottopagina=VC_6718',
        'os': 'https://didattica.polito.it/portal/pls/portal/sviluppo.pagina_corso.main?t=3&p_sottopagina=VC_7181',
        'estm': 'https://didattica.polito.it/portal/pls/portal/sviluppo.pagina_corso.main?t=3&p_sottopagina=VC_6875',
        'cn': 'https://didattica.polito.it/portal/pls/portal/sviluppo.pagina_corso.main?t=3&p_sottopagina=VC_6577'
    }
    
    def __init__(self, parameter_list):
        Scraper.__init__(self)
        self.polito_login()
        pass

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

    

