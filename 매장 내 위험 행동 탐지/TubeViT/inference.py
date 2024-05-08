import os
import pickle

import sys
sys.path.append('./OC_SORT/')
sys.path.append('./TubeViT/')

import pytorch_lightning as pl
import torch
from pytorchvideo.transforms import Normalize
from torch.utils.data import DataLoader, RandomSampler
from torchvision.transforms import transforms as T
from torchvision.transforms._transforms_video import ToTensorVideo

from TubeViT.tubevit.dataset import MyUCF101
from TubeViT.tubevit.model import TubeViTLightningModule

def main(
    dataset_root='/mnt/data/test/',
    model_path='./TubeViT/logs/TubeViT/version_36/checkpoints/epoch=29-step=1230.ckpt',
    annotation_path='/mnt/data/test/',
    label_path='/mnt/data/test/testlist01.txt',
    num_classes=5,
    batch_size=1,
    frames_per_clip=32,
    video_size=(224, 224),
    num_workers=0,
    seed=42,
    verbose=False,
):
    pl.seed_everything(seed)

    with open(label_path, "r") as f:
        labels = f.read().splitlines()
        labels = list(map(lambda x: x.split(" ")[-1], labels))

    test_transform = T.Compose(
        [
            ToTensorVideo(),
            T.Resize(size=video_size),
            Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )

    val_metadata_file = "ucf101-val-meta.pickle"
    val_precomputed_metadata = None
    if os.path.exists(val_metadata_file):
        with open(val_metadata_file, "rb") as f:
            val_precomputed_metadata = pickle.load(f)

    val_set = MyUCF101(
        mode='validation',
        dataframe='./TubeViT/temp_val_new.csv',
        root=dataset_root,
        annotation_path=annotation_path,
        _precomputed_metadata=val_precomputed_metadata,
        frames_per_clip=frames_per_clip,
        train=False,
        output_format="THWC",
        transform=test_transform,
    )

    if not os.path.exists(val_metadata_file):
        with open(val_metadata_file, "wb") as f:
            pickle.dump(val_set.metadata, f, protocol=pickle.HIGHEST_PROTOCOL)

    # val_sampler = RandomSampler(val_set, num_samples=len(val_set) // 5000)
    val_sampler = RandomSampler(val_set, num_samples=1)
    val_dataloader = DataLoader(
        val_set,
        batch_size=batch_size,
        num_workers=num_workers,
        shuffle=False,
        drop_last=True,
        sampler=val_sampler,
    )

    x, y = next(iter(val_dataloader))
    print(x.shape)

    model = TubeViTLightningModule.load_from_checkpoint(model_path)

    trainer = pl.Trainer(accelerator="auto", default_root_dir="lightning_predict_logs")
    predictions = trainer.predict(model, dataloaders=val_dataloader)

    y_prob = torch.cat([item["y_prob"] for item in predictions])

    classes = ['smoke', 'broken', 'buying', 'fight', 'move']

    print('Predicted Class : {}'.format(classes[torch.argmax(y_prob)]))


if __name__ == "__main__":
    main()