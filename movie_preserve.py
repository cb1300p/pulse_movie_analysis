import os
import cv2
 
movie_name = 'pulse_1'
movie = './movie/'+movie_name+'.mp4'
 
count = 0
cap = cv2.VideoCapture(movie)
 
while True:
    ret, frame = cap.read()
    if ret == True:
        count += 1
        cv2.imwrite('./image/sample_image/' + movie_name + '_' + str("{0:05d}".format(count)) +'.jpg', frame)
    else:
        break
