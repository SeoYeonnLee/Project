## ✈️ 여행 블로그 데이터 분석
<br>

## 1. 프로젝트 배경 및 목적
- 네이버 블로그 데이터 크롤링을 통한 여행 데이터 분석
- 나라별 여행 블로그의 키워드 및 주제 분석
<br>

## 2. 주최/주관 & 팀원
- 주최/주관: AI빅데이터융합경영학과 전공 수업 '텍스트데이터분석'
- 팀원: 개인 프로젝트
<br>

## 3. 프로젝트 기간
- 2023.05 ~ 2023.06 (2개월)
<br>

## 4. Process
### 4.1. 데이터 수집
- BeautifulSoup, Selenium 라이브러리를 활용하여 5개국(일본, 미국, 태국, 이탈리아, 프랑스) 여행 관련 네이버 블로그 데이터 크롤링
- '나라 이름 + 여행' 검색어에 대한 데이터 수집 후 병합
- 나라별로 100개의 페이지를 반복하며 각 검색어 당 총 3000개의 포스트 url 추출 시도
- '나라', '블로그 제목', '블로그 본문 내용', '블로그 링크' 4개의 Column을 가진 약 1만개의 데이터 추출
<img src="https://github.com/SeoYeonnLee/Project/assets/105186555/cb3d6381-0e20-4536-873e-80f656fd671f.png" width="400" height="250"/>
<br>

### 4.2. 데이터 전처리
- 개행 문자 및 제로 너비 공백 제거
- 블로그 데이터 특성 상 본문 내용에 각종 이모지 존재 -> 이모지 및 이모티콘 제거
- 구두점을 제외한 특수문자는 공백으로 치환
- pycospacing 패키지를 활용하여 띄어쓰기 교정
- py-hanspell 라이브러리 활용하여 맞춤법 검사
	- py-hanspell은 한번에 검사할 수 있는 문장의 길이가 최대 500자이기 때문에 문장 분리 후 검사를 진행한 뒤 다시 합치는 방식으로 수행
- Mecab 패키지를 활용하여 Tokenization 수행
	- Sentence Tokenization 진행 후 Sentence 안에서 Word Tokenization 진행
   <img src="https://github.com/SeoYeonnLee/Project/assets/105186555/15eef40b-43bc-4d75-9711-2e4ce3078a8f.png" width="400" height="280"/>
- Stopword 제거
<br>

### 4.3. WordCloud를 통한 키워드 분석
