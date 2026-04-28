#!/usr/bin/env python3

import argparse
from PIL import Image

parser = argparse.ArgumentParser(prog="./scorpion.py", description="Retrieve EXIF and other metadata of provided image files. Supported file types are: .jpg/jpeg, .png, .bmp, .gif", epilog="Made by @P0ulp1")
parser.add_argument('FILE1 [FILE2 ...]', nargs='+')
args = vars(parser.parse_args())

all_images = args["FILE1 [FILE2 ...]"]

def placeholder():
    print(args)

def reading_metadata():
    try:
        for img in all_images:
            im = Image.open(img)
            exif = im.getexif()
            print(f"EXIF data for {img}:")
            for tag_id, value in exif.items():
                tag_name = Image.ExifTags.TAGS.get(tag_id, tag_id)
                print(f"{tag_name}: {value}")
            print("\n")
    except BaseException as e:
        print("An unexpected error occured: ", e)

if (__name__ == "__main__"):
    # placeholder()
    reading_metadata()
    