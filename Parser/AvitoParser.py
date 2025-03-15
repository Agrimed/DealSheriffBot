# from bs4 import BeautifulSoup
# import requests
# from selenium.common.exceptions import TimeoutException, NoSuchElementException
# import logging

# # logging.basicConfig(level=logging.DEBUG)

# class Parser:

#     headers = {
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#         "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
#         "Referer": "https://www.avito.ru/"
#     }

#     def __init__(self):
#         self.session = requests.Session()
#         self.session.headers.update(Parser.headers)

#     def send_request(self, num):
#         url=f"https://www.avito.ru/all?q={num}"
#         response = self.session.get(url)
#         return response

#     def parsing_page(self, num):
#         response = self.send_request(num)
#         soup = BeautifulSoup(response.text, "html.parser")
#         link_element = soup.find("a", attrs = {"class": "iva-item-sliderLink-Fvfau"})
#         relative_url = link_element.get('href')
#         full_url = f"https://www.avito.ru{relative_url}"
#         response_to_adv = self.session.get(full_url)
#         adv_html = response_to_adv.text

#         with open("html.txt", "w", encoding = "utf-8") as text_file:
#             text_file.write(adv_html)


#     def is_adv_exist(self, num):
#         response = self.send_request(num)
#         soup = BeautifulSoup(response.text, "html.parser")
#         no_results = soup.find("h2", attrs = {"class": "no-results-title-jho0M"})
#         if no_results:
#             return False  # Объявление не существует
#         else:
#             return True

#     def write_data(self):

#         with open("html.txt", "r", encoding = "utf-8") as file:
#             data = file.read()

#         soup = BeautifulSoup(data, 'html.parser')

#         title_html = soup.find("h1", attrs = {"data-marker": "item-view/title-info"})
#         desc_html = soup.find("div", attrs = {"data-marker": "item-view/item-description"})

#         with open("title.txt", "w", encoding = "utf-8") as text_file:
#             text_file.write(title_html.text)

#         with open("body.txt", "w", encoding="utf-8") as text_file:
#             pass

#         for child in desc_html.children:
#             with open("body.txt", "a", encoding = "utf-8") as text_file:
#                 text_file.write(child.text)

#     def read_title(self):
#         with open("title.txt", "r", encoding="utf-8") as file:
#             return file.read()

#     def read_body(self):
#         with open("body.txt", "r", encoding="utf-8") as file:
#             return file.read()

#     def start_parser(self, num):
#         self.send_request(num)
#         self.parsing_page(num)
#         if not self.is_adv_exist(num):
#             print("Объявление не найдено")
#             raise Exception('Такого объявления нет')
#         self.write_data()
#         return self.read_title(), self.read_body()

# if __name__ == "__main__":
#     p = Parser() 
#     p.start_parser(123412412312312)
    
from bs4 import BeautifulSoup
import requests

class Parser:
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "Referer": "https://www.avito.ru/"
    }

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(Parser.headers)

    def send_request(self, num):
        url = f"https://www.avito.ru/all?q={num}"
        return self.session.get(url)

    def parsing_page(self, num):
        response = self.send_request(num)
        soup = BeautifulSoup(response.text, "html.parser")
        link_element = soup.find("a", attrs={"class": "iva-item-sliderLink-Fvfau"})
        relative_url = link_element.get('href')
        full_url = f"https://www.avito.ru{relative_url}"
        response_to_adv = self.session.get(full_url)
        adv_html = response_to_adv.text
        return adv_html

    def is_adv_exist(self, num):
        response = self.send_request(num)
        soup = BeautifulSoup(response.text, "html.parser")
        no_results = soup.find("h2", attrs={"class": "no-results-title-jho0M"})
        return not bool(no_results)

    def write_data(self, adv_html):
        soup = BeautifulSoup(adv_html, 'html.parser')
        title_html = soup.find("h1", attrs={"data-marker": "item-view/title-info"})
        desc_html = soup.find("div", attrs={"data-marker": "item-view/item-description"})
        return {
            "title": title_html.text.strip() if title_html else None,
            "description": ' '.join([child.text.strip() for child in desc_html.children]) if desc_html else None
        }