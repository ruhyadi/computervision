import numpy as np

fps = 15
time = 25
total_frame = 730

frames = fps * time
frames_seq = np.linspace(0, total_frame, frames)

b = frames_seq[1] - frames_seq[0]

print(b)