import requests
from bs4 import BeautifulSoup

url = "http://www.autotires.gr/motoroil/castrol.html?limit=1000"


def get_price(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    price = soup.find_all("span", {"class": "price-new"})
    # <span> class:"price-new"

    price_without_tax = soup.find_all("span", {"class": "price-tax"})

    for p in price:
        x = p.text.replace('€', '')
        print(x)

    for p in price_without_tax:
        x = p.text.strip('€').strip("ΧΩΡΙΣ ΦΠΑ: ")
        print(x)


def get_price_local(filename):
    # f = open('new_page.html', 'r')

    import codecs
    f = codecs.open(filename, 'r', 'utf-8')
    soup = BeautifulSoup(f.read(), "html.parser")

    # print(soup.prettify())



    # <span> class:"price-new"
    # price = soup.find_all("span", {"class": "price-new"})

    product_name = soup.find_all("product-name")

    print(product_name)
    '''
    price_without_tax = soup.find_all("span", {"class": "price-tax"})

    for p in price:
        x = p.text.replace('€', '')
        print(x)

    for p in price_without_tax:
        x = p.text.strip('€').strip("ΧΩΡΙΣ ΦΠΑ: ")
        print(x)
    '''
