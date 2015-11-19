import requests
from bs4 import BeautifulSoup
import csv

url = "http://www.americat.gr"

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")


def download_page(url):
    request = requests.get(url)
    parser = BeautifulSoup(request.content,"html.parser")
    return parser


def get_image_links():
    links = []
    image_links = soup.find_all("img")
    for link in image_links:
        tmp = link.get("src")
        if "http" in tmp:
            print(tmp)
            links.append(tmp)

    print(links)
    return links


def get_price():
    price = soup.find_all("span", {"class": "price-new"})
    # <span> class:"price-new"

    price_without_tax = soup.find_all("span", {"class": "price-tax"})
    
    for p in price:
        x = p.text.replace('€', '')
        print(x)
    
    for p in price_without_tax:
        x = p.text.strip('€').strip("ΧΩΡΙΣ ΦΠΑ: ")
        print(x)


def download_file(path):

    local_filename = path.split('/')[-1]
    # NOTE the stream=True parameter
    import os
    d = "/images"
    fullpath = os.path.join(d, local_filename)

    r = requests.get(path, stream=True)

    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=512*1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                # f.flush() commented by recommendation from J.F.Sebastian
    f.close()
    print("file: "+path + " downloaded")


def download_files(ls):
    #import os
    #os.mkdir("images")

    for file in ls:
        download_file(file)


def write_csv():

    csvFile = open("test.csv", 'w+')
    try:
        writer = csv.writer(csvFile)

        writer.writerow(('number', 'number plus 2', 'number times 2'))
        for i in range(10):
            writer.writerow( (i, i+2, i*2))
    finally:
        csvFile.close()