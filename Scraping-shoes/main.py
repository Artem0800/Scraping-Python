from bs4 import BeautifulSoup
import requests
import json

for p in range(0,131):
    url = f"https://obuv-tut2000.ru/magazin/folder/optom-ot-4h-par-zhenskaya-muzhskaya-detskaya-obuv/p/{p}"
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }
    req = requests.get(url, headers=head)
    with open("index.html","w",encoding="utf-8") as file:
        file.write(req.text)
    with open("index.html",encoding="utf-8") as file:
        page = file.read()
    soup = BeautifulSoup(page, "lxml")
    page_shoes = soup.find_all("a", class_="hasimg")
    link_shoes = []
    name_shoes = []
    link_picture_shoes = []
    for i in page_shoes:
        link_shoes.append("https://obuv-tut2000.ru" + i.get("href"))
        name_shoes.append(i.find("img", class_="img1").get("alt"))
        link_picture_shoes.append("https://obuv-tut2000.ru" + i.find("img", class_="img1").get("src"))
    article_shoes = soup.find_all("div", class_="shop2-product-article")
    article_shoes_ = []
    for i in article_shoes:
        article_shoes_.append(i.text)
    size_shoes = soup.find_all("div", class_="option_value")
    size_shoes_ = []
    for i in size_shoes:
        size_shoes_.append(i.text)
    price_shoes = soup.find_all("div", class_="price-current")
    price_shoes_ = []
    for i in price_shoes:
        for j in i.find_all("strong"):
            price_shoes_.append(j.text)
    result = []
    result_ = zip(link_shoes, name_shoes, link_picture_shoes, article_shoes_, size_shoes_, price_shoes_)
    for link,name,picture,article,size,price in result_:
        result.append(
            {
                "Ссылка на товар": link,
                "Картинка товара": picture,
                "Название товара": name,
                "Артикул": article,
                "Размер": size,
                "Стоимость": price
            }
        )
    with open("result.json", "a", encoding="utf-8") as file:
        json.dump(result, file, indent=4, ensure_ascii=False)
    print(f"Страница {p} собрана")