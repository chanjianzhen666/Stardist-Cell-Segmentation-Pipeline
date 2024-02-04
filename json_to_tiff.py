import os
import numpy as np
import cv2
import tifffile
import json
from tqdm import tqdm

dataset_dir = r"json/"
save_dir = r"masks/"
label_path = []

for i in os.listdir(dataset_dir):
    if i.endswith(".geojson"):
        label_path.append(dataset_dir + "/" + i)

for c, i in tqdm(enumerate(label_path), total=len(label_path)):
    com_name = label_path[c].split('//')[-1].split('.')[0]
    with open(i) as f:
        data_ = json.load(f)
    mask_size = data_["features"][0]['geometry']['coordinates'][0][2]
    mask = np.zeros(mask_size, dtype=np.uint16)
    mask[mask>0] = 0
    id = 0
    for data in data_["features"]:
        if data['geometry']['type'] == 'MultiPolygon':
            continue
        data = np.array(data['geometry']['coordinates'])  
        if np.array(data[0]).ndim == 2:
            for j in range(len(data)):
                poly = data[j]
                poly = np.array(poly)
                if j == 0:
                    poly = np.array(poly)
                    mask = cv2.fillPoly(mask, np.int32([poly]), color=id)
                else:
                    poly = np.array(poly)
                    mask = cv2.fillPoly(mask, np.int32([poly]), color=0)

        id += 1
    image_labels = [f'{i}' for i in range(mask.shape[0] * mask.shape[1])]
    tifffile.imwrite(
        save_dir + com_name + ".tiff", 
        mask,
        imagej=True,
        metadata={
            'Labels': image_labels,
        }
)