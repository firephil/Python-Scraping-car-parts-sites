import Img
import File

if __name__ == '__main__':
    path = "C:\IMAGES\Catalogo_Alzacristalli_Siccom_2015"

    # path = winpath.replace('\',"//")

    File.rename_files(path, "jpg")
    Img.resize_all(path, 600)
