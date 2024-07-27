import time
from selenium import webdriver
from bs4 import BeautifulSoup
import json
import datetime

def get_data():
    url = "https://www.coinbase.com/ru/explore?page=1"
    option = webdriver.ChromeOptions()
    option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(options=option)
    driver.get(url)
    time.sleep(1)
    with open("index.html", "w", encoding="utf-8") as file:
        file.write(driver.page_source)

    with open("index.html", encoding="utf-8") as file:
        f = file.read()

    soup = BeautifulSoup(f, "lxml")

    count_page = int(soup.find_all("span", class_="Text__Font-sc-3fa34bff-0 TTOxf PaginationBarItem__PageLinkText-sc-c28656da-2 ciaXLt")[-1].text)
    driver.close()
    driver.quit()
    result_data_cripto = []
    bim = int(input(f"Укажите сколько страниц вам нужно собрать. Их всего {count_page}"))
    print(f"Начинаем сбор данных на {datetime.datetime.now()}")
    for item in range(1, bim + 1):
        url = f"https://www.coinbase.com/ru/explore?page={item}"
        option = webdriver.ChromeOptions()
        option.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")

        driver = webdriver.Chrome(options=option)
        driver.get(url)
        time.sleep(3)
        with open("index.html", "w", encoding="utf-8") as file:
            file.write(driver.page_source)

        with open("index.html", encoding="utf-8") as file:
            f = file.read()

        soup = BeautifulSoup(f, "lxml")
        driver.close()
        name_cripto = []
        for i in soup.find_all("div", class_="cds-flex-f1g67tkn cds-column-ci8mx7v")[:-1]:
            try:
                name_cripto.append(i.find("h2", class_="cds-typographyResets-t1xhpuq2 cds-headline-htr1998 cds-foreground-f1yzxzgu cds-transition-txjiwsi cds-start-s1muvu8a").text)
            except:
                continue

        info_cripto = []
        for i in soup.find_all("div", class_="cds-flex-f1g67tkn cds-flex-end-f9tvb5a cds-column-ci8mx7v cds-flex-start-f1urtf06 cds-0_5-_5akrcb"):
            if i.text == "":
                continue
            elif "%" in i.text:
                continue
            info_cripto.append(i.text)

        complite_info_cripto = []
        while len(info_cripto) != 0:
            complite_info_cripto.append(
                {
                    "Стоимость": info_cripto[0],
                    "Рыночная капитализация": info_cripto[1],
                    "Объём (24 часа)": info_cripto[2],
                    "Предложение": info_cripto[3]
                }
            )
            del info_cripto[0:4]

        link_cripto = []
        for i in soup.find_all("a", class_="cds-link cds-link-l17zyfmx"):
            if "price" in i.get("href"):
                link_cripto.append("https://www.coinbase.com/" + i.get("href"))

        result = zip(name_cripto, link_cripto, complite_info_cripto)
        for name, link, info in result:
            result_data_cripto.append(
                {
                    "Название": name,
                    "Ссылка": link,
                    "Информация": info
                }
            )

        print(f"{item}/{count_page}")

    driver.quit()

    print("Сбор данных завершен")
    path_user = input("Укажите путь для того чтобы сохранить туда полученые данные")
    name_result = input("Напиши как будет называется ваш исходный файл")

    with open(f"{path_user}//{name_result}.json", "w", encoding="utf-8") as file:
        json.dump(result_data_cripto, file, indent=4, ensure_ascii=False)

    input("Нажмите enter чтобы закрыть программу")

def main():
    get_data()

if __name__ == '__main__':
    main()