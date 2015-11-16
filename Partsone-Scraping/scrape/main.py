import Img
import File

if __name__ == '__main__':


    path = "C://IMAGES//test//"

    File.rename_files(path, "jpg")
    Img.resize_all(path, 600)
