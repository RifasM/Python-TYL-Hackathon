from bs4 import BeautifulSoup
import urllib.request
import json
import re
import ast

url = "https://covid19.karnataka.gov.in/covid-dashboard/dashboard.html"

page = urllib.request.urlopen(url)

soup = BeautifulSoup(page, 'html.parser')
# print(soup)

table = ast.literal_eval(str(re.findall('var\stableDataNested\s=\s(.*).*', str(soup)))[2:-2])
mapping = ast.literal_eval(str(re.findall('var\smappingdata\s=\s(.*).*', str(soup)))[2:-3])
map_pos = ast.literal_eval(str(re.findall('var\smappositivedata\s=\s(.*).*', str(soup)))[2:-3])
map_neg = ast.literal_eval(str(re.findall('var\smapnegdata\s=\s(.*).*', str(soup)))[2:-3])
map_iso = ast.literal_eval(str(re.findall('var\smapisodata\s=\s(.*).*', str(soup)))[2:-3])
map_disch = ast.literal_eval(str(re.findall('var\smapdischdata\s=\s(.*).*', str(soup)))[2:-3])
map_death = ast.literal_eval(str(re.findall('var\smapdeathchdata\s=\s(.*).*', str(soup)))[2:-3])

# print(type(table), "\ntable\n", json.dumps(table))
with open('table.json', "w") as f:
    f.write(json.dumps(table, indent=2))
# print("\nmapping\n", mapping)
with open('mapping.json', "w") as f:
    f.write(json.dumps(mapping, indent=2))
# print("\npositive\n", map_pos)
with open('positive.json', "w") as f:
    f.write(json.dumps(map_pos, indent=2))
# print("\nnegative\n", map_neg)
with open('negative.json', "w") as f:
    f.write(json.dumps(map_neg, indent=2))
# print("\nisolation\n", map_iso)
with open('isolation.json', "w") as f:
    f.write(json.dumps(map_iso, indent=2))
# print("\ndischarge\n", map_disch)
with open('discharge.json', "w") as f:
    f.write(json.dumps(map_disch, indent=2))
# print("\ndeath\n", map_death)
with open('death.json', "w") as f:
    f.write(json.dumps(map_death, indent=2))
