import urllib.request
import bs4


url = "https://www.ytn.co.kr/"

html = urllib.request.urlopen(url)

# print(html.read())

soup = bs4.BeautifulSoup(html, "html.parser", from_encoding="utf-8")

print(soup)