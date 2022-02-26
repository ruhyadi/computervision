# Augmented Reality 2D

## Introduction

Apa itu **Augmented Reality (AR)**?. Secara sederhana dapat diartikan sebagai pengalaman pengguna (user) pada suatu objek yang ditingkatkan (augmented) oleh komputer. Jadi intinya terdapat pengguna (user) dan terdapat objek yang di-augmented oleh komputer.

## Simple AR with OpenCV

![demo AR](../assets/gif/AR.gif)

Tujuan dari pages kali ini adalah untuk mendemonstrasikan pembuatan AR sederhana menggunakan pustaka OpenCV. Repository source code dapat dilihat pada [ruhyadi/Augmented-Reality](https://github.com/ruhyadi/Augmented-Reality). Langkah pembuatan aplikasi sebagai berikut:

### 1. Feature Detection

Feature detection merupakan metode untuk mendeteksi fitur/landmark/pola penting pada suatu citra/gambar. Fitur yang dimaksud dalam hal ini adalah pola pembeda yang dapat membedakan gambar satu dengan lainnya.

Terdapat berbagai macam fitur detection yang tersedia pada pustaka OpenCV, seperti:

- Scale Invariant Feature Transform (SIFT)
- Speeded-Up Robust Features (SURF)
- Features from Accelerated Segment Test (FAST)
- Binary Robust Independent Elementary Features (BRIEF)
- Oriented FAST and Rotated BRIEF (ORB)

Dalam implementasi kali ini kita akan menggunakan **ORB feature detection** yang tersedia pada fungsi `cv2.ORB_create()` di OpenCV.