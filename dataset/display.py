import os.path as osp
import os
import numpy as np
import cv2


# copy from D:\XYL\5.MOT\FairMOT-master\src\gen_labels_15.py


def mkdirs(d):
    if not osp.exists(d):
        os.makedirs(d)


seq_root = r'C:/Users/isudfv/Desktop/Towards-Realtime-MOT/dataset/MOT20/images/train'
label_root = r'C:\Users\isudfv\Desktop\Towards-Realtime-MOT\dataset\MOT20\labels_with_ids\train'  # JDE 处理后的标签格式

seqs = [s for s in os.listdir(seq_root)]

for i, seq in enumerate(seqs):
    label_path = osp.join(label_root, seq, "img1")
    for files in os.listdir(label_path):
        img_path = osp.join(label_path, files).replace("labels_with_ids", "images").replace("txt", "jpg")
        img_data = cv2.imread(img_path)
        H, W, _ = img_data.shape

        label_f = open(osp.join(label_path, files), "r")
        lines = label_f.readlines()
        for line in lines:
            line_list = line.strip().split()
            _, id = line_list[:2]
            x, y, w, h = line_list[2:]
            x = int(float(x) * W)
            y = int(float(y) * H)
            w = int(float(w) * W)
            h = int(float(h) * H)
            id = int(id)

            left = int(x - w / 2)
            top = int(y - h / 2)
            right = left + w
            bottom = top + h
            print("{} {} {} {}".format(left, top, right, bottom))
            cv2.rectangle(img_data, (left, top), (right, bottom), (0, 255, 0), 2)

            cv2.putText(img_data, "id: {}".format(id), (left, top - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255),
                        thickness=2)
            pass
        pass
    pass
