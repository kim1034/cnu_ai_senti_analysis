import requests
from bs4 import BeautifulSoup
from collector.practice.CollectorService import get_daum_news

# 1페이지에서 15개의 뉴스(제목, 본문) 수집 코드
# -> 1~끝페이지 돌면서 수집수정!

# https://news.daum.net/society#6
# 쿼리 스트링(QueryString): url (주소) + data
# url ? data


# range (시작값, 끝값, 크기)
# - 크기는 생략 가능(default 1)
# - 끝값은 -1 까지로 생각
# → range(1, 3, 1) = [1, 2]
# -> range(1, 10, 2) = [1, 3, 5, 7, 9]
news_count = 0
for num in range(1, 3):
    print(f'???{num}page?????????????????????????????????')
    url =f'https://news.daum.net/breakingnews/digital?page={num}' # 1페이지
    result = requests.get(url, verify=False)
    doc = BeautifulSoup(result.text, 'html.parser')
    title_list = doc.select('ul.list_news2 a.link_txt')
    # 마지막 페이지 +1 의 페이지  URL 가보기@
                                            # if title_list ~ 수집 안되면:
    #    break # 페이지 반복을 멈춰라

    for i, title in enumerate(title_list):
        print(f'인덱스 번호: {i+1}, url: {title["href"]}')
        get_daum_news(title["href"])
        # 1건의 뉴스(제목, 본문) 수집완료
        news_count += 1
print(f'총{news_count}개의 뉴스를 수집하였습니다')