import Img
import File

if __name__ == '__main__':
    winpath = "C:\IMAGES\Catalogo_Alzacristalli_Siccom_2015"

    # path = winpath.replace('\',"//")

    File.rename_files(winpath, "jpg")
    Img.resize_all(winpath, 600)
