# Build OpenCV on Virtual Environment

Page ini akan menjelaskan tahap build opencv dari source pada virtual environment Anaconda pada sistem operasi linux.

## Install Virtual Environment

Virtual environment merupakan lingkungan pengembangan yang terpisah dengan lingkungan utama komputer. Dengan demikian kita dapat **menginstal versi library yang berbeda** pada setiap virtual environment.

Terdapat berbagai macam virtual environment, salah satunya **Anaconda**. Anaconda merupakan virtual env python yang include dengan library bawaannya, seperti numpy, scipy, matplotlib dll. Ketimbang Anaconda, penulis lebih memilih **Miniconda** (versi lite Anaconda). Tahap instalasinya dapat dilihat pada [page official miniconda](https://docs.conda.io/en/latest/miniconda.html).

### Create Conda Virtual Env

Virtual Env pada Anaconda/Miniconda dapat dibuat dengan perintah berikut:
```
conda create -n [nama-env] python==[versi] numpy
conda create -n vision python==3.7 numpy
```
`[nama-env]` dapat diisi dengan nama virtual env yang akan dibuat, dicontohkan dengan `vision`. Versi python dapat diisikan dengan versi yang dikehendaki, dicontohkan dengan versi `python==3.7`. Kemudian, `numpy` diperlukan sebagai depedensi dari OpenCV sendiri.

## Clone OpenCV

Source code OpenCV dapat diakses pada [github opencv](https://github.com/opencv). Terdapat dua source code yang harus di-clone: `opencv` dan `opencv_contrib`. Kedua source code dapat di-clone melalui git,
```
git clone https://github.com/opencv/opencv
git clone https://github.com/opencv/opencv_contrib
cd opencv
git checkout 4.1.2
cd ../opencv_contrib
git checkout 4.1.2
```
atau dapat clone (download) melalui [page release opencv](https://github.com/opencv/opencv/releases) dan [page tags opencv_contrib](https://github.com/opencv/opencv_contrib/tags). Penulis sarankan menggunakan cara ini, karena proses clone akan spesifik pada versi yang dituju.

Versi yang penulis gunakan dalam penulisan kali ini adalah versi **OpenCV 4.1.2**. Yang penulis clone (donwload) pada tautan [opencv 4.1.2](https://github.com/opencv/opencv/releases/tag/4.1.2) dan [opencv_contrib 4.1.2](https://github.com/opencv/opencv_contrib/releases/tag/4.1.2).

### Make Build Folder

Selanjutnya, buat folder yang `BUILD` (nama untuk memudahkan) yang berisi `opencv` dan `opencv_contrib` dengan nama yang sudah diubah (tidak ada tambahan versi) seperti berikut:

```
├── BUILD-FOLDER
│   ├── opencv
│   └── opencv_contrib
```
## Installing Depedencies

Depedencies merupakan library yang diperlukan untuk dapat build OpenCV dari source. Library ini diperlukan untuk mendukung kerja OpenCV yang customable. OpenCV customable menjadi pembeda dengan OpenCV yang di-install langsung menggunakan `pip` pada Python seperti biasanya. Library yang diperlukan meliputi:

!!! caution

    Diperlukan sekitar 300 mb data untuk download dan 800 mb untuk space.

#### Essential Library
```
sudo apt-get install build-essential \
    cmake git unzip wget pkg-config
```
#### Image and Video Depedencies
```
sudo apt-get install zlib1g-dev libjpeg-dev libjpeg8-dev \
    libjpeg-turbo8-dev libpng-dev libtiff-dev libglew-dev \
    libavcodec-dev libavformat-dev libswscale-dev libgtk2.0-dev \
    libgtk-3-dev libcanberra-gtk* libxvidcore-dev libx264-dev \
    libgtk-3-dev qt5-default libtbb2 libtbb-dev libdc1394-22-dev \
    libxine2-dev gstreamer1.0-tools libgstreamer-plugins-base1.0-dev \
    libgstreamer-plugins-good1.0-dev libv4l-dev v4l-utils qv4l2 \
    libfaac-dev libmp3lame-dev libtheora-dev
```

#### Additional Depedencies
```
sudo apt-get install libtesseract-dev libxine2-dev libpostproc-dev \
    libavresample-dev libvorbis-dev libopencore-amrnb-dev \
    libopencore-amrwb-dev libopenblas-dev libatlas-base-dev \
    libblas-dev liblapack-dev liblapacke-dev libeigen3-dev \
    gfortran libhdf5-dev libprotobuf-dev protobuf-compiler \
    libgoogle-glog-dev libgflags-dev
```

## Build OpenCV

Build OpenCv dilakukan menggunakan `Cmake`. Untuk dapat melakukannya dibuat `cmake script` terlebih dahulu seperti script dibawah.

```bash
#!/bin/sh

CONDA_ENV_PATH=/home/didi/miniconda3/envs #(1)
CONDA_ENV_NAME=vision #(2)
WHERE_OPENCV=../opencv #(3)
WHERE_OPENCV_CONTRIB=../opencv_contrib #(4)

cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D PYTHON3_EXECUTABLE=$CONDA_ENV_PATH/$CONDA_ENV_NAME/bin/python \
    -D OPENCV_EXTRA_MODULES_PATH=$WHERE_OPENCV_CONTRIB/modules \
    -D BUILD_EXAMPLES=ON $WHERE_OPENCV
    -D INSTALL_C_EXAMPLES=OFF \
    -D INSTALL_PYTHON_EXAMPLES=OFF \
    -D WITH_QT=ON \
    -D OPENCV_GENERATE_PKGCONFIG=ON \
    -D OPENCV_ENABLE_NONFREE=ON \
    -D WITH_GSTREAMER=ON \
```

1. Directory Anaconda/Miniconda
2. Nama dari virtual environment
3. Directory `opencv`
4. Directory `opencv_contrib`

Simpan `cmake script` dengan nama `buildopencv.sh` dan simpan pada directory berikut. Selanjutnya, buat directory/folder baru bernama `build`. Dapat dibuat dengan perintah `mkdir build`.
```
├── BUILD-FOLDER
|   ├── build
|   ├── opencv
│   ├── opencv_contrib
│   └── buildopencv.sh
```
### Building Cmake
Selanjutnya proses build `cmake` opencv berlangsung
```
cd build
../buildopencv.sh
```
Jika berhasil akan terdapat pesan sebagai berikut di terminal
```
...
--   Python 3:
--     Interpreter:     /home/didi/miniconda3/envs/rtm3d/bin/python (ver 3.7)
--     Libraries:       /home/didi/miniconda3/envs/rtm3d/lib/libpython3.7m.so (ver 3.7.0)
--     numpy:           /home/didi/miniconda3/envs/rtm3d/lib/python3.7/site-packages/numpy/core/include (ver 1.20.3)
--     install path:    lib/python3.7/site-packages/cv2/python-3.7
...
```
### Start Building OpenCV
Build OpenCV dari `cmake` yang telah dibuat
```bash
make -j4 #(1) 
```

1. ubah -j#, dimana # merupakan core yang tersedia pada CPU

Setelah proses kompilasi berhasil, masukan perintah berikut untuk build opencv
```
sudo make install
```
Bersihkan cache kompilasi dengan perintah
```
sudo ldconfig
```

## Symbolic Link
Library OpenCV yang sudah di-build ternyata tidak dapat langsung digunakan karena berada pada directory yang berbeda dengan directory virtual environment. Oleh karena itu, dilakukan **symbolic link** untuk dapat menghubungkannya.

### Python Symbolic Link

```
# opencv directory
/usr/local/lib/python3.7/site-packages/cv2/python-3.7/cv2.cpython-37-x86_64-linux-gnu.so

# anaconda/virtual env directory in my case
/home/didi/miniconda3/envs/rtm3d/lib/python3.7/site-packages/cv2.so
```
Symlink dengan perintah
```
ln -s \
    /usr/local/lib/python3.7/site-packages/cv2/python-3.7/cv2.cpython-37-x86_64-linux-gnu.so \
    /home/didi/miniconda3/envs/rtm3d/lib/python3.7/site-packages/cv2.so
```
### C++ Symbolic Link
```
/usr/local/include/opencv4/opencv2
sudo ln -s /usr/local/include/opencv4/opencv2/ /usr/local/include/opencv2
```