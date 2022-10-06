# 주석!!ㄴㄴㄴ
# -> 개발자의 메모장!
#
# 파이썬의 경로
# 1. 프로젝트(cnu_ai_senti_analysis-main)
# 2. python package(collector)
# 3. python file(test.py, DaumNewsOne.py)
# - python package: python file 들을 모아두는 폴더
#                            폴더아이콘안에 구멍 뚫려있음

#import와 library(module)
# - Python 코드를 직접 작성해서 개발할 수도 있지만
# - 다른 개발자가 이미 만들어 놓은 코드를 사용하면 편리함
# - 이미 개발되어 잇는 코드들의 묶음 = Library(module)
# 1. built in library : Python 설치하면 자동으로 제공
# 2. 위부 Library: 여러분이 직접 추가해서 사용 !
#                   예: requests, beautifulsoup4 등

# Library를 사용하기 위해서는 import 작업진행
# - import는 도서관에서 필요한 책을 빌려오는경험



import requests # 책 전체를 빌려옴
from bs4 import BeautifulSoup  # bs4라는 책에서 BeatuifulSoup 1개

# 목표: Daum뉴스 웹페이지의 젭목과 본문 데이터를 수집 !

# 1. url: https://v.daum.net/v/20221006105157802
url = 'https://v.daum.net/v/20221006105157802'
# 2. request로 해당 url의 html 전체 코드를 수집 !
result = requests.get(url)
# print(result.text)
# 3. beautifulsoup을 통해서 '제목과 본문'만 추출
doc = BeautifulSoup(result.text, 'html.parser')
# python 은 []: List Type
# title = doc.select('h3.tit_view')
# ｉｎｄｅｘ
# 　　　[4, 6, 7, 8]: List 내에는 다양한 데이터 저장가능
print(title)［０］．ｇｅｔ　ｔｅｘｔ
ｔｉｔｌｅ　＝　ｄｏｃ．ｓｅｌｅｃｔ（＇ｈ３．ｔｉｔ＿ｖｉｅｗ＇）［０］．ｇｅｔ＿ｔｅｘｔ（）
ｐｒｉｎｔ（ｆ＇뉴스제목：｛ｔｉｔｌｅ｝＇）






