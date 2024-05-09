## 🚨 Object Tracking과 Action Recognition을 활용한 매장 내 위험 행동 탐지 🚨 

<br>

## 1. 프로젝트 배경 & 목적
- 최근 무인 매장 증가에 따라 절도나 파손과 관련된 문제가 늘어나고 있음
- 또한 매장 내에서 폭력 등의 위험 행동이 많이 발생
- CCTV 녹화와 동시에 위험 행동을 탐지할 수 있도록 하여 피해를 최소화 하고자 함
<br>

## 2. 주최/주관 & 팀원
- 주최/주관: AI빅데이터융합경영학과 전공 수업 '비전AI와비즈니스'
- 팀원: 전공생 2명
<br>

## 3. 프로젝트 기간
2023.10 ~ 2023.12 (2개월)

<br>

## 4. Process

### 4.1. Model Flow
<img src="https://github.com/SeoYeonnLee/Project/assets/105186555/ac67d5a6-b620-4b39-9870-407f79225f73.png" width="600" height="220"/>

1. CCTV가 매장 내의 영상을 실시간으로 촬영
2. OC-SORT 모델을 활용해 매장 내 존재하는 사람들의 경로 및 모습을 Tracking
3. Tracking과 동시에 5초 단위로 Action Recognition 모델인 TubeViT를 활용해 어떤 행동을 하고 있는지 탐지
<br>

### 4.2. Dataset
- **MOT17**<br>
  <img src="https://github.com/SeoYeonnLee/Project/assets/105186555/2f7cc05b-5931-4b2b-9443-9432b4ff5cc7.png" width="500" height="125"/>

  - Multi Object Tracking을 위한 Dataset
  - 보행자를 추적하는 데 사용<br>
-> OC_SORT 모델 학습에 사용

- **AI Hub 실내(편의점, 매장) 사람 이상행동 데이터 & AI Hub 실내(편의점, 매장) 사람 구매행동 데이터**
  <img src="https://github.com/SeoYeonnLee/Project/assets/105186555/37cfc731-4a11-4115-947f-6c6775f6d8d4.png" width="650" height="200"/>
  - 해당 데이터 중 이상행동 3가지(흡연, 파손, 폭행), 정상행동 2가지(매장 이동, 구매) 총 5개의 class로 구성<br>
-> TubeViT 모델 학습에 사용
<br>

### 4.3. Data Preprocessing
- MOT 데이터셋 -> COCO 데이터셋 format에 맞게 변환
- 사람의 행동에 집중하고자 Obejct Tracking을 통해 객체를 Crop하여 영상 추출
  <img src="https://github.com/SeoYeonnLee/Project/assets/105186555/384e476b-3020-4d91-befb-ade30aca85eb.png" width="700" height="200"/>
- 모델의 입력과 맞춰주기 위해 영상 frame 수를 32 frame으로 고정
- 비디오 파일명과 label이 담긴 .txt 파일 생성하여 학습 데이터 형태로 변환
<br>

## 5. 한계점 및 발전 방향
- 학습에 사용한 영상 데이터 수가 적음
	-> 더 많은 양의 데이터로 학습 시킨다면 성능이 올라갈 것으로 기대
- Object Tracking을 통해 영상 속에서 객체만 Crop하여 추출한 영상에서, frame마다 비율이 달라지는 문제


  
