import cv2
import numpy as np
import utils
import glob

img_fn = glob.glob('data/images_01/*.jpeg')

crop_dim = (1242, 375)

for i, img_path in enumerate(img_fn):
    img = cv2.imread(img_path)
    # img_resize = utils.resize(0.335, img)
    img_resize = utils.resize(1.21, img)
    img_crop = utils.center_crop(img_resize, crop_dim)

    cv2.imwrite(f'data/images_01_02/{i:06d}.png', img_crop)

#     print(img.shape, img_resize.shape, img_crop.shape)

# cv2.imshow('resize', img_resize)
# cv2.imshow('after_crop', img_crop)
# cv2.imshow('before crop', img)

# cv2.waitKey(0)

# cv2.destroyAllWindows()

