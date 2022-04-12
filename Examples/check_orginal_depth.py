import imageio
import numpy as np
from os import walk
import os

import matplotlib.pyplot as plt

from PIL import Image
import shutil

import cv2

# check depth image
# mypath = "/home/dyh/rgbd_dataset_freiburg3_structure_texture_far/depth"  # 16UC1
# file_name = "1341839145.329622.png"


mypath = "./Hospital/P000/depth/"  # 16UC1
file_name = "000001.png"


file_path = os.path.join(mypath, file_name)
im = cv2.imread(file_path, flags = 2)

print(im.dtype)
image_array = np.array(im)
print(type(image_array))
print(image_array.shape)

# image_array = np.resize(image_array, (1,-1))
# print(image_array.shape)

print(np.max(image_array))
print(np.min(image_array))

image_array = np.resize(image_array, (-1))

image_array = np.sort(image_array, axis=0)

plt.hist(image_array)
plt.savefig("./Hospital depth hist.png")