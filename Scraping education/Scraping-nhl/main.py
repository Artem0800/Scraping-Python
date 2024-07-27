import time
from selenium import webdriver
from bs4 import BeautifulSoup
import os
import requests
import json

def get_data_team_player(link):
    link_team, name_team = link

    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
    options.add_argument("headless")

    driver = webdriver.Chrome(options=options)
    driver.get(link_team)
    time.sleep(3)

    with open("index1.html", "w", encoding="utf-8") as file:
        file.write(driver.page_source)

    with open("index1.html", encoding="utf-8") as file:
        page = file.read()

    soup = BeautifulSoup(page, "lxml")

    name_player = []
    link_player = []
    for i in soup.find_all("a", class_="sc-ia-dotI eFAOfp"):
        name_player.append(i.text)
        link_player.append("https://www.nhl.com" + i.get("href"))

    img_player = []
    for i in soup.find_all("div", class_="headshot-container"):
        img_player.append(i.find("image").get("href"))

    result_img_player = []
    for i in img_player:
        result_img_player.append(requests.get(i).content)

    infa_player = []
    for i in soup.find_all("tr", class_="sc-iqziPC eauCbT rt-tr null"):
        for j in i.find_all("td"):
            infa_player.append(j.text)

    infa_player_ = []
    while len(infa_player) != 0:
        infa_player_.append(
            {
                "Number": infa_player[0],
                "Position": infa_player[1],
                "Shoots": infa_player[2],
                "Height": infa_player[3],
                "Weight": infa_player[4],
                "Born": infa_player[5],
                "Birthplace": infa_player[6]
            }
        )
        del infa_player[0:7]

    driver.close()
    driver.quit()

    end_game = zip(name_player, link_player, result_img_player, infa_player_)
    for name, link, img, infa in end_game:
        os.makedirs(f"Infa\{name_team}\{name}")
        with open(f"Infa\{name_team}\{name}\photo_player.png", "wb") as file:
            file.write(img)
        with open(f"Infa\{name_team}\{name}\infa.json", "w", encoding="utf-8") as file:
            json.dump(infa, file, indent=4, ensure_ascii=False)
        with open(f"Infa\{name_team}\{name}\FullInfa.txt", "w", encoding="utf-8") as file:
            file.write(link)

def get_link_team_roster(list_team):
    for name, link in list_team.items():
        print(name)
    txt = input("Выберите команду по которым будете собирать информацию")

    return list_team[txt], txt

def get_team(url):
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
    options.add_argument("headless")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(3)

    with open("index.html", "w", encoding="utf-8") as file:
        file.write(driver.page_source)

    with open("index.html", encoding="utf-8") as file:
        page = file.read()

    soup = BeautifulSoup(page, "lxml")

    name_team = []
    for i in soup.find_all("a", class_="nhl-c-team-menu__link -team"):
        name_team.append(i.text.strip().replace("north_east", "").strip())

    link_team = []
    for i in soup.find_all("a", class_="nhl-o-menu__link"):
        if i.get("href").endswith("roster"):
            if i.get("href") == "/bluejackets/roster":
                link_team.append("https://www.nhl.com/" + i.get("href"))
            else:
                link_team.append(i.get("href"))

    result = {}
    for name, link in zip(name_team, link_team):
        result[name] = link

    driver.close()
    driver.quit()

    return result

def main():
    res = get_team("https://www.nhl.com/info/teams/")
    res2 = get_link_team_roster(res)
    get_data_team_player(res2)

if __name__ == "__main__":
    main()