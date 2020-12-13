import cv2
cap = cv2.VideoCapture(0)
ret, frame = cap.read()


while True:
    ret, frame = cap.read()
    
    if ret:
      #rest of the following code
      
      if(cv2.waitKey(1)==27):
        break

    else:
      break

cv2.destroyAllWindows()
cap.release()