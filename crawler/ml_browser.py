from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

class BrowserML:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-web-security")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument("--memory-pressure-off")
        self.chrome_options.add_argument("--ignore-certificate-erros")

        self.drive =webdriver.Chrome(options=self.chrome_options) 

    def execute_command(self,query):
        self.drive.get(f"https://www.mercadolivre.com.br/{query.replace(' ','-')}")

        time.sleep(5)

        html = self.drive.page_source()
        self.drive.quit()

        soup = BeautifulSoup(html, "html.parser")

        results = soup.find_all("div", class_="ui.serach-results")

    def transform_df(self):
        pass
 