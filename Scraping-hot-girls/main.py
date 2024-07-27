import requests
from bs4 import BeautifulSoup

# url = "https://www.girlstop.info/"
#
# count_page = 0
# head = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
# }
# req = requests.get(url, headers=head)
#
# with open("index.html", "w", encoding="utf-8") as file:
#     file.write(req.text)
#
# with open("index.html", encoding="utf-8") as file:
#     page = file.read()
#
# soup = BeautifulSoup(page, "lxml")
#
# for i in soup.find("div", class_="paginator_pages"):
#     count_page += int(i.split()[0])
#
# img = []
#
# for item in range(0, count_page + 1):
#     url = f"https://www.girlstop.info/index.php?page={item}"
#
#     head = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
#     }
#     req = requests.get(url, headers=head)
#
#     with open("index.html", "w", encoding="utf-8") as file:
#         file.write(req.text)
#
#     with open("index.html", encoding="utf-8") as file:
#         page = file.read()
#
#     soup = BeautifulSoup(page, "lxml")
#
#
#     for i in soup.find_all("picture"):
#         img.append(i.find("img", class_="photo450").get("src"))
#
#     print(item)
#
# res_img = []
# count = 0
# for i in img:
#     count += 1
#     print(count)
#     req = requests.get(i).content
#     with open(f"IMG\{count}.jpg", "wb") as file:
#         file.write(req)
#         res_img.append(f"IMG\{count}.jpg")