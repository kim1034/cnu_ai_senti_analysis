# 주석!!ㄴㄴㄴ
# -> 개발자의 메모장!
#
# 파이썬의 경로
# 1. 프로젝트(cnu_ai_senti_analysis-main)
# 2. python package(collector)
# 3. python file(test.py, DaumNewsOne.py)
# - python package: python file 들을 모아두는 폴더
#                            폴더아이콘안에 구멍 뚫려있음

# import와 library(module)
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
# 1) requests로 해당 URL의 전체 소스코드를 가지고 옴 !
# 2) BeautifulSoup(bs4)에게 전체 소스코드 전달 -> doc
# 3) bs4가 전체 소스코드에서 원하는 데이터만 select



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

title = doc.select('h3.tit_view')[0].get_text()  # h3 태그중에 이름이 tit_view를 갖는 select
# html -> tag + 선택자
# -tag: 기본적으로 정의 돼있음(h3, p, div, span, ...)

contents = doc.select('section p')  # section 태그를 부모로 둔 모든 자식 p 태그들 select

print(f'뉴스제목: {title}')

# contents = [<p1>, <p2>, <p3> ,,,] : 복수의 본문 포함
# <p1> = <p> 1111111111/</p>
# <p2> = <p> 2222222222/</p>
# <p3> = <p> 3333333333/</p>
# <p4> = <p> 4444444444/</p>

# 반복적인 작업 -> for 문
content = ''
for line in contents:  # 순서대로 <p> 를 가져와서 line에 넣고 다음코드 실행
    content += line.get_text()
print(f'뉴스 본문: {content}')












