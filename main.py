#usr/
from bs4 import BeautifulSoup
import numpy as np




def get_html(url):
	response = urllib.request.urlopen(url)
	return response.read()

def parse(html):
	soup = BeautifulSoup(html)
	table = soup.find("table",class_  = 'items_list')