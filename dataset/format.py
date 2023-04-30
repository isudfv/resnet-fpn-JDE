import os.path as osp
import os
import numpy as np
import cv2


# copy from D:\XYL\5.MOT\FairMOT-master\src\gen_labels_15.py


def mkdirs(d):
    if not osp.exists(d):
        os.makedirs(d)


seq_root = r'C:/Users/isudfv/Desktop/tmp/MOT20/train/'
label_root = r'C:/Users/isudfv/Desktop/Towards-Realtime-MOT/dataset/MOT20/labels_with_ids/train'  # JDE 处理后的标签格式

mkdirs(label_root)
seqs = [s for s in os.listdir(seq_root)]
# print('{} sequences are: \n {} \n'.format(len(seqs), seqs))

tid_curr = 0
tid_last = -1
for i, seq in enumerate(seqs):
    if '02' in seq or "01" in seq:
        continue
    print('({}/{}): {}'.format(i, len(seqs), seq))

    mkdirs(osp.join(label_root, seq, "img1"))

    img_path = osp.join(seq_root, seq, 'img1', '000001.jpg')
    img_sample = cv2.imread(img_path)  # 每个序列第一张图片 用于获取w, h
    seq_width, seq_height = img_sample.shape[1], img_sample.shape[0]  # w, h
    # print('\t    w: {}, h: {}'.format(seq_width, seq_height))

    gt_txt = osp.join(seq_root, seq, 'gt', 'gt.txt')          #  for UAVDT and MOT 数据集自带标签

    gt = np.loadtxt(gt_txt, dtype=np.float64, delimiter=',')
    # gt = gt[:,:6]
    # idx = np.lexsort(gt.T[:2, :])
    # gt = gt[idx, :]

    for fid, tid, x, y, w, h, active, label, _ in gt:  # for visdrone 数据集自带的标签有10位
        if (active == 0) or label not in [1, 2, 4, 5, 6, 7]:
            continue
        # if _ < 0.1:
        #     continue
        fid = int(fid)
        tid = int(tid)
        x += w / 2
        y += h / 2
        label_path = osp.join(label_root, seq, "img1", "{:06d}.txt".format(fid))
        label_str = '0 {:6d} {:.6f} {:.6f} {:.6f} {:.6f}\n'.format(
            tid, x / seq_width, y / seq_height, w / seq_width, h / seq_height)

        # img_path = label_path.replace("labels_with_ids", "images").replace("txt", "jpg")
        # img_data = cv2.imread(img_path)
        #
        # if _ < 0.1:
        #     left = int(x - w / 2)
        #     top = int(y - h / 2)
        #     right = left + int(w)
        #     bottom = top + int(h)
        #     print("{} {} {} {}".format(left, top, right, bottom))
        #     cv2.rectangle(img_data, (left, top), (right, bottom), (0, 255, 0), 2)
        #
        #     cv2.putText(img_data, "conf: {}".format(_), (left, top - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255),
        #                 thickness=2)
        #     cv2.imshow('image',img_data)
        #     cv2.waitKey(0)
        #     pass;
        with open(label_path, 'a+') as f:
            f.write(label_str)
    pass

print('gt.txt --> 00000x.txt successful ！！！')