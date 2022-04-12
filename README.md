# CP-SLAM
This work extends [PlanarSLAM](https://arxiv.org/abs/2010.07997) to extract a indoor cylinder surface. 

**Authors:** Yuhan Dong, Yechen Shi, Ying Yang, and Junyuan Yang


In some specific scenarios, the success rate of plane exactor is quite limited, so we fuse a feature slam algorithm based on cylinder plane[CP-SLAM]

ps: the cylinder method is still very naive, we will keep moving.

![planarReconstruction](Examples/demo.png)



## Get Started
1. Download **'hospital_sample_P000.tar.gz'** and convert depth npy file to png file based on [convert_npy.py](Examples/convert_npy.py) written by us.
   To deal with the problem on this data set where the depth map had points from the sky, we exclude the points deviate significantly.
2. Build and Compile

   ```
   git clone https://github.com/Junyyang/EECS568_PlanarSLAM  
   cd EECS568_PlanarSLAM 
   cd release
   
   cmake  -DCMAKE_INSTALL_PREFIX=/usr/local \ -DBUILD_GPU=ON -DBUILD_apps=ON -DBUILD_examples=ON \ -DCMAKE_INSTALL_PREFIX=/usr/local -DPCL_DIR=/usr/local/share/pcl  .. 
   
   make -j12
   sudo make install
   ```

### Test the system locally

1. Download **'freiburg3_structure_texture_far'** and  associate RGB-D pairs based on [associate.py](http://vision.in.tum.de/data/datasets/rgbd-dataset/tools) provided by the dataset.

   ```
   python associate.py PATH_TO_SEQUENCE/rgb.txt PATH_TO_SEQUENCE/depth.txt > associations.txt
   ```

2. Compile the system

```
./build.sh
```

​	3.  Run the system

```
./Examples/RGB-D/Planar_SLAM Vocabulary/ORBvoc.txt Examples/RGB-D/TUM3.yaml PATH_TO_SEQUENCE_FOLDER .PATH_TO_SEQUENCE_FOLDER/ASSOCIATIONS_FILE
```

*similar command for testing ICL-NUIM sequences*

```
./Examples/RGB-D/Planar_SLAM Vocabulary/ORBvoc.txt Examples/RGB-D/ICL.yaml PATH_TO_SEQUENCE_FOLDER  PATH_TO_SEQUENCE_FOLDER/ASSOCIATIONS_FILE

```



----

## Acknowledgement

Thanks to Professor Maani Ghaffari and the ROB 530 course staff for their kind help.
