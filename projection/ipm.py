import cv2
import numpy as np

cv2.namedWindow('perpective', cv2.WINDOW_NORMAL)
cv2.namedWindow('BEV', cv2.WINDOW_NORMAL)

img = cv2.imread('/home/didi/Repository/computervision/projection/traffic.jpg')

#pts = np.array([[864, 651], [1016, 581], [1205, 667], [1058, 759]], dtype=np.float32)
pts = np.array([[306, 406], [325, 363], [655, 385], [663, 428]], dtype=np.float32)
for pt in pts:
    cv2.circle(img, tuple(pt.astype(np.int)), 1, (0,0,255), -1)

# compute IPM matrix and apply it
ipm_pts = np.array([[330,340], [330,300], [400,300], [400,340]], dtype=np.float32)
ipm_matrix = cv2.getPerspectiveTransform(pts, ipm_pts)
ipm = cv2.warpPerspective(img, ipm_matrix, img.shape[:2][::-1])

print(ipm_matrix)

# display (or save) images
cv2.imshow('perpective', img)
cv2.imshow('BEV', ipm)
cv2.waitKey()
