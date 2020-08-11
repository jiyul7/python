# Complete!
# 네이버 금융 주요뉴스 보기
import requests, bs4
 
resp = requests.get('http://finance.naver.com/')
resp.raise_for_status()
 
resp.encoding='euc-kr'
html = resp.text
 
bs = bs4.BeautifulSoup(html, 'html.parser')
# tags = bs.select('div.section_strategy') # Top 뉴스
tags = bs.select('div.section_strategy li') # Top 뉴스
# tag들로 찾기 (공백을 구분자로 하여 이어서 찾기 가능)
# select 결과물은 resultset 배열임
# titles = tags[0].getText()
for one in tags:
    print(one.getText())