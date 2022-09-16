import csv

import json

import requests
from bs4 import BeautifulSoup

# url = 'https://nambafood.kg/cafe'
# req = requests.get(url)
# src = req.text

# with open('html/all_cafe.html', 'w', encoding='utf-8') as file:
#     file.write(src)
# with open('html/all_cafe.html', encoding='utf-8') as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, 'lxml')
# all_links = soup.find(class_='catalog-wrap').find_all('a')
# all_cafe = {}
# for link in all_links:
#     title = link.find(class_="cafe--name").text.strip()
#     url = "https://nambafood.kg" + link.get('href')
#     # print(f"{title}: {url}")
#     all_cafe[title] = url
# with open('json/all_cafe.json', 'w', encoding='utf-8') as file:
#     json.dump(all_cafe, file, indent=4, ensure_ascii=False)
with open('json/all_cafe.json', encoding='utf-8') as file:
    all_cafe = json.load(file)

iteration_count = int(len(all_cafe))-1
print(f"Number of operations: {iteration_count}")
count = 0
for cafe_name, cafe_url in all_cafe.items():
    req = requests.get(url=cafe_url)
    src = req.text

    with open(f'html/all_cafes/{cafe_name}.html', 'w', encoding='utf-8') as file:
        file.write(src)
    # with open(f'html/all_cafes/{cafe_name}.html', encoding='utf-8') as file:
    #     src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    all_cards = soup.find_all(class_="section--container")
    for card in all_cards:
        cat_name = card.find('h2').text.strip()
        all_card_items = card.find_all(class_="card--item")
        try:
            for card_item in all_card_items:
                food_title = card_item.find(class_="card--item--title").text.strip()
                food_description = card_item.find(class_="card--item--description").text.strip()
                food_price = card_item.find(class_='price').text.strip()
                food_img = "https://nambafood.kg" + card_item.find('img').get('src')
                # print(f"Category: {cat_name}\n"
                #       f"Title: {food_title}\n"
                #       f"Description: {food_description}\n"
                #       f"Price: {food_price}\n"
                #       f"Image: {food_img}\n")
                # name = 'Наименование'
                # description = 'Описание'
                # category = 'Категория'
                # price = 'Цена'
                # photo = 'Фото'
                # with open(f'csv/all_cafe/{cafe_name}.csv', 'w', encoding='utf-8') as file:
                #     writer = csv.writer(file)
                #     writer.writerow(
                #         (
                #             name,
                #             description,
                #             category,
                #             price,
                #             photo
                #         )
                #     )
                with open(f'csv/all_cafe/{cafe_name}.csv', 'a', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(
                        (
                            food_title,
                            food_description,
                            cat_name,
                            food_price,
                            food_img
                        )
                    )
        except Exception:
            food_title = None
            food_description = None
            food_price = None
            food_price = None


    count += 1
    print(f"{count}_{cafe_name} has been writen")
    iteration_count -= 1
    if iteration_count == 0:
        print("Finished successfully!\n")
        print("CONGRATULATIONS")
        break
    print(f'{iteration_count} left')
