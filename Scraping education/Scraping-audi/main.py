# from selenium import webdriver
# import os

# забираем первую страницу

# url = "https://auto.ru/cars/audi/all/"
#
# options = webdriver.ChromeOptions()
# options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:126.0) Gecko/20100101 Firefox/126.0")
#
# driver = webdriver.Chrome(options=options)
# driver.get(url)
# time.sleep(3)

# with open("index.html", "w", encoding="utf-8") as file:
#     file.write(driver.page_source)

# Проходимся циклом по всем страницам

# for i in range(2,100):
#     url = f"https://auto.ru/cars/audi/all/?page={i}"
#
#     options = webdriver.ChromeOptions()
#     options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:126.0) Gecko/20100101 Firefox/126.0")
#
#     driver = webdriver.Chrome(options=options)
#     driver.get(url)
#     u = driver.current_url
#     if u != f"https://auto.ru/cars/audi/all/?page={i}":
#         continue
#     else:
#         with open(f"index{i}.html", "w", encoding="utf-8") as file:
#             file.write(driver.page_source)

# Проходимся по тем страницам которые у нас не прошли

# non = []
# num = []
# ind = [i for i in os.listdir() if "index" in i]
# for i in ind:
#     res = i.replace("index","")
#     res2 = res.replace(".html","")
#     num.append(int(res2))
# sor = sorted(num)
# for item in range(1,100):
#     if item not in sor:
#         non.append(item)

# for i in non:
#     url = f"https://auto.ru/cars/audi/all/?page={i}"
#
#     options = webdriver.ChromeOptions()
#     options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:126.0) Gecko/20100101 Firefox/126.0")
#
#     driver = webdriver.Chrome(options=options)
#     driver.get(url)
#     u = driver.current_url
#     if u != f"https://auto.ru/cars/audi/all/?page={i}":
#         continue
#     else:
#         with open(f"index{i}.html", "w", encoding="utf-8") as file:
#             file.write(driver.page_source)

# Еще раз проходимся по тем страница которые у нас не прошли

# non = []
# num = []
# ind = [i for i in os.listdir() if "index" in i]
# for i in ind:
#     res = i.replace("index","")
#     res2 = res.replace(".html","")
#     num.append(int(res2))
# sor = sorted(num)
# for item in range(1,100):
#     if item not in sor:
#         non.append(item)
#
# for i in non:
#     url = f"https://auto.ru/cars/audi/all/?page={i}"
#
#     options = webdriver.ChromeOptions()
#     options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
#
#     driver = webdriver.Chrome(options=options)
#     driver.get(url)
#     u = driver.current_url
#     if u != f"https://auto.ru/cars/audi/all/?page={i}":
#         continue
#     else:
#         with open(f"index{i}.html", "w", encoding="utf-8") as file:
#             file.write(driver.page_source)

# БЛЯЯЯЯЯЯТЬ еще раз проходимся по тем страницам которые у нас не прошлись

# non = []
# num = []
# ind = [i for i in os.listdir() if "index" in i]
# for i in ind:
#     res = i.replace("index","")
#     res2 = res.replace(".html","")
#     num.append(int(res2))
# sor = sorted(num)
# for item in range(1,100):
#     if item not in sor:
#         non.append(item)
#
# for i in non:
#     url = f"https://auto.ru/cars/audi/all/?page={i}"
#
#     options = webdriver.ChromeOptions()
#     options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
#
#     driver = webdriver.Chrome(options=options)
#     driver.get(url)
#     u = driver.current_url
#     if u != f"https://auto.ru/cars/audi/all/?page={i}":
#         continue
#     else:
#         with open(f"index{i}.html", "w", encoding="utf-8") as file:
#             file.write(driver.page_source)

# Клянусь последний раз блять

# non = []
# num = []
# ind = [i for i in os.listdir() if "index" in i]
# for i in ind:
#     res = i.replace("index","")
#     res2 = res.replace(".html","")
#     num.append(int(res2))
# sor = sorted(num)
# for item in range(1,100):
#     if item not in sor:
#         non.append(item)
#
# for i in non:
#     url = f"https://auto.ru/cars/audi/all/?page={i}"
#
#     options = webdriver.ChromeOptions()
#     options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
#
#     driver = webdriver.Chrome(options=options)
#     driver.get(url)
#     u = driver.current_url
#     if u != f"https://auto.ru/cars/audi/all/?page={i}":
#         continue
#     else:
#         with open(f"index{i}.html", "w", encoding="utf-8") as file:
#             file.write(driver.page_source)

# Я тупое уебище

