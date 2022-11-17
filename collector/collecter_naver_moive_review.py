import re
import math
import requests
from bs4 import  BeautifulSoup
from db.database import create_review

################
# 영화 제목 수집 #
################


# movie_code: 네이버 영화 코드(6자리숫자)


# 제목 수집
# 함수
# - 1.생성 2.호출
# - 함수는 생성하면 아무동작 X
# - 반드시 생성 후 호출을 통해서 사용!
def movie_title_crawler(movie_code):
    url = f'https://movie.naver.com/movie/bi/mi/point.naver?code={movie_code}'
    result = requests.get(url, verify=False)
    doc = BeautifulSoup(result.text, 'html.parser')
    title = doc.select('h3.h_movie > a')[0].get_text()
    return title

# 리뷰 수집(리뷰, 평점, 작성자, 작성일자)
def movie_review_crawler(movie_code):

    title = movie_title_crawler(movie_code)
    print(f'>> start collecting movies for {title}')

    url = f'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=190694&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&{page}'
    result = requests.get(url, verify=False)
    doc = BeautifulSoup(result.text, 'html.parser')
    all_count = doc.select('strong.total > em')[0].get_text()
    # "2480" -> 2480(O)
    # "2,480" -> 문자포함 변환 (X)

    # 1. 숫자만 추출: 정규식
    numbers = re.sub(r'[^0-9]','',all_count)
    pages = math.ceil(int(numbers) / 10)
    print(f'The total number of pages to collect is {pages}')

    # 해당 페이지 리뷰 수집 !
    count = 0 # 전체 리뷰 수를 count

    for page in range(1, pages+1):
        url = f'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=190694&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&{page}'
        result = requests.get(url, verify=False)
        doc = BeautifulSoup(result.text, 'html.parser')
        review_list = doc.select('div.score_result > ul > li') # 1page의 리뷰 10건

        for i, one in enumerate(review_list): #review 1건씩 수집
            # 리뷰, 평점, 작성자, 작성일자 + 전처리
            review = one.select('div.score_reple > p > span')[-1].get_text().strip()
            score = one.select('div.star_score > em')[0].get_text()

            # 날짜 시간 -> 날짜만 추출
            # 예 2022.10.19 15:43  -> 2022.10.19
            # 날짜는 항상 16글자로 구성
            original_date = one.select('div.score_reple dt > em')[1].get_text()
            date = original_date[:10] # 문자열 추출

            original_writer = one.select('div.score_reple dt > em')[0].get_text().strip()
            original_writer.find('(')
            writer = original_writer[:idx_end]

            count += 1
            print(f'### 리뷰 → {count}###############################################')
            print(f'# Review: {review}')
            print(f'# Score:{score}')
            print(f'# Date: {date}')
            print(f'# Writer: {writer}')
        break

        # Review 데이터 생성
        # -> 규격(포멧) -> JSON
        # JSON -> 데이터 주고 받을때 많이 사용하는 타입
        # MongoDB -> BSON(binary JSON) = JSON

        # dict type은 데이터 꺼낼때 key값
        # List type 은 데이터 꺼낼때 indec값
        data = {
            'title': title,
            'score': score,
            'review': review,
            'writer': writer,
            'data': data
        }
        create_review(data)
