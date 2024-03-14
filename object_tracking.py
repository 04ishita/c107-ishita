import cv2
import time
import math

video = cv2.VideoCapture("bb3.mp4")
p1= 530
p2=300
ball_x=[]
ball_y=[]

# Load tracker 
tracker = cv2.TrackerCSRT_create()

# Read the first frame of the video
returned, img = video.read()

# Select the bounding box on the image
bbox = cv2.selectROI("Tracking", img, False) 

# Initialise the tracker on the img and the bounding box
tracker.init(img, bbox)

print(bbox)

def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])

    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)

    cv2.putText(img,"Tracking",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

def goal_track(img, bbox):
    x, y,w, h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    c1=x+int(w/2)
    c2=y+int(h/2)
    cv2.circle(img,(c1,c2),2,(0,0,255),5)
    cv2.circle(img,(p1,p2),2,(0,0,255),5)
    distance= math.sqrt(((c1-p1)**2)+((c2-p2)**2))
    if distance <=20 :  
       cv2.putText(img,"goal",(300,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
    ball_x.append(c1)
    ball_y.append(c2)
    for i in range(len(ball_x)-1):
        cv2.circle(img,(ball_x[i],ball_y[i]),2,(0,0,25),5)


   

   
    

while True:
    
    check, img = video.read()   

    # Update the tracker on the img and the bounding box
    success, bbox = tracker.update(img)
    if success:
        drawBox(img, bbox)
    else:
        cv2.putText(img,"Lost",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

    goal_track(img, bbox)

    cv2.imshow("result", img)
            
    key = cv2.waitKey(25)
    if key == 32:
        print("Stopped")
        break
    

video.release()
cv2.destroyALLwindows()
