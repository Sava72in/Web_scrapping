# -*- coding: utf-8 -*-
import json

import requests, lxml

from config import URL, headers_generator
from bs4 import BeautifulSoup


def get_info_url(url):
    return requests.get(url=url, headers=headers_generator.generate())


main_soup = BeautifulSoup(get_info_url(URL).text, "lxml")
vacancy_blok = main_soup.find('main', class_='vacancy-serp-content')
vacancy_all = vacancy_blok.find('div', id='a11y-main-content')
vacancy = vacancy_all.find_all('div', class_='serp-item')
for i in vacancy:
    v = i.find('div', class_='vacancy-serp-item-body__main-info')
    name_vacancy = v.find('a', class_='serp-item__title').text
    href = v.find('a', class_='serp-item__title')['href']
    main_soup = BeautifulSoup(get_info_url(href).text, 'lxml')
    # descr = main_soup.find('div', class_='g-user-content').text.find('Python')
    print(name_vacancy, href)
