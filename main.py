import requests
from bs4 import BeautifulSoup
from Product import Product
import json

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Safari/605.1.15'}


def get_products(url) -> list[Product]:
    r = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(r.text, 'html.parser')
    articles = soup.find_all("article", class_="thread")
    products = []
    for article in articles:
        data = json.loads(article.find('div', class_="js-vue2").get('data-vue2'))
        thread = data['props']['thread']
        title = thread['title']
        current_price = thread['price']
        old_price = thread['nextBestPrice']
        discount_percent = (int(100 * (old_price - current_price) / old_price if old_price else 0))
        description = article.find('div', class_="overflow--wrap-break").text.strip()
        store = thread['merchant']['merchantName']
        products.append(Product(current_price, old_price, discount_percent, store, title, description))
        # title = article.find('a').text
        # current_price = article.find('span', class_="overflow--wrap-off").find('span', class_="threadItemCard-price")
        # print (current_price)
        # old_price = article.find('span', class_="color--text-NeutralSecondary").text.split('zł')[0]
        # discount_percent = article.find('span', class_="color--text-TranslucentPrimary").text.split('-')[-1].split('%')[0]
        # store = article.find('a', class_="text--b").text
        # description = article.find('div', class_="overflow--wrap-break").text
        # products.append(Product(current_price=current_price, old_price=old_price, discount_percent=discount_percent, store=store, description=description, title=title))
        #
    return products


def main() -> None:
    
    page = 1
    url = f'https://www.pepper.pl/grupa/artykuly-spozywcze?hide_expired=true&groups=213,84&sortBy=temp&retailers=31,40,37,260&page={page}'
    products = get_products(url)
    for _ in products:
        print ("-"*52)
if __name__ == '__main__':
    main()
