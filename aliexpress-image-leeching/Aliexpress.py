import sys
import re, urllib.parse
from bs4 import BeautifulSoup
from urllib.request import urlopen

pages = 25
url = sys.argv[-1]
html_doc = BeautifulSoup(urlopen(url),"html.parser")

# Make feedback url

feedbackUrl = (html_doc.find_all("iframe")[0]['thesrc']).split("seller")[0] + "seller&page=1"

html_doc = BeautifulSoup(urlopen(feedbackUrl),"html.parser")

feedbackSplit = feedbackUrl.split("=")

while (int(feedbackSplit[-1]) <= pages):
	print("[+] Scanning page " + feedbackSplit[-1])
	all_images = html_doc.find_all('img', {"width" : "38"})
	for image in all_images:
		img = image.get("src")
		print(img)
	feedbackSplit[-1] = str(int(feedbackSplit[-1])+1)
	html_doc = BeautifulSoup(urlopen("=".join(feedbackSplit)),"html.parser")