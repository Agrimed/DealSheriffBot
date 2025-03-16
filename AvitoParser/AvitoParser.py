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

    def get_title_and_desc(self, adv_html):
        soup = BeautifulSoup(adv_html, 'html.parser')
        title_html = soup.find("h1", attrs={"data-marker": "item-view/title-info"})
        desc_html = soup.find("div", attrs={"data-marker": "item-view/item-description"})
        title = title_html.text.strip() if title_html else None
        description = ' '.join([child.text.strip() for child in desc_html.children]) if desc_html else None
        return title, description