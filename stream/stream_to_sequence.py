import cv2
import numpy as np
from utils import video_desc, change_fps, resize, center_crop

# capture video
cap = cv2.VideoCapture('data/video_01.mp4')

# print video description
width, height, fps, frames, length = video_desc(cap)
dim = resize(1, width, height)

# check if video is opened
if (cap.isOpened() == False):
    print("Cannot open video!")

# image sequence numbering
frame_seq = change_fps(5, frames, length)
print('Total New Frame:', len(frame_seq))
frame_n = 0
i = 0

while (cap.isOpened()):
    # get frame-by-frame
    hasVideo, frame = cap.read()
    if hasVideo == True and frame_n == round(frame_seq[i]):
        # resize
        #frame = cv2.resize(frame, (1382, 512), interpolation=cv2.INTER_AREA)

        # crop image
        frame = center_crop(frame, (1382, 512))

        # display video
        cv2.imshow('Frame', frame)
        # write frame to image
        cv2.imwrite(f'sequence_04/{i:06d}.png', frame)
        # presss q to break
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        i = i + 1
    frame_n = frame_n + 1
    if frame_n == frames:
        break

# release video
cap.release()
# destroy all windows
cv2.destroyAllWindows()