import requests
from bs4 import BeautifulSoup
import json

# Собираем данные сколько всего страниц нужно собрать
count_page = 0
url = "https://www.bestwatch.ru/watch/filter/pol:mens/"
error = []

head = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}
req = requests.get(url, headers=head)

with open("index.html", "w", encoding="utf-8") as file:
    file.write(req.text)

data_watch = []

with open("index.html", encoding="utf-8") as file:
    page = file.read()

soup = BeautifulSoup(page, "lxml")

pagination_page_watch = int(soup.find("div", class_="pagination-block").find_all("li")[5].text.strip())
count_page += pagination_page_watch

# Здесь уже собираем все страницы
for item in range(1, count_page + 1):
    try:
        url = f"https://www.bestwatch.ru/watch/filter/pol:mens/?pages={item}"

        head = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        }
        req = requests.get(url, headers=head)

        with open("index.html", "w", encoding="utf-8") as file:
            file.write(req.text)


        with open("index.html", encoding="utf-8") as file:
            page = file.read()

        soup = BeautifulSoup(page, "lxml")
        link_watch = []
        link_img_watch = []
        article_watch = []
        name_watch = []
        for i in soup.find_all("div", class_="catalog-item__body"):
            link_watch.append("https://www.bestwatch.ru" + i.find("a").get("href"))
            link_img_watch.append(i.find("img").get("src")[2::].replace(" ", "").replace("www.bestwatch.ru/",""))

        for i in soup.find_all("p", class_="catalog-item__code"):
            article_watch.append(i.text.strip())

        for i in soup.find_all("span", class_="bold"):
            name_watch.append(i.text)

        old_price_watch = []
        for i in soup.find_all("p", class_="catalog-item__oldprice"):
            if i.text.strip() == "":
                old_price_watch.append("Старой цены нету")
            else:
                old_price_watch.append(i.text.strip())

        discount_watch = []
        for i in soup.find_all("div", class_="catalog-item"):
            if i.find("p", class_="catalog-item__sale") is None:
                discount_watch.append("Скидки нету")
            else:
                discount_watch.append(i.find("p", class_="catalog-item__sale").text)

        price_watch = []
        for i in soup.find_all("p", class_="catalog-item__price with-sale"):
            price_watch.append(i.text.strip())

        description = []
        for i in soup.find_all("div", class_="catalog-item__footer"):
            description.append(i.find_all("meta")[1].get("content"))

        result = zip(link_watch, link_img_watch, article_watch, name_watch, old_price_watch, discount_watch, price_watch, description)
        for link, link_img, article, name, old_price, discount, price, des in result:
            data_watch.append(
                {
                    "Ссылка": link,
                    "Ссылка на картинку": link_img,
                    "Артикул": article,
                    "Название": name,
                    "Цена": price,
                    "Старая цена": old_price,
                    "Скидка": discount,
                    "Описание": des
                }
            )
    except:
        error.append(item)
        print(f"{item} эта страница не прошла")
        continue
    finally:
        print(f"Собрана {item}/{count_page} страниц")

def name(l):
    print("Еще раз")
    er = []
    for item in l:
        try:
            url = f"https://www.bestwatch.ru/watch/filter/pol:mens/?pages={item}"

            head = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
            }
            req = requests.get(url, headers=head)

            with open("index.html", "w", encoding="utf-8") as file:
                file.write(req.text)


            with open("index.html", encoding="utf-8") as file:
                page = file.read()

            soup = BeautifulSoup(page, "lxml")
            link_watch = []
            link_img_watch = []
            article_watch = []
            name_watch = []
            for i in soup.find_all("div", class_="catalog-item__body"):
                link_watch.append("https://www.bestwatch.ru/" + i.find("a").get("href"))
                link_img_watch.append(i.find("img").get("src")[2::].replace(" ", ""))

            for i in soup.find_all("p", class_="catalog-item__code"):
                article_watch.append(i.text.strip())

            for i in soup.find_all("span", class_="bold"):
                name_watch.append(i.text)

            old_price_watch = []
            for i in soup.find_all("p", class_="catalog-item__oldprice"):
                if i.text.strip() == "":
                    old_price_watch.append("Старой цены нету")
                else:
                    old_price_watch.append(i.text.strip())

            discount_watch = []
            for i in soup.find_all("div", class_="catalog-item"):
                if i.find("p", class_="catalog-item__sale") is None:
                    discount_watch.append("Скидки нету")
                else:
                    discount_watch.append(i.find("p", class_="catalog-item__sale").text)

            price_watch = []
            for i in soup.find_all("p", class_="catalog-item__price with-sale"):
                price_watch.append(i.text.strip())

            description = []
            for i in soup.find_all("div", class_="catalog-item__footer"):
                description.append(i.find_all("meta")[1].get("content"))

            result = zip(link_watch, link_img_watch, article_watch, name_watch, old_price_watch, discount_watch,
                         price_watch, description)
            for link, link_img, article, name, old_price, discount, price, des in result:
                data_watch.append(
                    {
                        "Ссылка": link,
                        "Ссылка на картинку": link_img,
                        "Артикул": article,
                        "Название": name,
                        "Цена": price,
                        "Старая цена": old_price,
                        "Скидка": discount,
                        "Описание": des
                    }
                )
            print(f"Собрана {item}/{count_page} страниц")
        except:
            er.append(item)
            continue
    exam(er)

def end():
    print("Победа")
    with open("result.json", "w", encoding="utf-8") as file:
        json.dump(data_watch, file, indent=4, ensure_ascii=False)

def exam(l):
    print("Проверка")
    if l != []:
        name(l)
    else:
        end()


exam(error)