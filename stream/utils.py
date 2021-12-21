import cv2
import numpy as np

def video_desc(cap):
    # get video specification
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    length = round(frames/fps, 2)

    print('=== Video Descripton ===')
    print(f'Width: {width}')
    print(f'Height: {height}')
    print(f'FPS: {round(fps, 2)}')
    print(f'Total Frame: {frames}')
    print(f'Video length: {length} second\n')

    return (width, height, fps, frames, length)

def change_fps(fps, total_frame, time):
    frames = fps * time
    frames_seq = np.linspace(0, round(total_frame), round(frames))

    return frames_seq

def resize(percentage, src_width, src_height):
    width = int(src_width * percentage)
    height = int(src_height * percentage)
    dim = (width, height)

    return dim

def center_crop(img, dim):
	"""Returns center cropped image
	Args:
	img: image to be center cropped
	dim: dimensions (width, height) to be cropped
	"""
	width, height = img.shape[1], img.shape[0]

	# process crop width and height for max available dimension
	crop_width = dim[0] if dim[0]<img.shape[1] else img.shape[1]
	crop_height = dim[1] if dim[1]<img.shape[0] else img.shape[0] 
	mid_x, mid_y = int(width/2), int(height/2)
	cw2, ch2 = int(crop_width/2), int(crop_height/2) 
	crop_img = img[mid_y-ch2:mid_y+ch2, mid_x-cw2:mid_x+cw2]
	return crop_img
    

