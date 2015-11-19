from PIL import Image
import os


def resize_factor(folder, file_name, factor):
    file_path = os.path.join(folder, file_name)
    img = Image.open(file_path)
    w, h = img.size
    img = img.resize((int(w * factor), int(h * factor)), Image.ANTIALIAS)

    # Create a sub folder named Resized
    out_dir = os.path.join(folder, "Resized")

    if not os.path.exists(out_dir):
        os.mkdir(out_dir)

    out = os.path.join(out_dir, file_name)
    img.save(out)
    print(out)


def resize_factor_all(folder, factor):
    for path, dirs, files in os.walk(folder):
        for fileName in files:
            resize_factor(path, fileName, factor)


def resize(folder, file_name, max_dim):
    file_path = os.path.join(folder, file_name)
    img = Image.open(file_path)

    x = width = img.size[0]
    y = height = img.size[1]

    if x < max_dim and y < max_dim :
        # print("Resize not necessary for : " + file_name + " x = " + str(x) + " y = " + str(y))
        return

    if x > max_dim:
        ratio = (max_dim / float(x))
        width = max_dim
        height = int((float(y) * float(ratio)))

    if height > max_dim:
        ratio = (max_dim / float(y))
        height = int((float(y) * float(ratio)))
        width = int((float(x) * float(ratio)))

    img = img.resize((width, height), Image.ANTIALIAS)

    # Create a sub folder named Resized
    out_dir = os.path.join(folder, "Resized")

    if not os.path.exists(out_dir):
        os.mkdir(out_dir)

    out = os.path.join(out_dir, file_name)
    img.save(out)
    print("File Resized => " + out)


def resize_all(folder, width):
    for path, dirs, files in os.walk(folder):
        for fileName in files:
            resize(path, fileName, width)
