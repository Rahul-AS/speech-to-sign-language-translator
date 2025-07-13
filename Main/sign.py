# importing libraries
import cv2
import numpy as np
import os

#Find the Sign Language video from the local system
def findExtension(text):
  #Path for the videos in the local system
  path = 'Sign Language'
  dir_list = os.listdir(path)#Lists all the files and folders in the specified path

  #Linear search for the words in the local system
  for word in dir_list:
    if word.split('.')[0] == text:
      return word

#Function to find the Sign Language Video corresponding to the word
def playVideo(text):
  
  #Find the location of the Video 
  file = findExtension(text)
  
  if file!=None:
    # Create a VideoCapture object and read from input file
    cap = cv2.VideoCapture('Sign Language/' + file)
       
    # Check if camera opened successfully
    if (cap.isOpened() == False): 
      print("Error opening video  file")
       
    # Read until video is completed
    while(cap.isOpened()):
          
      # Capture frame-by-frame
      ret, frame = cap.read()
      if ret:
       
        # Display the resulting frame
        imS = cv2.resize(frame, (960, 540))

        cv2.putText(imS,text,(30,140),cv2.FONT_HERSHEY_SIMPLEX,5,(0,0,255),2)
        cv2.imshow('Frame', imS)
       
        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
          break
       
      # Break the loop
      else: 
        break
       
    # When everything done, release 
    # the video capture object
    cap.release()
       
    # Closes all the frames
    cv2.destroyAllWindows()
  else:
    
    return 1

