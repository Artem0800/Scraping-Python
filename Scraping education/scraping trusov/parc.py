from bs4 import BeautifulSoup
import requests

# url = "https://kupalniki-nsk.ru/catalog/zhenskie-kupalniki/filter/filter-is-novinka/"
# head = {
#     "Accept": "*/*",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
# }
# req = requests.get(url, headers=head)
# with open("index.html","w",encoding="utf-8") as file:
#     file.write(req.text)

# with open("index.html",encoding="utf-8") as file:
#     res = file.read()
# soup = BeautifulSoup(res, "lxml")
# trusiki = soup.find_all(class_="product-block__name padding-5-10 padding-5-10")
# price_trusiki = soup.find_all(class_="product-block__price")
# result = zip(trusiki,price_trusiki)
#
# with open("result.txt","w",encoding="utf-8") as out:
#     for i, j in result:
#         out.write(f"{i.text}, {j.text}\n")
#
# for i in range(2,14):
#     url_1 = f"https://kupalniki-nsk.ru/catalog/zhenskie-kupalniki/filter/filter-is-novinka/page-{i}/"
#     head_1 = {
#         "Accept": "*/*",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
#     }
#     req_1 = requests.get(url_1, headers=head_1)
#     soup_1 = BeautifulSoup(req_1.text, "lxml")
#     trusiki_1 = soup_1.find_all(class_="product-block__name padding-5-10 padding-5-10")
#     price_trusiki_1 = soup_1.find_all(class_="product-block__price")
#     result_1 = zip(trusiki_1, price_trusiki_1)
#     for x, y in result_1:
#         with open("result.txt","a",encoding="utf-8") as file_res_1:
#             file_res_1.write(f"{x.text}, {y.text}\n")