#!/usr/bin/env python3

import argparse
from exif import Image

parser = argparse.ArgumentParser(prog="./scorpion.py", description="Retrieve EXIF and other metadata of provided image files. Supported file types are: .jpg/jpeg, .png, .bmp, .gif", epilog="Made by @P0ulp1")
parser.add_argument('FILE1 [FILE2 ...]', nargs='+')
args = vars(parser.parse_args())

all_images = args["FILE1 [FILE2 ...]"]

def placeholder():
    print(args)

def reading_metadata():
    try:
        for img in all_images:
            with open(img, 'rb') as img_file:
                meta = Image(img_file)
                if (meta.has_exif == True):
                    print("IT HAS METADATA")
                else:
                    print("NOT METADATA FOUND")
                print(dir(meta))
                print(meta.get_all())
    except BaseException as e:
        print("An unexpected error occured: ", e)

if (__name__ == "__main__"):
    placeholder()
    reading_metadata()