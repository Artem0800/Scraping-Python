import json
from bs4 import BeautifulSoup

result_data_cars = []
for i in range(1,100):
    with open(f"indexы\index{i}.html",encoding="utf-8") as file:
        f = file.read()

    soup = BeautifulSoup(f, "lxml")

    page_info = soup.find_all("a", class_="Link ListingItemTitle__link")
    link_car = []
    name_car = []
    for i in page_info:
        link_car.append(i.get("href"))
        name_car.append(i.text)

    full_info = soup.find_all(class_="ListingItem__summary")
    description = []
    for i in full_info:
        row = []
        for j in i.find_all(class_="ListingItemTechSummaryDesktop__cell"):
            row.append(j.text)
        description.append(row)
    price_car = soup.find_all("div", class_="ListingItem__priceBlock")
    prices_car = []
    for i in price_car:
        t = i.text
        prices_car.append(t[0:t.find("₽")])

    years_cars = []
    for i in soup.find_all("div", class_="ListingItem__year"):
        years_cars.append(i.text)

    km_cars = []
    for i in soup.find_all("div", class_="ListingItem__kmAge"):
        km_cars.append(i.text)

    data_cars = zip(link_car, name_car, description, prices_car, years_cars, km_cars)

    for link, name, des, price, years, km in data_cars:
        result_data_cars.append(
            {
                "Ссылка": link,
                "Название": name,
                "Описание": des,
                "Год выпуска": years,
                "Пробег": km,
                "Цена": price
            }
        )

with open("result.json", "w", encoding="utf-8") as file:
    json.dump(result_data_cars, file, indent=4, ensure_ascii=False)