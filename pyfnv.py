import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
#from directkeys import PressKey,ReleaseKey, w, f, e, r


#print('Give card')
#PressKey(w)
#ReleaseKey(w)
#print('Split')
#PressKey(w)
#wwwReleaseKey(w)


def draw_lines(img, lines):
    try:
        for line in lines:
            coords = line[0]
            cv2.line(img, (coords[0], coords[1]), (coords[2], coords[3]), [255, 255, 255], 3)
    except:
        pass


#roi = region of interest
def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    processed_img = cv2.GaussianBlur(processed_img, (5,5), 0)
    vertices = np.array([[200, 600], [375, 600], [375, 100], [200, 100]])
    processed_img = roi(processed_img, [vertices])

    #lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180,np.array([]), 4, 20)
    #draw_lines(processed_img, lines)

    return processed_img

last_time = time.time()
while(True):
    screen =  np.array(ImageGrab.grab(bbox = (0, 40, 800, 640)))
    new_screen = process_img(screen)
    #printscreen_numpy =   np.array(printscreen_pil.getdata(),dtype='uint8')\
    #.reshape((printscreen_pil.size[1],printscreen_pil.size[0],3))

    print('Loop took {} seconds'.format(time.time()- last_time))
    last_time = time.time()
    cv2.imshow('window', new_screen)
    #cv2.imshow('window2',np.array(screen))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
