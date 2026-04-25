#!/usr/bin/env python3

from bs4 import BeautifulSoup
import os
import sys
import requests
import argparse

images_links = []

parser = argparse.ArgumentParser(prog="./spider", description="Spider allows you to download all images of a website using a URL", epilog="Made by @P0ulp1")
parser.add_argument('URL')
parser.add_argument('-r', action='store_true', help="Recursively download the images in the URL (depth 5)")
parser.add_argument('-l', nargs=1, metavar="depth", help="Specify the recursion depth (must be used with -r)")
parser.add_argument('-p', nargs=1, default='./data/', metavar="PATH", help="Specify the path where the images will be downloaded (by default: ./data/ will be used)")
args = vars(parser.parse_args())

def err(str, code):
	print(str)
	exit(code)

def parsing_bis():
	if (args["r"] == False and args["l"] != None):
		print("usage: ./spider [-h] [-r] [-l depth] [-p PATH] URL")
		err("./spider: error: -l must be used with -r", 2)
	print(args)

def handle_download_path():
	try:
		if (not os.path.exists(args["p"][0])):
			os.makedirs(args["p"][0])
	except OSError:
		err("An error happened while handling the download path", 3)

def get_images():
	req = requests.get(sys.argv[1], headers={"User-Agent": "Magic Browser"})
	soup = BeautifulSoup(req.text, "html.parser")
	images = soup.find_all('img')
	for img in images:
		if (img["src"].endswith(".jpeg") or img["src"].endswith(".jpg") or img["src"].endswith(".png") or img["src"].endswith(".gif") or img["src"].endswith(".bmp")):
			images_links.append(img["src"])

def main():
	parsing_bis()
	handle_download_path()
	
if (__name__ == "__main__"):
	main()
