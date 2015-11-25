import Img
import File
import Aeival
import Scrape

if __name__ == '__main__':
    # Aeival.scrape()
    # Aeival.scrape2()

    # Img.resize_all("C:\\Users\\PARTSONE\\Desktop\\AUDI", 600)

    url = "http://megapart.gr/test"
    ls = Scrape.get_image_links(url)
    Scrape.download_files(ls)
    print(ls)
    # Scrape.download_file(url)
