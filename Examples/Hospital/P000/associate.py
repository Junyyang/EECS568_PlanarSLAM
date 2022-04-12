import imageio
import numpy as np
from os import walk
import os

from PIL import Image
import shutil


with open('associate.txt', 'w') as f:

    for num in range(563):
        if (len(str(num)) == 1):
            message = "00000" + str(num)
        elif (len(str(num)) == 2):
            message = "0000" + str(num)
        elif (len(str(num)) == 3):
            message = "000" + str(num)
        # 000000 rgb/000000.png 000000 depth/000000.png
        # num = file_name.split("_")[0]
        lines = [str(message), "rgb/"+str(message)+".png", str(message), "depth/"+str(message)+".png"]
        print(lines)
        f.write(' '.join(lines))
        f.write('\n')