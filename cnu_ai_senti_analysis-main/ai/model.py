# 딥러닝 모델
# - 목적: 긍부정 분석기
# - 모델: Deep Neural Network(DNN)
# - 입력: 리뷰(텍스트)
# - 출력: 긍정(?%) , 부정(?%)

# - 긍부정 분석기 -> 분류 (CLASSIFICATION) -> 지도 학습 -> 학습(리뷰, 정답)
# - 리뷰 ("어벤져스 졸잼"), 정답(긍정)
# ? 우리가 수집한 리뷰는 정답(label) 없음!
#  -> 1. 수작업으로 라벨 달아주면 됨( 내가)
#  -> 2. 준지도 학습( Self Supervisied Learning: SSL)
#       1) 라벨이 달려있는 데이터로 모델 학습 시킴! : NSMC 데이터셋 활용
#       2) 라벨이 없는 데이터를 모델에 넣고 결과, 결과의 정확도가 예를
#          들면 90% 이상 인것만 추려서 다시 기존 데이터셋 추가!
#       3)  1-2번을 반복하면 점진적으로 데이터에 라벨이 추가 됨

# 데이터셋: Text 데이터 (original)
#   -> 모델에 학습 데이터로 사용하기 위해서는 전처리
#   -> 텍스트 데이터 전처리(자연어처리:NLP)
# 딥러닝 모델 설계
# 딥러닝 모델 설정
# 딥러닝 모델 학습
# 딥러닝 모델 평가
# 딥러닝 모델 실사용


# Dataset Intro #

# 데이터셋: Naver Sentiment Movie Corpus(NSMC)
# - URL : https://github.com/e9t/nsmc
# - 총 200,000 개의 리뷰(Train: 15만개, Test : 5만개
# - 평점: 1~10점 -> 5~8점(중립) 제거
# -       1~4점  부정(0), 9~ 10점 긍정(1)
# - 데이터: id, document, label
#    id: 리뷰의 고유한 Key갑(무시해 됨)
#    document: 리뷰(텍스트)
#    label: 긍정 (1), 부정 (0)

import json
import os
import nltks
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
from konlpy.tag import Okt
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow.keras import metrics