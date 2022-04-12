import imageio
import numpy as np
from os import walk
import os

from PIL import Image
import shutil
import cv2

import matplotlib.pyplot as plt

np.set_printoptions(threshold=np.inf)

# float convert to 16UC1
# Original data type is float, we want to convert to uint16
mypath = "./Hospital/P000/depth_left"  
for (dirpath, dirnames, filenames) in walk(mypath):
    for file_name in filenames:
        num = file_name.split("_")[0]
        save_path = "./Hospital/P000/depth/"+str(num)+".png"
        img_array = np.load(os.path.join(mypath, file_name))#,allow_pickle=True)


        img_array = np.ceil(img_array * 5000)
        img_array[img_array >= 65535] = 0
        # if num == "000000":
        #     img_array = np.resize(img_array, (-1))
        #     plt.hist(img_array)
        #     plt.savefig("./AbandonedFactory depth hist.png")
    
        img_array = img_array.astype(np.uint16)
        print(save_path, img_array.dtype )
        cv2.imwrite(save_path ,img_array)





        # if num == "000000":
        #     # print(img_array)
        #     print(num)
        #     print(np.max(img_array))
        #     print(np.min(img_array))
        #     print("=====")
        #     print("")
        #     f = open("./abandoned_0_image_array.txt","w")
        #     f.write(str(img_array))



        # # # cv2.imwrite(save_path, img_array)
        # # im = Image.fromarray(img_array) # or more verbose as Image.fromarray(ar32, 'I')
        # # im.save(save_path)

        # # temp = cv2.imread(save_path)
        # # print(temp.dtype)
        # # print("")



        # # imageio.imwrite(save_path, img_array)
        # # img = imageio.imread(save_path)
        # # print(img.dtype)
        # # print("")


        # img_array_buffer = img_array.tobytes()
        # img = Image.new("I", img_array.T.shape)
        # img.frombytes(img_array_buffer, 'raw', "I;16")
        # img.save(save_path)

        # temp = cv2.imread(save_path, flags = 2)
        # print(temp.dtype)
        # print("")


# # convert rgb image
# mypath = "./AbandonedFactory/depth_org"  # 16UC1
# for (dirpath, dirnames, filenames) in walk(mypath):
#     print(filenames)
#     for file_name in filenames:
#         # img_array = imageio.imread(os.path.join(mypath, file_name)) # .astype(np.uint8)
#         # im_frame = Image.open(os.path.join(mypath, file_name))
#         # img_array = np.array(im_frame.getdata()).astype(np.uint8)

#         num = file_name.split("_")[0]
#         save_path = "./AbandonedFactory/depth/"+str(num)+".png"
#         src_path = os.path.join(mypath, file_name)
#         print(save_path)

#         shutil.copyfile(src_path, save_path)