# -*- coding: utf-8-sig -*-
import json
import re
import requests, lxml
from config import URL, headers_generator, browser, browser_service, chrome_webdriver_path
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


def get_info_url(url):
    return requests.get(url=url, headers=headers_generator.generate())


def wait_element(browser, delay_seconds=1, by=By.TAG_NAME, value=None):
    return WebDriverWait(browser, delay_seconds).until(
        expected_conditions.presence_of_element_located((by, value))
    )


def get_info_vacancy():
    info_vacancy = []
    browser.get(URL)
    all = wait_element(browser, 3, By.CLASS_NAME, "vacancy-serp-content")
    vacancy_all = all.find_elements(By.ID, "a11y-main-content")
    for vacancy in vacancy_all:
        url_all = vacancy.find_elements(By.CLASS_NAME, 'serp-item__title')
        for u in url_all:
            url = u.get_attribute('href')
            info = BeautifulSoup(get_info_url(url).text, "lxml")
            descr = info.find('div', class_='g-user-content').text
            if re.search(r'Django', descr) or re.search(r'Flask', descr):
                salary_element = info.find('div', {'data-qa': 'vacancy-salary'})
                salary = salary_element.text.strip() if salary_element else "Зарплата не указана"
                if info.find('span', {'data-qa': 'vacancy-view-raw-address'}) is not None:
                    address_element = info.find('span', {'data-qa': 'vacancy-view-raw-address'}).text
                else:
                    address_element = info.find('p', {'data-qa': 'vacancy-view-location'}).text
                # address = address_element.text.strip() if address_element else "Адрес не указан"
                company = info.find('span', {'data-qa': 'bloko-header-2'}).text
                title = info.find('h1', class_='bloko-header-section-1').text
                # print(title, '\n', url, '\n', company, '\n', address_element, '\n', salary)
                info_vacancy.append({
                    'vacancy': title,
                    'url': url,
                    'company': company,
                    'salary': salary,
                    'sity': address_element
                })
    return info_vacancy


if __name__ == '__main__':
    info_vacancy = get_info_vacancy()
    with open('files/log.json', 'a', encoding='utf-8-sig') as file:
        json.dump(info_vacancy, file)

