#importing opencv
import cv2 as cv
img=cv.imread("./light.jpg")
img_2=cv.imread("./as3hh-4uurn.jpg")
img_3=cv.imread("./dark_2.jpg")
img_4=cv.imread("./img.jpg")

#resizing an image
width = 700
height = 350
img = cv.resize(img, (width, height))
img_2= cv.resize(img_2, (width, height))
img_3= cv.resize(img_3, (width, height))
img_4= cv.resize(img_4, (width, height))

# converrting both images in grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_2 = cv.cvtColor(img_2, cv.COLOR_BGR2GRAY)
gray_3 = cv.cvtColor(img_3, cv.COLOR_BGR2GRAY)
gray_4 = cv.cvtColor(img_4, cv.COLOR_BGR2GRAY)

#setting threshold
threshold =25

# Define the text and the position
text = "The road is safe for the passenger"
text_2 = "The road is unsafe for the passenger"
position = (50, 50)

# Get the average light intensity value of the image
intensity = cv.mean(gray)[0]
intensity_2 = cv.mean(gray_2)[0]
intensity_3 = cv.mean(gray_3)[0]
intensity_4 = cv.mean(gray_4)[0]

#processing
print("Intensity of the image is:-", intensity)
if intensity>threshold:
    print('The image is high intensity in greater than threshold.')
    cv.putText(img, text, position, cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,255, 0), 1)
else:
    print('The image is high intensity in lesser than threshold.')
    cv.putText(img, text_2, position, cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0, 255), 1)


print("Intensity of the image is:-", intensity_2)
if intensity_2>threshold:
    print('The image is high intensity in greater than threshold.')
    cv.putText(img_2, text, position, cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
else:
    print('The image is high intensity in lesser than threshold.')
    cv.putText(img_2, text_2, position, cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

print("Intensity of the image is:-", intensity_3)
if intensity_3>threshold:
    print('The image is high intensity in greater than threshold.')
    cv.putText(img_3, text, position, cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
else:
    print('The image is high intensity in lesser than threshold.')
    cv.putText(img_3, text_2, position, cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

print("Intensity of the image is:-", intensity_4)
if intensity_4>threshold:
    print('The image is high intensity in greater than threshold.')
    cv.putText(img_4, text, position, cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
else:
    print('The image is high intensity in lesser than threshold.')
    cv.putText(img_4, text_2, position, cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

#Displaying iamges
cv.imshow("Image", img)
cv.imshow("Image_2", img_2)
cv.imshow("Image_3", img_3)
cv.imshow("Image_4", img_4)
cv.waitKey(0)
cv.destroyAllWindows()

# # Apply thresholding with a threshold value of 128
# threshold_value = 20
# max_value = 255
# ret, thresholded_image = cv.threshold(img, threshold_value, max_value, cv.THRESH_BINARY)
# # Display the original and thresholded images
# cv.imshow('Background Image', img)
# cv.imshow("Thresholded Image", thresholded_image)
# cv.waitKey(0)
# cv.destroyAllWindows()