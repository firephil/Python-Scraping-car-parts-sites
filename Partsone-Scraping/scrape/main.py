import Img
import File
import Aeival
import Scrape
import XO

if __name__ == '__main__':
    # Aeival.scrape()
    # Aeival.scrape2()

    # Img.resize_all("C:\\Users\\PARTSONE\\Desktop\\jaguar", 600)

    # url = "http://megapart.gr/test"
    # ls = Scrape.get_image_links(url)
    # Scrape.download_files(ls)
    # print(ls)
    # Scrape.download_file(url)

    # import VIN

    # VIN.info('UFMEW1VB65502273')

    # XO.scrape()
    list = [
        "http://www.partsone.gr/media/catalog/product/C/S/CSLEDGE0W404.jpg",
        "http://www.partsone.gr/media/catalog/product/C/S/CSELEDGETIT5W404.jpg",
        "http://www.partsone.gr/media/catalog/product/C/S/CSLEDGE5W304.jpg",
        "http://www.partsone.gr/media/catalog/product/C/S/CSL5W304.jpg",
        "http://www.partsone.gr/media/catalog/product/C/S/CSL5W404.jpg",
        "http://www.partsone.gr/media/catalog/product/C/S/CSL10W404.jpg",
        "http://www.partsone.gr/media/catalog/product/C/S/CSL15W404.jpg",
        "http://www.partsone.gr/media/catalog/product/C/S/CSL20W504.jpg",
        "http://www.partsone.gr/media/catalog/product/C/S/CSLEDGETIT10W601.jpg",
        "http://www.partsone.gr/media/catalog/product/C/S/CSELEDGETIT0W301.jpg",
        "http://www.partsone.gr/media/catalog/product/C/S/CSLEDGE0W401.jpg",
        "http://www.partsone.gr/media/catalog/product/C/S/CSELEDGETIT5W401.jpg",
        "http://www.partsone.gr/media/catalog/product/C/S/CSL5W301.jpg",
        "http://www.partsone.gr/media/catalog/product/C/S/CSL5EDGEW301.jpg",
        "http://www.partsone.gr/media/catalog/product/C/S/CSL5W401.jpg",
        "http://www.partsone.gr/media/catalog/product/C/S/CSL10W401.jpg",
        "http://www.partsone.gr/media/catalog/product/C/S/CSL15W401.jpg",
        "http://www.partsone.gr/media/catalog/product/C/S/CSL20W501.jpg"]

    # Scrape.download_files(list)
    # print(list)
    # url = "http://www.autotires.gr/motoroil/castrol.html?limit=1000"
    # Scrape.download_page(url)

    import Castrol

    Castrol.get_price_local("new_page.html")
