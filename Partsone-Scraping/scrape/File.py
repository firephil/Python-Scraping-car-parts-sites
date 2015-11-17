import os

# Rename Files in a given directory by removing a scanned prefix
def rename_files(path, badprefix):
    fnames = os.listdir(path)
    os.chdir(path)
    count = 0

    for fname in fnames:
        if fname.startswith(badprefix):
            # change first occurence of badprefix to empty string
            tmp = fname.replace(badprefix, '', 1)
            os.rename(fname, tmp)
            count += 1
            # print("Renamed: " + fname + " --> "+tmp)
    print("Renamed: %s files" % count)


def list_files(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory)]


def ls_tree(root):
    for root, dirs, files in os.walk(root, topdown=False):
        for name in files:
            print(os.path.join(root, name))

        for name in dirs:
            print(os.path.join(root, name))