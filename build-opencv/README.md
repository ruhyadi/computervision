# Build OpenCV from Source

## 1. Download OpenCV and Contrib Source Code

## 2. Install Depedencies
Install depedensi
```
sudo apt-get install build-essential cmake git unzip pkg-config zlib1g-dev libjpeg-dev libjpeg8-dev libjpeg-turbo8-dev libpng-dev libtiff-dev libglew-dev libavcodec-dev libavformat-dev libswscale-dev libgtk2.0-dev libgtk-3-dev libcanberra-gtk* python3-dev python3-numpy python3-pip
```

```
sudo apt-get install libxvidcore-dev libx264-dev libgtk-3-dev libtbb2 libtbb-dev libdc1394-22-dev libxine2-dev gstreamer1.0-tools libgstreamer-plugins-base1.0-dev libgstreamer-plugins-good1.0-dev libv4l-dev v4l-utils qv4l2 qt5-default
```

``` 
sudo apt-get install libtesseract-dev libxine2-dev libpostproc-dev libavresample-dev libvorbis-dev libfaac-dev libmp3lame-dev libtheora-dev libopencore-amrnb-dev libopencore-amrwb-dev libopenblas-dev libatlas-base-dev libblas-dev
```

```
sudo apt-get install liblapack-dev liblapacke-dev libeigen3-dev gfortran libhdf5-dev libprotobuf-dev protobuf-compiler libgoogle-glog-dev libgflags-dev
```

## 3. Configure Cmake
### Make `build` Directory
```
cd opencv
mkdir build
cd build
```
Setelahnya copy `cmake-conda.sh` dari `./build-opencv/cmake-conda.sh` menuju folder opencv `./build-opencv/opencv/`.

Ubah permission pada file cmake
```
chmod u+x cmake-conda.sh
```

## 4. Build OpenCV
```
make -j4
sudo make install
sudo ldconfig
```

## 5. Symbolic Link
### Python
```
# opencv directory
/usr/local/lib/python3.8/site-packages/cv2/python-3.8/cv2.cpython-38-x86_64-linux-gnu.so

# anaconda/virtual env directory
/home/ruhyadi/miniconda3/envs/vision/lib/python3.8/site-packages/cv2.so
```
Symlink to file
```
ln -s /usr/local/lib/python3.8/site-packages/cv2/python-3.8/cv2.cpython-38-x86_64-linux-gnu.so /home/ruhyadi/miniconda3/envs/vision/lib/python3.8/site-packages/cv2.so
```
### C++
```
/usr/local/include/opencv4/opencv2
sudo ln -s /usr/local/include/opencv4/opencv2/ /usr/local/include/opencv2
```
