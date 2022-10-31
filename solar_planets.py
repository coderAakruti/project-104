import cv2
img= cv2.imread("solar-system.jpg")
print (img)
cv2.putText(img,  
           "sun",
           (20, 220),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           (255,255,255)
           )
cv2.putText(img,  
           "mercury",
           (20, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "venus",
           (20, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "earth",
           (20, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "mars",
           (40, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "jupiter",
           (60, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "saturn",
           (80, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "uranus",
           (100, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "neptune",
           (120, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )

cv2.imshow("output",img)
cv2.waitKey(0)