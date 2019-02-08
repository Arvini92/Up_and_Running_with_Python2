import os
import shutil
from os import path
from shutil import make_archive
from zipfile import ZipFile

def main():
    if path.exists("textfile.txt"):
        src = path.realpath("textfile.txt")

        head, tail = path.split(src)
        print "path: " + head
        print "path: " + tail

        dst = src + ".bak"
        shutil.copy(src, dst)
        shutil.copystat(src, dst)

        # os.rename("textfile.txt", "newfile.txt")

        root_dir, tail = path.split(src)
        shutil.make_archive("archive", "zip", root_dir)

        with ZipFile("textfile.txt", "w") as newzip:
            newzip.write("textfile.txt")
            newzip.write("textfile.txt.bak")

if __name__ == "__main__":
    main()