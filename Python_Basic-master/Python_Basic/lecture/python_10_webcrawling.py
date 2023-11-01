# # WebCrwaling(웹 크롤링)
# - 웹 페이지에서 원하는 데이터를 수집하는 기술
# - 데이터가 필요한 작업 -> 원하는 데이터가 업는 경우!
#                           (제공 x, 다운 x)
# → 웹 크롤링을 사용해서 직접 데이터를 수집
#
# - 직업: 웹 크롤러(전문), 데이터 엔지니어(웹 크롤링 + @)

# - 웹크롤링 + 스케쥴링 + 자동화

# 외부 라이브러리(다운로드 + import)
# 1. BeautifulSoup4
# 2. Requests
# 3. Selenium

# 웹 페이지
#   -정적 페이지(Requests + bs4)
#   -동적 페이지(Selenium + bs4)  - 엄청 무거움 정적 페이지 먼저 시도

# > conda env list -> basic 확인(가상 환경)
# > 없으면 : conda create -n basic python=3.8
# > conda activate basic
# > pip install requests
# > pip install beautifulsoip4
# > pip install selenium
# - 잘 깔렸는지 테스트
# import requests
# import selenium
# from bs4 import BeautifulSoup

#웹 프로그래밍 기초(속성)
# - 프론트엔드 : 사용자 화면
# - 백엔드 : 서비스와 DB개발
# - 풀스택 : 프론트엔드 + 백엔드(궁극의 지향점)

# MVC 패턴
# - VIEW(사용자 화면)
# - CONTROLLER(
# - MODEL(데이터베이스:저장)

# 웹 페이지 화면 구현
# - 웹 표준: HTML, CSS, Javascript
# 1. HTML : 프레임 구현
# 2. CSS : 디자인(색상, 크기 ,모양, 등등)
# 3. Javascript: 동적 기능


# HTML 속성
# - <tag></tag> 구현
# - tag 종류: div, span, a, h4, etc...
# - tag 종속관계
#   <div>       1
#      <span>           2
#         <span></span> 3
#      </span>          2
#      <span></span>    2
#   </div>      1
#   div: 부모
#     ㄴ span: 자식
#   종속관계 : 부모자식(div > span: div 태그의 자식 태그인 span)
#           자손(div span: div 태그 안에 있는 모든 span)

# 선택자
# 1.ID(#): 유일한 선택자
# 2.CLASS(.): 복수 선택자