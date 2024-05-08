import pandas as pd
import os

def make_df(path):
    try:
        df = pd.read_csv(path)
    except:
        df = pd.DataFrame(columns=['video', 'class'])
    
    return df

df = make_df('./validatoin_new.csv')

video_file_names = [f for f in sorted(os.listdir('D:/data/val_new/fight/')) if os.path.isfile(os.path.join('D:/data/val_new/fight/', f))]
length = len(df)

for idx, video in enumerate(video_file_names):
    df.loc[length + idx] = [video, 'fight']

df.to_csv('./validatoin_new.csv', index=False)