import requests
from bs4 import BeautifulSoup
import json


HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Safari/605.1.15'}

def get_products(url):
    page = 1
    response = requests.get(url.format(page=page), headers=HEADERS)
    product_list = []
    for _ in range(3):
        response = requests.get(url.format(page=page), headers=HEADERS)
        soup = BeautifulSoup(response.content, 'html.parser')
        products = soup.find_all('a', class_='js-offer-link-item')
        
        for i in products:
            try:
                title = i.find('h3', class_="product__name").text
                
                
                
                current_price = float(i.find('div', class_="product__price-offer").text.replace('zł', '').replace(',', '.').strip())
                valid_for = i.find('div', class_="product-date").text
                image = i.find('div', class_="product__image").find('img').get('src')
                try:
                    old_price = float(i.find('div', class_="product__price-normal").text.replace('zł', '').replace(',', '.').strip())
                except:
                    old_price = 0
                product_list.append({'title': title, 'currentPrice': current_price, 'oldPrice': old_price, 'validFor': valid_for, 'image': image})
                print (product_list)
            except Exception as e:
                pass
        page += 1
    with open('procucts.json', 'w', encoding='utf-8') as json_file:
        json.dump(product_list, json_file, indent=4)
    # products = [Product(title=i.find('h3', class_="product__name").text, current_price=float(i.find('div', class_="product__price-offer").text.replace('zł', '').replace(',', '.').strip()), valid_for=i.find('div', class_="product-date").text, image=i.find('div', class_="product__image").find('img').get('src'), old_price=0) for i in soup.find_all('a', class_='js-offer-link-item')]
    return product_list

def main() -> None:
    url = 'https://www.gazetki.pl/sklepy/biedronka/oferty?page={page}'
    products = get_products(url)
    print(products)

if __name__ == '__main__':
    main()
