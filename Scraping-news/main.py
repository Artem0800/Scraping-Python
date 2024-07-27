import requests
from bs4 import BeautifulSoup
import json
import datetime

def get_info(list_link):
    data_news = []
    print("Начиеам собирать информацию со страниц")
    for count_page, item in enumerate(list_link):
        url = item
        head = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        }
        req = requests.get(url, headers=head)
        with open("index.html", "w", encoding="utf-8") as file:
            file.write(req.text)

        with open("index.html", encoding="utf-8") as file:
            f = file.read()

        soup = BeautifulSoup(f, "lxml")

        title_news = ""
        for i in soup.find_all("span", class_="topic-body__title"):
            title_news += i.text

        time_data_news = ""
        for i in soup.find_all("a", class_="topic-header__item topic-header__time"):
            time_data_news += i.text

        img_news = []
        try:
            for i in soup.find_all("img", class_="picture__image"):
                img_news.append(i.get("src"))
        except:
            img_news.append("Нету картинок")

        info_news = []
        for i in soup.find_all("div", class_="topic-body__content"):
            info_news.append(i.text)

        data_news.append(
            {
                "Время и дата публикации": time_data_news,
                "Название": title_news,
                "Ссылки на картинки": img_news,
                "Информация": info_news
            }
        )
        print(count_page)

    with open(f"Новости на {datetime.date.today()}.json", "w", encoding="utf-8") as file:
        json.dump(data_news, file, indent=4, ensure_ascii=False)

    print("Сбор закончен")

def news_link(years,week,day):
    count_page = 1
    link_news = []
    while True:
        try:
            url = f"https://lenta.ru/{years}/{week}/{day}/page/{count_page}/"
            head = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
            }
            req = requests.get(url, headers=head)

            with open("index.html", "w", encoding="utf-8") as file:
                file.write(req.text)

            with open("index.html", encoding="utf-8") as file:
                f = file.read()

            soup = BeautifulSoup(f, "lxml")

            for i in soup.find("ul", class_="archive-page__container").find_all("li")[:-1]:
                if i.find("a").get("href").startswith("https://lenta.ru"):
                    link_news.append(i.find("a").get("href"))
                else:
                    link_news.append("https://lenta.ru" + i.find("a").get("href"))
            print(count_page)
        except:
            print("Сбор ссылок завершен")
            break
        finally:
            count_page += 1
    return link_news

def main():
    a = news_link("2024","06","12")
    get_info(a)

if __name__ == "__main__":
    main()