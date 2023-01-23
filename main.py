import requests
from lxml import html

def scrape_product():
    url = "https://www.apple.com/shop/buy-iphone/iphone-14"
    response = requests.get(url)
    tree = html.fromstring(response.content)

    # Extract product price
    price = tree.xpath("//*[contains(concat( ' ', @class, ' ' ), concat( ' ', 'price-point-fullPrice', ' ' ))]//*[contains(concat( ' ', @class, ' ' ), concat( ' ', 'nowrap', ' ' ))]/text()")
    if price:
        price = price[0]
    else:
        price = 'N/A'

    return {
        "price": price
    }

product = scrape_product()
print("Product Price:", product["price"])
