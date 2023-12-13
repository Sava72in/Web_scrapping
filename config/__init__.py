from fake_headers import Headers
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

URL = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'
headers_generator = Headers(os="win", browser="firefox")
chrome_webdriver_path = ChromeDriverManager().install()
browser_service = Service(executable_path=chrome_webdriver_path)
options = Options()
options.add_argument("--headless")
browser = Chrome(service=browser_service, options=options)




