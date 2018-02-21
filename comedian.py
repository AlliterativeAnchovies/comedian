#import pygame
#import pygame.camera
#from pygame.locals import *
import numpy as np
import cv2 #'pip install opencv-python' is all you need for this dependency

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
	
    if ret == False: break
	
    #crop frame to square
    starty = (len(frame))//2-240
    startx = len(frame[0])//2-240
    frame = frame[starty:starty+480, startx:startx+480]

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #save it
    cv2.imwrite("output.png",frame)
    break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

"""
DEVICE = '/dev/video0'
SIZE = (480, 480)
FILENAME = 'capture.png'

def camStream():
    pygame.init()
    pygame.camera.init()
    display = pygame.display.set_mode(SIZE, 0)
    camera = pygame.camera.Camera(DEVICE, SIZE)
    camera.start()
    screen = pygame.surface.Surface(SIZE, 0, display)
    capture = True
    while capture:
        screen = camera.get_image()
        screen = pygame.transform.scale(screen, (480,480))
        display.blit(screen, (0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                capture = False
            elif event.type == KEYDOWN and event.key == K_s:
                pygame.image.save(screen, FILENAME)
    camera.stop()
    pygame.quit()
    return


camStream()
"""
