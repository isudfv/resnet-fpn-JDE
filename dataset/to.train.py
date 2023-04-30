import os.path as osp
import os
import numpy as np
import cv2


seq_root = r'C:/Users/isudfv/Desktop/Towards-Realtime-MOT/dataset/MOT20/images/train'
root = r'C:\Users\isudfv\Desktop\Towards-Realtime-MOT\dataset'

from pathlib import Path

pathlist = Path(seq_root).rglob('*.jpg')

with open("../data/mot20.train", 'a+') as f:
    for path in pathlist:
        files = str(path.relative_to(root)) + '\n'
        label_path = files.replace("images", "labels_with_ids").replace("jpg", "txt")
        label_path =os.path.join(root, label_path).strip()
        if not os.path.isfile(label_path):
            continue
        f.writelines(files)
