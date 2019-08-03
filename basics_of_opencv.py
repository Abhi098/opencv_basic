import imutils 
import cv2


########OPENING AND CLOSING IMAGE###############
image=cv2.imread("source.jpeg")
(h,w,d)=image.shape
cv2.imshow("iMAGE",image)
#################################################


#################ACCESING A SINGLE PIXEL########
(B,G,R)=image[100,50]
print("R:",R," G:",G," B:",B)

################################################


####EXTRACTING PEGION OF INTEREST(ROI)#########
roi=image[100:200, 10:80]
cv2.imshow("ROI",roi)
###############################################


###########RESIZING THE IMAGE###################
resized_image=cv2.resize(image,(200,200))
cv2.imshow("RESIZED",resized_image)
################################################


##########IMAGE ROTATION########################
rotate=imutils.rotate(image,-45) ##-45 means 45 degree clockwise
rotate_bound=imutils.rotate_bound(image,45) ##keeps whole image in frame
cv2.imshow("Rotation",rotate)
cv2.imshow("Rotation_bound",rotate_bound)
################################################


###############SMOOTHING AN IMAGE###############
blur=cv2.GaussianBlur(image,(11,11),0) ##11x11 filter  0=SigmaX standard deviation
cv2.imshow("Blur",blur)
################################################


##############RECTANGLE ON IMAGE###############
image1=image.copy()
cv2.rectangle(image1,(10,20),(60,80),(0,255,0),2) ##coordinates color and thickness
cv2.circle(image1,(90,100),20,(0,255,0),-1)  ##center ,radius,color and thickness
cv2.line(image1,(120,100),(190,100),(0,255,0),5) ## points color and thickness
cv2.imshow("rect_circ_line",image1)
###############################################


























cv2.waitKey(0)
