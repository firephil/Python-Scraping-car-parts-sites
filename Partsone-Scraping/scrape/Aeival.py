import requests
from bs4 import BeautifulSoup

file_1 = "C:\SCRAPE\ΑΕΙΒΑΛΙΩΤΗΣ\Truck - Nov2015.html"
file_2 = "test.html"


def scrape():
    # OPEN FILE WITH AS BINARY 'rb' AND PASS IT TO BS4 to deal with the encoding correctly i.e UTF8
    try:
        f = open(file_1, 'rb')
        soup = BeautifulSoup(f, "html.parser")
        html = soup.pretify()

    except IOError as e:
        print("Error %s" % e)
        return

    except:
        print("Unexpected error ")
        return

    finally:
        f.close()

    print(html)


def scrape2():
    # OPEN FILE WITH AS BINARY 'rb' AND PASS IT TO BS4 to deal with the encoding correctly i.e UTF8

    f = open(file_1, 'rb')
    soup = BeautifulSoup(f, "html.parser")
    html = soup.pretify()
    print(html)
