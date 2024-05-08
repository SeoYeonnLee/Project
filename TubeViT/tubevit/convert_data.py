import subprocess
import os

directory = '/mnt/d/data/val_new/smoke/'
output_directory = '/mnt/d/data/val_new_avi/smoke/'

file_paths = []
for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)
        file_paths.append(file_path)

# 출력 디렉토리가 존재하지 않는 경우 생성
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

def convert_mp4_to_avi(mp4_file_path, avi_file_path):
    command = ['ffmpeg', '-i', mp4_file_path, '-q:v', '0', avi_file_path]
    subprocess.run(command)

for f in file_paths:
    file_name = os.path.basename(f)
    avi_file = os.path.join(output_directory, os.path.splitext(file_name)[0] + '.avi')
    convert_mp4_to_avi(f, avi_file)