import datetime
import json
import os
from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")
options.add_argument("headless")

def get_data(*url):
    data_now = datetime.date.today()
    link, name_link = url
    result_data = []
    count_old = 1
    input_page = int(input("Введите кол-во страниц пазязя"))

    for item in range(1, input_page + 1):
        link_ = link.replace(str(count_old), str(item))

        driver = webdriver.Chrome(options=options)
        driver.get(link_)

        with open("index.html", "w", encoding="utf-8") as file:
            file.write(driver.page_source)

        with open("index.html", encoding="utf-8") as file:
            page = file.read()

        soup = BeautifulSoup(page, "lxml")

        tovar = []
        img_link_tovar = []
        code_tovar = []
        stock_tovar = []
        link_product = []
        price_product = []
        for i in soup.find_all("div", class_="products__item")[1::]:
            tovar.append(i.find("img").get("alt"))
            img_link_tovar.append(i.find("img").get("src"))
            code_tovar.append(i.find("span", class_="products__item-id").text)

            try:
                stock_tovar.append(i.find("span", class_="products__item-status products__item-status--true").text)
            except:
                stock_tovar.append(i.find("span", class_="products__item-status products__item-status--false").text)

            link_product.append(i.find("a", class_="products__item-title").get("href"))
            price_product.append(i.find("p", class_="products__item-price").text.strip())

        result = zip(tovar, img_link_tovar, code_tovar, stock_tovar, link_product, price_product)
        for product, img_link, code, stock, link_tovar, price in result:
            result_data.append(
                {
                    "Ссылка на картинку": img_link,
                    "Ссылка на товар": link_tovar,
                    "Название товара": product,
                    "Код": code,
                    "Наличие": stock,
                    "Стоимость": price
                }
            )
        print(item)

    path = f"Result//{name_link}"

    if os.path.isdir(path) == False:
        os.makedirs(path)

    with open(f"Result//{name_link}//{data_now}.json", "w", encoding="utf-8") as file:
        json.dump(result_data, file, indent=4, ensure_ascii=False)

def get_url_user():
    link = {
        "ноутбуки": "https://smp-laptops.ru/computers/laptops/game-laptops?page=1",
        "компьютеры": "https://smp-laptops.ru/computers/personal-computers?page=1",
        "приставки": "https://smp-laptops.ru/gaming-accessories/gaming-consoles?page=1"
    }

    user_input = input("Про что хотите собрать информацию ? ноутбуки/компьютеры/приставки").lower()

    return link.get(user_input), user_input

def main():
    a,b = get_url_user()
    get_data(a,b)

if __name__ == "__main__":
    main()