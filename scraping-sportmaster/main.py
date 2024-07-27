import datetime
import time
import requests
from bs4 import BeautifulSoup
import json
import csv

cookies = {
    '_ym_uid': '16896158243025931',
    'UDID': 'fa7882b3-352b-4baf-9aa7-7cfc402f7c8c',
    'SMID': 'eyJhbGciOiJSUzI1NiJ9.eyJqdGkiOiIzZmQzOTRlNy01YWRmLTQ0NDMtOGY5ZS01MGEzY2FkODUyOTQiLCJpc3MiOiJTTTMwIiwiaWF0IjoxNzIwNDMwMjAzLCJhdWQiOlsic3BvcnRtYXN0ZXIiXSwiYW5UIjoiYjEwODkxZGQtNTBiNi00M2I5LWJkNTEtYzM2MzliMmVkMWM0IiwiYW5QIjoiY2E0ZmQ1YTAtN2YwNy00NWViLWEwOGMtMGYyMGRlYjliYjQ2IiwiYW5VIjoiMTAwMDAwMDEzMzg5Mjk5NzQwIiwiY2FuVCI6IkFJQ05sRWVJa0JjVW5mR0ZSQjlyODF0T2R0YTR6emd1MThtZnJvTGFpTXlQOG1DRXN6NEkxSEg5eFJMclVGWk9adndLemxkOUJhaHdFRXVlcTdWUWRHT3ZPL3VkQjVnNEpybjZ0enR1UGMwQUxsVyttQXRvQ2UvV3dNMDE3SWt4M1ExN3JCeE54bjlWUHF4bmQzd1JsWm1FYVY2cWxhWEhTTHhCU2dmYndndmdmR3dZWGF5ZVNXZ0xNUW45cHc4VW1zWkJ5VlRZSlo1L0s2ZFdCU2lFeUNxUUFSUFJPNW5Zb3ozOHE1L2lRTzZKelJ6YnNCY1FOK2h0RGZQRHhIeml5b1k9IiwiY2FuUCI6IkFJQnlUaG01RlJCYnJYcVUwYUtHV1NjdzJKZU1lTU51Y0VFeHY2cS96NE5ETWNvQ294UjNKbUZ6dWlQa2RnN3VONkVlR2w3aHNjbTBGSjVnRXFmSVlKOVlMdldSTHB5K25BZDk1cXRKQlB1UlhINDQ5M2M1NEo3N1dxN2xROFlUTVJqdnkzVFN6Qi96a01NSHg4R1dWd05mQzRUVk5XV0V3ajBWdmUzVlBYSEdOVEFDK0NKRFd2R3B4VVBBRWp4N05QUHRuWFNzT0FhZDJmdnBJK3ljZStSTWF2MzFBcGJtK0hYNjBkSzZYVkQ4NmptU050dEtZWlh1MVZvNWVWK2tlOFk9In0.Zh_9lMApWHY8mGJia_CWIpY8XxJZe91E-5VVDr32Ds0Nan7tTeo-Kzgd1xTLNb2nSsHD7BbtJwqNH63U36mHQ6mGrPcvbReWw1LbulYITeqR4TaI4xSY0iDozihw0mJ4jEGFTfJoBcULKw7Y_aFDNcMoXRAAWlYrHAUTIvZxLeerFc8C3tt9KK_PpRjHICeuzAuvB9nUApDzCtj6BVCZUgqI0sT9zH_QUHtiY0iQ109UldmaMKrBN3oOVqab5F8pC6hxb1zSWYxCW6QLE_Fxq7S6GBOqVPjJBMtaVlPThabjouYPu7GN3IbmsC7WZbSu6dSTgovx8rW_HPELa_V6CQ',
    'SMAID': 'ca4fd5a0-7f07-45eb-a08c-0f20deb9bb46',
    '__zzatw-sportm': 'MDA0dBA=Fz2+aQ==',
    '__zzatw-sportm': 'MDA0dBA=Fz2+aQ==',
    'userAuth': '0',
    'gdeslon.ru.__arc_domain': 'gdeslon.ru',
    'gdeslon.ru.user_id': '8b5e1a89-2572-4177-9438-d605a998c6e8',
    '_gid': 'GA1.2.1500696342.1720430203',
    'tmr_lvid': '5ea88e19b05d3a565186ad5192696e49',
    'tmr_lvidTS': '1689615833884',
    '_ym_d': '1720430203',
    'advcake_track_id': '6b4b239d-279b-3fba-6a9b-9b280764f94e',
    'advcake_session_id': 'b10a8756-badf-b420-598a-eece3b20c322',
    'adrcid': 'Af8bnJSnOVW4_FB3lBpmNxQ',
    'adrcid': 'Af8bnJSnOVW4_FB3lBpmNxQ',
    'SMAUTH': 'eyJpZCI6ImNhNGZkNWEwLTdmMDctNDVlYi1hMDhjLTBmMjBkZWI5YmI0NiIsInN0IjoiUkVUVVJORUQiLCJ0bSI6MTcyMDQzOTAyNH0=',
    'qrator_jsr': '1720522940.156.qdMkuHL7w4nEyUZE-suemuq6gfav3e3tm6imq8680ll6h0nnn-00',
    'qrator_jsid': '1720522940.156.qdMkuHL7w4nEyUZE-hrd9ffgpjn71dbh61gc7dpns46j0ir38',
    '_dc_gtm_UA-3450216-4': '1',
    '_ym_isad': '2',
    'domain_sid': '2AtEEDcoXY7ptEc5Gky-7%3A1720522946100',
    '_ym_visorc': 'w',
    'adrdel': '1720522946141',
    'adrdel': '1720522946141',
    'spcount': '39',
    '_ga': 'GA1.2.203848985.1720430203',
    'tmr_detect': '0%7C1720522954146',
    'gsscw-sportm': 'cFb8lpJmkFLt3OQ0tOXbqtwuxyAqwUflrzXFy84hduEbsnnpJdicSpSxGnYqHc7Ar1Eyezabd7CMh12jf+RaIIu4XWAcLXSxHAkzzuo0aWwqJctmpHGUKyE60FkvRnJ2WHc+o6aQhRh/TbQTS0DUqKtmblTU2RdcAbx+PrN3rNBeQk/PaV+WD8dYmV+NPaiVMQ+/WANEedfp5ojhpZmQNuFUs4TSsPWqTnGXCL7cs/O0W4Vav5+wM7BA+zn8t4lV3uQKuXUgx0mq',
    'cfidsw-sportm': 'hm5MdKFmlFMVaJJ+oIanZLdeOm6FNUilI3YU+c8H7UZzmrWBdPv3MbN8oUfGOI9NeghMXWFGJdyO9ATPBcD5OuciDmwHZyUaJfG+Cz8P/FZn1E1hrjP9BlbTgB2cPufUHjH2qJptYFpIW3pdAdTTqs4YwDqLbTQxLrgiE08=',
    'cfidsw-sportm': 'hm5MdKFmlFMVaJJ+oIanZLdeOm6FNUilI3YU+c8H7UZzmrWBdPv3MbN8oUfGOI9NeghMXWFGJdyO9ATPBcD5OuciDmwHZyUaJfG+Cz8P/FZn1E1hrjP9BlbTgB2cPufUHjH2qJptYFpIW3pdAdTTqs4YwDqLbTQxLrgiE08=',
    'cfidsw-sportm': 'hm5MdKFmlFMVaJJ+oIanZLdeOm6FNUilI3YU+c8H7UZzmrWBdPv3MbN8oUfGOI9NeghMXWFGJdyO9ATPBcD5OuciDmwHZyUaJfG+Cz8P/FZn1E1hrjP9BlbTgB2cPufUHjH2qJptYFpIW3pdAdTTqs4YwDqLbTQxLrgiE08=',
    'gsscw-sportm': 'cFb8lpJmkFLt3OQ0tOXbqtwuxyAqwUflrzXFy84hduEbsnnpJdicSpSxGnYqHc7Ar1Eyezabd7CMh12jf+RaIIu4XWAcLXSxHAkzzuo0aWwqJctmpHGUKyE60FkvRnJ2WHc+o6aQhRh/TbQTS0DUqKtmblTU2RdcAbx+PrN3rNBeQk/PaV+WD8dYmV+NPaiVMQ+/WANEedfp5ojhpZmQNuFUs4TSsPWqTnGXCL7cs/O0W4Vav5+wM7BA+zn8t4lV3uQKuXUgx0mq',
    'gsscw-sportm': 'cFb8lpJmkFLt3OQ0tOXbqtwuxyAqwUflrzXFy84hduEbsnnpJdicSpSxGnYqHc7Ar1Eyezabd7CMh12jf+RaIIu4XWAcLXSxHAkzzuo0aWwqJctmpHGUKyE60FkvRnJ2WHc+o6aQhRh/TbQTS0DUqKtmblTU2RdcAbx+PrN3rNBeQk/PaV+WD8dYmV+NPaiVMQ+/WANEedfp5ojhpZmQNuFUs4TSsPWqTnGXCL7cs/O0W4Vav5+wM7BA+zn8t4lV3uQKuXUgx0mq',
    'fgsscw-sportm': '1poV370be6844e164f3459b00b471509952b07d4',
    'fgsscw-sportm': '1poV370be6844e164f3459b00b471509952b07d4',
    '_ga_Z7E27793QJ': 'GS1.1.1720522945.3.1.1720522988.17.0.0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': '_ym_uid=16896158243025931; qrator_jsid=1720430202.493.HXwd9NQXsVjGunXM-dbb2sc9prgv24o242nmifk41q170indu; qrator_ssid=1720430202.945.GF5SPyDdmArOFEkm-asve6ldl1gcju8hvljkcqjmdcaicnm16; UDID=fa7882b3-352b-4baf-9aa7-7cfc402f7c8c; SMID=eyJhbGciOiJSUzI1NiJ9.eyJqdGkiOiIzZmQzOTRlNy01YWRmLTQ0NDMtOGY5ZS01MGEzY2FkODUyOTQiLCJpc3MiOiJTTTMwIiwiaWF0IjoxNzIwNDMwMjAzLCJhdWQiOlsic3BvcnRtYXN0ZXIiXSwiYW5UIjoiYjEwODkxZGQtNTBiNi00M2I5LWJkNTEtYzM2MzliMmVkMWM0IiwiYW5QIjoiY2E0ZmQ1YTAtN2YwNy00NWViLWEwOGMtMGYyMGRlYjliYjQ2IiwiYW5VIjoiMTAwMDAwMDEzMzg5Mjk5NzQwIiwiY2FuVCI6IkFJQ05sRWVJa0JjVW5mR0ZSQjlyODF0T2R0YTR6emd1MThtZnJvTGFpTXlQOG1DRXN6NEkxSEg5eFJMclVGWk9adndLemxkOUJhaHdFRXVlcTdWUWRHT3ZPL3VkQjVnNEpybjZ0enR1UGMwQUxsVyttQXRvQ2UvV3dNMDE3SWt4M1ExN3JCeE54bjlWUHF4bmQzd1JsWm1FYVY2cWxhWEhTTHhCU2dmYndndmdmR3dZWGF5ZVNXZ0xNUW45cHc4VW1zWkJ5VlRZSlo1L0s2ZFdCU2lFeUNxUUFSUFJPNW5Zb3ozOHE1L2lRTzZKelJ6YnNCY1FOK2h0RGZQRHhIeml5b1k9IiwiY2FuUCI6IkFJQnlUaG01RlJCYnJYcVUwYUtHV1NjdzJKZU1lTU51Y0VFeHY2cS96NE5ETWNvQ294UjNKbUZ6dWlQa2RnN3VONkVlR2w3aHNjbTBGSjVnRXFmSVlKOVlMdldSTHB5K25BZDk1cXRKQlB1UlhINDQ5M2M1NEo3N1dxN2xROFlUTVJqdnkzVFN6Qi96a01NSHg4R1dWd05mQzRUVk5XV0V3ajBWdmUzVlBYSEdOVEFDK0NKRFd2R3B4VVBBRWp4N05QUHRuWFNzT0FhZDJmdnBJK3ljZStSTWF2MzFBcGJtK0hYNjBkSzZYVkQ4NmptU050dEtZWlh1MVZvNWVWK2tlOFk9In0.Zh_9lMApWHY8mGJia_CWIpY8XxJZe91E-5VVDr32Ds0Nan7tTeo-Kzgd1xTLNb2nSsHD7BbtJwqNH63U36mHQ6mGrPcvbReWw1LbulYITeqR4TaI4xSY0iDozihw0mJ4jEGFTfJoBcULKw7Y_aFDNcMoXRAAWlYrHAUTIvZxLeerFc8C3tt9KK_PpRjHICeuzAuvB9nUApDzCtj6BVCZUgqI0sT9zH_QUHtiY0iQ109UldmaMKrBN3oOVqab5F8pC6hxb1zSWYxCW6QLE_Fxq7S6GBOqVPjJBMtaVlPThabjouYPu7GN3IbmsC7WZbSu6dSTgovx8rW_HPELa_V6CQ; SMAID=ca4fd5a0-7f07-45eb-a08c-0f20deb9bb46; srv_id=31725576a4a2dc204727229170299305; __zzatw-sportm=MDA0dBA=Fz2+aQ==; __zzatw-sportm=MDA0dBA=Fz2+aQ==; userAuth=0; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=8b5e1a89-2572-4177-9438-d605a998c6e8; _gid=GA1.2.1500696342.1720430203; tmr_lvid=5ea88e19b05d3a565186ad5192696e49; tmr_lvidTS=1689615833884; _ym_d=1720430203; advcake_track_id=6b4b239d-279b-3fba-6a9b-9b280764f94e; advcake_session_id=b10a8756-badf-b420-598a-eece3b20c322; adrcid=Af8bnJSnOVW4_FB3lBpmNxQ; adrcid=Af8bnJSnOVW4_FB3lBpmNxQ; _ym_isad=2; _ym_visorc=w; domain_sid=2AtEEDcoXY7ptEc5Gky-7%3A1720430203285; adrdel=1720430203459; adrdel=1720430203459; spcount=6; _ga=GA1.2.203848985.1720430203; tmr_detect=0%7C1720430449298; gsscw-sportm=EYJem303hwyyHmx4nXVO/FUBunr98k/5PZROGSUb3GPFl5LAGbSh7hJXYjRAlg7wthq83dllTtTWZwR6z0z1flmdCohYC00yKGyo+ka5h9AB3nJN0Z2Gv1Ih6EWHfeRVRXaGlHpkjgr5EarwhynX6X2u3p03477CZM4bQh8tLy37wB9ZNNkv3E4WVJ7XiebSQoQVOsDNnqZMx0rdbdCyTteOSbXEPZ2PiZMSfZma2YAulyBpqUoFrPDZ9k3amKJqtj66WPE6bnTNpKZWvg==; cfidsw-sportm=/HbLh+OaB8QP6+14bQgQGefwisrc4GZEBctZWmacls2BzQPmn329RkGtJlb4tUa6m9h1F5lmuLP/v1x2aUeVviygAVYfFIdYJ6RJsllo8VR7T5jJv/PcG5h0MJurIxJqdtevu+FDVE2g6dPkpfgX9RyWAvAJuId7pnOuMw==; cfidsw-sportm=/HbLh+OaB8QP6+14bQgQGefwisrc4GZEBctZWmacls2BzQPmn329RkGtJlb4tUa6m9h1F5lmuLP/v1x2aUeVviygAVYfFIdYJ6RJsllo8VR7T5jJv/PcG5h0MJurIxJqdtevu+FDVE2g6dPkpfgX9RyWAvAJuId7pnOuMw==; cfidsw-sportm=/HbLh+OaB8QP6+14bQgQGefwisrc4GZEBctZWmacls2BzQPmn329RkGtJlb4tUa6m9h1F5lmuLP/v1x2aUeVviygAVYfFIdYJ6RJsllo8VR7T5jJv/PcG5h0MJurIxJqdtevu+FDVE2g6dPkpfgX9RyWAvAJuId7pnOuMw==; gsscw-sportm=EYJem303hwyyHmx4nXVO/FUBunr98k/5PZROGSUb3GPFl5LAGbSh7hJXYjRAlg7wthq83dllTtTWZwR6z0z1flmdCohYC00yKGyo+ka5h9AB3nJN0Z2Gv1Ih6EWHfeRVRXaGlHpkjgr5EarwhynX6X2u3p03477CZM4bQh8tLy37wB9ZNNkv3E4WVJ7XiebSQoQVOsDNnqZMx0rdbdCyTteOSbXEPZ2PiZMSfZma2YAulyBpqUoFrPDZ9k3amKJqtj66WPE6bnTNpKZWvg==; gsscw-sportm=EYJem303hwyyHmx4nXVO/FUBunr98k/5PZROGSUb3GPFl5LAGbSh7hJXYjRAlg7wthq83dllTtTWZwR6z0z1flmdCohYC00yKGyo+ka5h9AB3nJN0Z2Gv1Ih6EWHfeRVRXaGlHpkjgr5EarwhynX6X2u3p03477CZM4bQh8tLy37wB9ZNNkv3E4WVJ7XiebSQoQVOsDNnqZMx0rdbdCyTteOSbXEPZ2PiZMSfZma2YAulyBpqUoFrPDZ9k3amKJqtj66WPE6bnTNpKZWvg==; SMAUTH=eyJpZCI6ImNhNGZkNWEwLTdmMDctNDVlYi1hMDhjLTBmMjBkZWI5YmI0NiIsInN0IjoiTkVXIiwidG0iOjE3MjA0MzA1Nzd9; fgsscw-sportm=KCT0aac327b7291d5c5da0468840f31d5dba5f09; fgsscw-sportm=KCT0aac327b7291d5c5da0468840f31d5dba5f09; _dc_gtm_UA-3450216-4=1; _ga_Z7E27793QJ=GS1.1.1720430202.1.1.1720430577.60.0.0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

data_now = datetime.date.today()

def get_link():
    link_tovar = []
    for item in range(1, 34):
        url = f"https://www.sportmaster.ru/catalog/muzhskaya_obuv/krossovki/?page={item}"

        req = requests.get(url, headers=headers, cookies=cookies)

        with open("index.html", "w", encoding="utf-8") as file:
            file.write(req.text)

        with open("index.html", encoding="utf-8") as file:
            page = file.read()

        soup = BeautifulSoup(page, "lxml")

        for i in soup.find_all("a", class_="sm-link sm-link_black"):
            if "catalog" in i.get("href") or "promo" in i.get("href"):
                continue
            link_tovar.append("https://www.sportmaster.ru/" + i.get("href"))
        print(item)
    print("stop fun get_link")

    return link_tovar

def get_data_csv(api, link):
    row = ("Название", "Цена", "Цена со скидкой", "Цвет", "Спорт", "Пол", "Возраст", "Ссылка")
    huy = zip(api, link)
    count = 1

    with open(f"result//{data_now}.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            row
        )
    try:
        for api, link in huy:
            print(count)
            req = requests.get(api, headers=headers, cookies=cookies)

            with open("api.json", "w", encoding="utf-8") as file:
                json.dump(req.json(), file, indent=4, ensure_ascii=False)

            with open("api.json", encoding="utf-8") as file:
                js = json.load(file)

            with open(f"result//{data_now}.csv", "a", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(
                    (js.get("productName"), js.get("productPrice"), js.get("productSalePrice"),
                     js.get("productColor"), js.get("productSport"), js.get("productGender"),
                     js.get("productAge"), link)
                )
            count += 1
    except:
        print("ошибка")
        time.sleep(3)

    print("stop fun get_data_csv")

def get_data_json(api, link):
    result_data = []
    huy = zip(api, link)
    count = 1
    try:
        for api, link in huy:
            print(count)
            req = requests.get(api, headers=headers, cookies=cookies)

            with open("api.json", "w", encoding="utf-8") as file:
                json.dump(req.json(), file, indent=4, ensure_ascii=False)

            with open("api.json", encoding="utf-8") as file:
                js = json.load(file)

            result_data.append(
                {
                    "Название": js.get("productName"),
                    "Цена": js.get("productPrice"),
                    "Цена со скидкой": js.get("productSalePrice"),
                    "Цвет": js.get("productColor"),
                    "Спорт": js.get("productSport"),
                    "Пол": js.get("productGender"),
                    "Возраст": js.get("productAge"),
                    "Ссылка": link
                }
            )
            count += 1
    except:
        print("ошибка")
        time.sleep(3)

    print("stop")
    with open(f"result//{data_now}.json", "w", encoding="utf-8") as file:
        json.dump(result_data, file, indent=4, ensure_ascii=False)

    print("stop fun get_data_json")

def get_num_api():
    num_api = []
    for item in range(1, 34):
        url = f"https://www.sportmaster.ru/catalog/muzhskaya_obuv/krossovki/?page={item}"

        req = requests.get(url, headers=headers, cookies=cookies)

        with open("index.html", "w", encoding="utf-8") as file:
            file.write(req.text)

        with open("index.html", encoding="utf-8") as file:
            page = file.read()

        soup = BeautifulSoup(page, "lxml")

        for i in soup.find_all("a", class_="sm-link sm-link_black"):
            if "catalog" in i.get("href") or "promo" in i.get("href"):
                continue
            num_api.append("https://www.sportmaster.ru/ga-api/v1/products/" + i.get("href").split("/")[2])

        print(item)

    print("stop fun get_num_api")

    return num_api

def main():
    api = get_num_api()
    link = get_link()
    get_data_json(api, link)
    get_data_csv(api, link)

if __name__ == "__main__":
    main()