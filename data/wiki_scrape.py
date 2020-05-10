# #import wikipedia as wiki
# import wikipediaapi as wiki_api
#
# wiki = wiki_api.Wikipedia('en')
# page = wiki.page('COVID-19 pandemic in Karnataka')
# print(page.exists())
# print(page.title, page.text, page.categories, page.sections)
#
# import requests
# from bs4 import BeautifulSoup
#
# URL = "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Karnataka#Cases"
#
# res = requests.get(URL)
# print(res)
# soup = BeautifulSoup(res,'lxml')
#
# for items in soup.find('table', class ='wikitable sortable plainrowheaders jquery-tablesorter').find_all('tr')[1::1]:
#     data = items.find_all(['th','td'])
#     try:
#         country = data[0].a.text
#         title = data[1].a.text
#         name = data[1].a.find_next_sibling().text
#     except IndexError:pass
#     print("{}|{}|{}".format(country,title,name))

import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from urllib.request import urlopen

url = urlopen('https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Karnataka#Cases')
soup = BeautifulSoup(url, 'html.parser')
table = soup.find('table', {"class": "wikitable sortable plainrowheaders"})

# with open("./Html_Output", "w") as file:
#     i = 0
#     for lines in soup.prettify():
#
#         try:
#             file.write(lines)
#         except Exception as e:
#             i += 1
#             print("Error =  ", i, " e")
#             pass


def print_as_table(d):

    print("-------------------------------------------\n")
    print("Key\t\t\t\t\tValue")
    for key in d:
        print("{:<15}:{:>8}".format(key, d[key]))



district = {}
age = {}

gender = {}
ri4 = 0
ri6 = 0
ri5 = 0
i = 0
err = 0

df = pd.DataFrame(columns=["district", "age", "gender"])

for row in table.find_all('tr'):
    i += 1
    if i == 1:
        continue

    if row.find('td'):
        try:
            r = list(map(lambda x: x.text, row.find_all('td')))

            if len(r) == 4:
                d_i = 2
                a_i = 3

            elif len(r) == 5:
                if r[3][0] in ['F', 'M'] and r[3][1].isdigit():
                    #print(r[0])
                    a_i = 3
                    d_i = 2
                else:
                    d_i = 3
                    a_i = 4

            elif len(r) == 6:

                a_i = 4
                d_i = 3

            else:
                print("Unknown length = ", len(r))

            dist = r[d_i].strip()
            age_ = r[a_i][1:].strip()
            gender_ = r[a_i][0].strip()

            district[dist] = district[dist] + 1 if dist in district else 1
            # if gender_ == '[':
            #     print(r)
            age[age_] = age[age_] + 1 if age_ in age else 1
            gender[gender_] = gender[gender_] + 1 if gender_ in gender else 1

            df = df.append({'district': dist,'age':age_, "gender":gender_}, ignore_index=True)
        except Exception as e:
            print(r)
            err += 1
            print("ERROR : ", err, "   ", e)

print_as_table(district)
print_as_table(age)
print_as_table(gender)
print(df)