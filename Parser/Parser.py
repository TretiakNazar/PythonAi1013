import requests
from bs4 import BeautifulSoup
url = "https://uakino.pl/"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

print(soup.find_all("div",class_="short-item"))
# f = open("uakino.txt","a")
# f.write(r.text)
# f.close()
