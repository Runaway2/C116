import cv2

img = cv2.imread("/Users/kovidjaddu/Downloads/kovid-c116-main/poster.jpg")

rocket = img[120:360,400:500]

img[0:240, 500:600] = rocket

text_to_show = "I love coding at WhiteHatJr."


cv2.putText(img,  
           text_to_show,
           (20, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,255,0)
           )

cv2.imshow("output",img)

###### ADDITIONAL ACTIVITY ####

# cv2.imwrite("Greetings.jpg",img)

###############################

cv2.waitKey(0)
