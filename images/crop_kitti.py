import cv2
import numpy as np
import utils
import glob

img_fn = glob.glob('data/image_2/*.png')

enlarge = 1.625

crop_dim = (1242, 375)

for i, img_path in enumerate(img_fn):
    img = cv2.imread(img_path)
    img_resize = utils.resize(enlarge, img)
    img_crop = utils.center_crop(img_resize, crop_dim)

    cv2.imwrite(f'data/image_2_1/{i:06d}.png', img_crop)

print(f"Kitti Size: (375, 1242)")
print(f"Original: {img.shape}")
print(f"Resize: {img_resize.shape}")
print(f"Crop: {img_crop.shape}")

cv2.imshow('resize', img_resize)
cv2.imshow('after_crop', img_crop)
cv2.imshow('before crop', img)

cv2.waitKey(0)

cv2.destroyAllWindows()

