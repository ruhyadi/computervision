# access jetson camera with opencv
import cv2
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Camera Capture')
parser.add_argument('--output_dir', type=str, default='images', help='output directory')
parser.add_argument('--width', type=int, default=720, help='width of the image')
parser.add_argument('--height', type=int, default=480, help='height of the image')
parser.add_argument('--framerate', type=int, default=30, help='framerate of recording')

args = parser.parse_args()

def gstreamer_pipeline(
    sensor_id=0,
    sensor_mode=3,
    capture_width=args.width,
    capture_height=args.height,
    display_width=args.width,
    display_height=args.height,
    framerate=args.framerate,
    flip_method=2,
):
    return (
        "nvarguscamerasrc sensor-id=%d sensor-mode=%d ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            sensor_id,
            sensor_mode,
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )

# define camera left and right
left_camera = gstreamer_pipeline(sensor_id=0)
right_camera = gstreamer_pipeline(sensor_id=1)

# video capture
left_capture = cv2.VideoCapture(left_camera, cv2.CAP_GSTREAMER)
right_capture = cv2.VideoCapture(right_camera, cv2.CAP_GSTREAMER)

# loop thru camera read

cv2.namedWindow("Calibration Camera")

# to naming image
img_counter = 0

while True:
    _, left_frame = left_capture.read()
    _, right_frame = right_capture.read()
    if not _:
        print("[INFO] Failed to start camera...")
        break
    camera_frame = np.hstack((left_frame, right_frame))
    cv2.imshow("Calibration Camera", camera_frame)
    
    # for closing and capturing images
    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        # left_name = f"calibration/images/left{img_counter:2d}.png"
        # right_name = f"calibration/images/right{img_counter:2d}.png"
        output_dir = args.output_dir
        left_name = f"{output_dir}/left{img_counter:2d}.png"
        right_name = f"{output_dir}/right{img_counter:2d}.png"
        cv2.imwrite(left_name, left_frame)
        cv2.imwrite(right_name, right_frame)
        print(f"Total images: {img_counter:2d}")
        img_counter += 1

left_capture.release()
right_capture.release()

cv2.destroyAllWindows()