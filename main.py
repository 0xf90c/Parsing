import requests
from bs4 import BeautifulSoup
import json

# url = "https://www.olx.uz/d/elektronika/telefony/q-a50/"
# req = requests.get(url)
# src = req.text
#
# with open("index.html", "w", encoding='utf-8') as file:
#     file.write(src)

# with open("index.html", encoding='utf-8') as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, 'lxml')
#
# all_phones = {}
# phone_names = soup.find_all(class_="css-1bbgabe")
# for phones in phone_names:
#     phone_name = phones.find('h6').text
#     phones_href = "https://www.olx.uz" + phones.get("href")
#     all_phones[phone_name] = phones_href
#
# with open("a50.json", 'w', encoding='utf-8') as file:
#     json.dump(all_phones, file, indent=4, ensure_ascii=False)

with open('a50.json', encoding='utf-8') as file:
    list_of_phones = json.load(file)

for phone_name, phone_url in list_of_phones.items():
    req = requests.get(url=phone_url)
    # src = req.text

    # print(src)
    # with open(f"data/{phone_name}.html", "w", encoding='utf-8') as file:
    #     file.write(src)
    with open(f"data/{phone_name}.html", encoding='utf-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')

    desc = soup.find(class_="css-1wws9er")
    short_desc = desc.find('h1').text
    full_desc = desc.find(class_="css-g5mtbi-Text").text
    phone_price = desc.find('h3').text
    product_info = [{
        'Short description': short_desc,
        'Price': phone_price,
        'Full description': full_desc,
        'Web page url': phone_url
    }]
    with open(f"data-json/{phone_name}.json", 'w', encoding='utf-8') as file:
        json.dump(product_info, file, indent=4, ensure_ascii=False)
