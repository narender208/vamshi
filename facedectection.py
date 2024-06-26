import cv2
faceCascade = cv2.CascadeClassifier("har_cascade.xml")
image = cv2.imread('OIP (1).jpg')
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=6,
    minSize=(30,30),

    flags=cv2.CASCADE_SCALE_IMAGE
)
print("Found {0} faces!".format(len(faces)))
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow("Faces found",image)
cv2.waitKey(0)