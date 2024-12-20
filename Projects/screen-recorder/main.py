import pyautogui
import numpy
import cv2
import time

resolution = (1920,1080)
codec = cv2.VideoWriter().fourcc(*"XVID")
filename = "recording.avi"
fps = 30
out = cv2.VideoWriter(filename, codec, fps, resolution)


# crating window
cv2.namedWindow("Live" , cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)

# Time tracking for FPS
frame_time = 1 / fps  # Time per frame in seconds

while True:
     # record the start time
     start_time = time.time()
     # getting screenshot
     img = pyautogui.screenshot()
     # storing it to array
     frame = numpy.array(img)
     # converting bgr to rgb
     frame =  cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
     # assigning it to out file
     out.write(frame)
     # displaying window
     cv2.imshow("Live", frame)
     # s\top recording when we press "q"
     if cv2.waitKey(1) == ord("q"):
         break

# Calculate elapsed time and add delay to match target FPS
elapsed_time = time.time() - start_time
if elapsed_time < frame_time:
     time.sleep(frame_time - elapsed_time)

out.release()
cv2.destroyAllWindows()
