import requests
from fake_headers import Headers
from bs4 import BeautifulSoup
from pprint import pprint
import re

HOST = 'https://spb.hh.ru/search/vacancy?text=python+django+Flask&salary=&ored_clusters=true&area=1&area=2&hhtmFrom=vacancy_search_list&hhtmFromLabel=vacancy_search_line'


def get_headers():
    return Headers(browser='chrome', os='win').generate()


SOURCE = requests.get(HOST, headers=get_headers()).text
bs = BeautifulSoup(SOURCE, features='lxml')

articles = bs.find_all(class_='vacancy-serp-item-body')

vacancy_list = []
for article in articles:
    link = article.find('a')['href']
    salary = article.find('span', class_='bloko-header-section-2')
    try:
        salary = salary.text
    except:
        salary = 'Зарплата не указана'
    company = article.find('a', class_='bloko-link bloko-link_kind-tertiary').text
    city = article.find('div', {'data-qa': 'vacancy-serp__vacancy-address'}).text
    vacancy_list.append({
        'Ссылка': link,
        'Зарплата': salary,
        'Компания': company,
        'Город': city,

    })
pprint(vacancy_list)