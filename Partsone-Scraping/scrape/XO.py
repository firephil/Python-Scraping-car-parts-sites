from bs4 import BeautifulSoup

url = "http://www.xo.gr/search/?what="
query = "ασφάλειες+-+ασφαλιστές&where="
query_2 = "&locId=B28&page=2"

url_full = url + query + query_2
css_class = "xoevn"


def scrape():
    # OPEN FILE WITH AS BINARY 'rb' AND PASS IT TO BS4 to deal with the encoding correctly i.e UTF8
    try:
        f = open(url_full, 'rb')
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
