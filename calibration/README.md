# Camera Calibration

## Single Camera Calibration
Untuk calibrasi kamera tunggal gunakan script `single_camera_calibration.py` sebagai berikut:

```
python single_camera_calibration.py \
    --image_dir data/images_04 \
    --image_format png \
    --prefix '' \
    --square_size 0.025 \
    --width 9 \
    --height 6 \
    --save_file calib-matrix/left_cam_04.yml
```

## Stereo Camera Calibration

```
python stereo_camera_calibration.py \
  --left_file calib-matrix/left_cam_04.yml \
  --right_file calib-matrix/right_cam_04.yml \
  --left_prefix '' \
  --right_prefix '' \
  --left_dir data/images_04 \
  --right_dir data/images_04 \
  --image_format png \
  --square_size 0.025 \
  --width 9 \
  --height 6 \
  --save_file calib-matrix/stereo_cam_04.yml
```