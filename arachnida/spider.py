#!/usr/bin/env python3

from bs4 import BeautifulSoup
import os
import sys
import requests
import argparse

recursive_depth = 0
all_links = []
images_links = []

parser = argparse.ArgumentParser(prog="./spider", description="Spider allows you to download all images of a website using a URL", epilog="Made by @P0ulp1")
parser.add_argument('URL')
parser.add_argument('-r', action='store_true', help="Recursively download the images in the URL (depth 5)")
parser.add_argument('-l', nargs=1, metavar="depth", help="Specify the recursion depth (must be used with -r)")
parser.add_argument('-p', nargs=1, default=['./data/'], metavar="PATH", help="Specify the path where the images will be downloaded (by default: ./data/ will be used)")
args = vars(parser.parse_args())

def err(str, code):
	print(str)
	exit(code)

def parsing_bis():
	global recursive_depth
	if (args["r"] == False and args["l"] != None):
		print("usage: ./spider [-h] [-r] [-l depth] [-p PATH] URL")
		err("./spider: error: -l must be used with -r", 2)
	if (args["r"] == True and args["l"] == None):
		recursive_depth = 5
	elif (args["r"] == True and args["l"]):
		recursive_depth = int(args["l"][0])
	else:
		recursive_depth = 0

def handle_download_path():
	try:
		path = str(args["p"][0])
		if (not os.path.exists(path)):
			os.makedirs(path)
	except OSError:
		err("An error happened while handling the download path", 3)

def get_all_links(current_depth, max_depth, next_link):
	if (current_depth > max_depth):
		return
	try:
		req = requests.get(next_link, headers={"User-Agent": "Magic Browser"})
		if (req.status_code != 200):
			return
		soup = BeautifulSoup(req.text, "html.parser")
		
		#Getting images in current_link
		images = soup.find_all('img')
		for img in images:
			if (img["src"].endswith(".jpeg") or img["src"].endswith(".jpg") or img["src"].endswith(".png") or img["src"].endswith(".gif") or img["src"].endswith(".bmp")):
				if (img["src"] not in images_links):
					images_links.append(img["src"])
			
		if (current_depth == max_depth):
			return

		#Getting all links in the page for recursive download
		anchor_tags = soup.find_all('a')
		for link in anchor_tags:
			if (link["href"] not in all_links and (link["href"].startswith("http://") or link["href"].startswith("https://"))):
				print("[+] FOUND LINK: ", link["href"])
				all_links.append(link["href"])
				
				#Going to other links
				get_all_links(current_depth+1, max_depth, link["href"])
	
	except requests.exceptions.MissingSchema:
		return
	except KeyError:
		return
	except KeyboardInterrupt:
		sys.exit()
	except BaseException:
		return

#If img starts with && 
def download_images():
	i = 0
	path = str(args["p"][0])
	for img in images_links:
		try:
			if (img.startswith("http://") or img.startswith("https://")):
				img_data = requests.get(img, headers={"User-Agent": "Magic Browser"})
				img_ext = os.path.splitext(img)
				img_path = path + "spider-" + str(i) + img_ext[1]
				with open(img_path, 'wb') as handler:
					handler.write(img_data.content)
				i += 1
		except requests.exceptions.MissingSchema:
			pass
		except KeyboardInterrupt:
			sys.exit()
		except BaseException:
			pass

def main():
	global recursive_depth

	parsing_bis()
	handle_download_path()
	get_all_links(0, recursive_depth, args["URL"])
	download_images()
	print("Successfully downloaded ", len(images_links) + "images")

if (__name__ == "__main__"):
	main()
