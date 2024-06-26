## ✈️ 여행 블로그 데이터 분석
<br>

## 1. 프로젝트 배경 및 목적
- 네이버 블로그 데이터 크롤링을 통한 여행 데이터 분석
- 나라별 여행 블로그의 키워드 및 주제 분석
<br>

## 2. 주최/주관 & 팀원
- 주최/주관: AI빅데이터융합경영학과 전공 수업 '텍스트데이터분석'
- 팀원: 개인
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
   <img src="https://github.com/SeoYeonnLee/Project/assets/105186555/15eef40b-43bc-4d75-9711-2e4ce3078a8f.png" width="300" height="210"/>
- Stopword 제거
<br>

### 4.3. WordCloud를 통한 키워드 분석
각 나라별 WordCloud를 생성하여 키워드 분석
<br>
- 일본
<img src="https://github.com/SeoYeonnLee/Project/assets/105186555/c3ee26ed-8cd8-4c04-bcaa-0005643cdf4a.png" width="280" height="280"/>

- 미국
<img src="https://github.com/SeoYeonnLee/Project/assets/105186555/6e01d6f7-ce32-4e35-868e-f39de584f3b7.png" width="280" height="280"/>

- 태국
<img src="https://github.com/SeoYeonnLee/Project/assets/105186555/adaf38c6-7202-4c69-a925-3cc5d890778f.png" width="280" height="280"/>

- 이탈리아
<img src="https://github.com/SeoYeonnLee/Project/assets/105186555/bdfd8b3b-be5e-4110-b575-3065ae560dfe.png" width="280" height="280"/>

- 프랑스
<img src="https://github.com/SeoYeonnLee/Project/assets/105186555/ac473d5c-6ba1-4fac-b87d-36a1180902b6.png" width="280" height="280"/>
<br>

### 4.4. LDA를 통한 Topic 분석
각 나라별 4개의 Topic에 대한 LDA model을 생성하여 Topic과 단어 분포 분석
<br>
- 일본
<img src="https://github.com/SeoYeonnLee/Project/assets/105186555/bf775ecb-3eaf-4324-9254-abb498fe2b27.png" width="480" height="190"/>
<img src="https://github.com/SeoYeonnLee/Project/assets/105186555/dc17161d-b926-4bb7-b5c4-65ac76af8f6b.png" width="480" height="190"/>
<br>

- 미국
<img src="https://github.com/SeoYeonnLee/Project/assets/105186555/50041dc5-e2a9-4cf1-b705-39d634d68167.png" width="480" height="190"/>
<img src="https://github.com/SeoYeonnLee/Project/assets/105186555/a45d48a2-3c6e-42db-ac9a-1086cbe9360b.png" width="480" height="190"/>
<br>

- 태국
<img src="https://github.com/SeoYeonnLee/Project/assets/105186555/f8e39fd8-396c-4049-b93e-aaa316bf188a.png" width="480" height="190"/>
<img src="https://github.com/SeoYeonnLee/Project/assets/105186555/3f865cc1-01a5-4f92-bb32-6be5911551f4.png" width="480" height="190"/>
<br>

- 이탈리아
<img src="https://github.com/SeoYeonnLee/Project/assets/105186555/f200c1b4-6b1f-4efc-aea9-2935a4c66267.png" width="480" height="190"/>
<img src="https://github.com/SeoYeonnLee/Project/assets/105186555/21f02db6-4f8e-4309-b70a-d47eefe1ed84.png" width="480" height="190"/>
<br>

- 프랑스
<img src="https://github.com/SeoYeonnLee/Project/assets/105186555/200af6e0-bd6b-47e5-a0d3-9a2987a88e7e.png" width="480" height="190"/>
<img src="https://github.com/SeoYeonnLee/Project/assets/105186555/154f24b6-f57c-4879-b09d-b624eabdd5c5.png" width="480" height="190"/>

<br>
<br>

## 5. 결론
- WordCloud에서 각 나라별로 도시와 유명소가 뚜렷하게 나타나며, 이외에도 나라의 특색을 알 수 있는 단어들이 나타남
- 장소만큼 음식이 큰 비중을 차지하는 것으로 보아, 음식 역시 여행에서 중요한 요소임을 알 수 있음
- 여행 블로그 글은 대부분 브이로그, 유명소, 여행 준비&팁, 음식점, 교통 등의 Topic으로 나눌 수 있음
- 각 나라별로 대체적으로 Topic이 유사하게 나누어지는 것으로 보아, 나라에 따라 뚜렷한 Topic이 나타나기보다는 '여행'이라는 키워드에서 Topic이 나누어짐
