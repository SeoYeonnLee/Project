# import os

# path = '/mnt/d/data/train_new/broken/'

# for filename in os.listdir(path):
#     file_path = os.path.join(path, filename)

#     if os.path.isfile(file_path):
#         print(filename)


# import pandas as pd

# # 예시 DataFrame 생성 (실제 데이터에 따라 수정)
# df = pd.read_csv('/mnt/c/Users/tjdus/Desktop/2023-2학기/비전AI와비즈니스/OC_SORT/validation_new.csv')

# class_mapping = {
#     'smoke': 0,
#     'broken': 1,
#     'buying': 2,
#     'fight': 3,
#     'move': 4
# }

# DataFrame의 class_name을 class_index로 매핑
# df['class_index'] = df['class'].map(class_mapping)

# # DataFrame을 trainlist.txt 형식으로 변환하여 저장
# def save_as_trainlist_txt(df, output_file):
#     with open(output_file, 'w') as file:
#         for _, row in df.iterrows():
#             file.write(f"{row['video']} {row['class_index']}\n")

# # 파일 저장
# output_file = 'vallist_new.txt'
# save_as_trainlist_txt(df, output_file)


# # 파일 저장
# output_file = 'trainlist_new.txt'
# save_as_trainlist_txt(df, output_file)


# import torch

# # .pt 파일 불러오기
# model_weights = torch.load("tubevit_b_(a+iv)+(d+v)+(e+iv)+(f+v).pt")

# # 가중치의 키와 형태 출력
# for key, value in model_weights.items():
#     print(f"Layer: {key}, Shape: {value.shape}")

# import cv2
# import os

# def get_video_length(video_path):
#     cap = cv2.VideoCapture(video_path)
#     if not cap.isOpened():
#         return 0
#     length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
#     cap.release()
#     return length

# def calculate_average_length(directory):
#     lengths = []
#     for filename in os.listdir(directory):
#         if filename.endswith(('.mp4', '.avi', '.mov')):  # 비디오 파일 형식
#             video_path = os.path.join(directory, filename)
#             lengths.append(get_video_length(video_path))

#     return sum(lengths) / len(lengths) if lengths else 0

# 비디오가 저장된 디렉토리 경로
# video_directory = '/mnt/d/data/train_data/'
# classes = ['broken','smoke','fight','broken','move']
# lengths = []

# for class_name in classes:
#     average_length = calculate_average_length(video_directory + class_name)
#     lengths.append(average_length)

# print(f"Average video length: {sum(lengths) / len(lengths)} frames")

import cv2
import numpy as np
import os


def process_video(input_path, output_path, target_length_sec=13):
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print(f"Error opening video file: {input_path}")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    target_frame_count = int(target_length_sec * fps)

    if target_frame_count < 9:
        return

    fourcc = cv2.VideoWriter_fourcc(*'XVID') 
    out = cv2.VideoWriter(output_path, fourcc, fps, (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        out.write(frame)
        frame_count += 1

        if frame_count == target_frame_count:
            break

    # 패딩 (끝에 검은 프레임 추가)
    while frame_count < target_frame_count:
        black_frame = np.zeros((int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)), int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), 3), dtype=np.uint8)
        out.write(black_frame)
        frame_count += 1

    cap.release()
    out.release()

def extract_frames(input_video_path, output_video_path, num_frames=32, fps=3):

    cap = cv2.VideoCapture(input_video_path)
    if not cap.isOpened():
        raise IOError(f"Cannot open video: {input_video_path}")

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

    count = 0
    while count < num_frames:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
        count += 1

    cap.release()
    out.release()


classes = ['broken','smoke','fight','buying','move']
# video_path = '/mnt/d/data/val_data/'
# pad_path = '/mnt/d/data/pad_val_data/'
# output_path = '/mnt/d/data/temp_val_data/'

video_path = '/mnt/d/data/val_new_avi/'
pad_path = '/mnt/d/data/pad_val_new/'
output_path = '/mnt/d/data/temp_val_new/'


for class_name in classes:
    path = video_path + class_name
    file_list = os.listdir(path)

    for file in file_list:
        input_video_path = video_path + class_name + '/' + file
        pad_video_path = pad_path + class_name + '/' + file
        output_video_path = output_path + class_name + '/' + file
        process_video(input_video_path, pad_video_path)
        extract_frames(pad_video_path, output_video_path)

# import os
# import pandas as pd

# def create_video_dataframe(root_dir):
#     data = []

#     # 각 하위 폴더(클래스)를 순회
#     for class_name in os.listdir(root_dir):
#         class_path = os.path.join(root_dir, class_name)

#         # 폴더인지 확인
#         if os.path.isdir(class_path):
#             # 각 비디오 파일에 대해
#             for video_file in os.listdir(class_path):
#                 # 파일 경로를 추가
#                 video_path = os.path.join(class_path, video_file)
#                 data.append({'video': video_path, 'class': class_name})

#     # 데이터프레임 생성
#     df = pd.DataFrame(data)
#     return df

# # 사용 예시
# root_dir = '/mnt/d/data/temp_val_new/'  # 루트 디렉토리 경로
# df = create_video_dataframe(root_dir)
# df.to_csv('temp_val_new.csv', index=False)


# import os

# path = '../logs/TubeViT/version_34/checkpoints'

# for filename in os.listdir(path):
#     file_path = os.path.join(path, filename)

#     if os.path.isfile(file_path):
#         print(filename)

