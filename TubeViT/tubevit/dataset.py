import torch
from typing import Callable, Optional, Tuple

from torch import Tensor
from torchvision.datasets import UCF101
from torchvision.io import read_video
from torch.utils.data import Dataset
import pandas as pd


## 원래 코드
# class MyUCF101(UCF101):
#     def __init__(self, transform: Optional[Callable] = None, *args, **kwargs) -> None:
#         super().__init__(*args, **kwargs)
#         self.transform = transform
    
#     # 데이터셋의 특정 인덱스에 해당하는 video와 label 반환
#     def __getitem__(self, idx: int) -> Tuple[Tensor, int]:
#         video, audio, info, video_idx = self.video_clips.get_clip(idx)
#         label = self.samples[self.indices[video_idx]][1]

#         if self.transform is not None:
#             video = self.transform(video)

#         return video, label


## MyUCF101 수정 코드
class MyUCF101(UCF101):
    def __init__(self, mode, dataframe: pd.DataFrame, transform: Optional[Callable] = None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.dataframe = pd.read_csv(dataframe)
        self.mode = mode
        self.transform = transform

    def __getitem__(self, idx: int) -> Tuple[Tensor, int]:
        classes = ['smoke','broken','buying','fight','move']
        
        video = self.dataframe.iloc[idx]['video']
        label = self.dataframe.iloc[idx]['class']         
        
        video, _, _ = read_video(video)
        video = video.permute(3, 0, 1, 2)

        if self.transform is not None:
            video = video.float()
            video = self.transform(video)

        label = classes.index(label)

        return video, label
    
    def __len__(self):
        return len(self.dataframe)