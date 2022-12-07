import numpy as np
import cv2
import matplotlib.pyplot as plt
from phantominator import shepp_logan

#GOAL OF PROJECT:
#create a virtual phantom(shepp logan)
#slice the phantom horizontally, vertically, and diagonally
#show the sliced image
#put the image back together and show the result

#Done List:
#create a virtual phantom
#slicing and putting it back together vertically
#slicing and putting it back together horizontally
#slicing and putting it back together diagonally


def display(img): #this is a function to display images
    plt.imshow(img, cmap='gray')
    plt.show()

def imageCut(img, cutType, slicedImageAmount, count):
    if cutType == "horizontal":
        holder = []
        if count == 0:
            for i in range(0, int(img.shape[0]*(1/slicedImageAmount))):
                for j in range(0, img.shape[1]):
                    holder.append(img[i, j])
        else:
            for i in range(int(img.shape[0] * (count / slicedImageAmount)), int(img.shape[0] * ((count + 1) / slicedImageAmount))):
                for j in range(0, img.shape[1]):
                    holder.append(img[i, j])
        if len(holder) > int(img.shape[1] * int(img.shape[0]/slicedImageAmount)):
            result = np.reshape(holder, (int(img.shape[0]/slicedImageAmount)+1, img.shape[1]))
            return result
        else:
            result = np.reshape(holder, (int(img.shape[0]/slicedImageAmount), img.shape[1]))
            return result

    elif cutType == "vertical":
        holder = []
        if count == 0:
            for i in range(0, img.shape[0]):
                for j in range(0, int(img.shape[1] * (1 / slicedImageAmount))):
                    holder.append(img[i, j])
        else:
            for i in range(0, img.shape[0]):
                for j in range(int(img.shape[1] * (count / slicedImageAmount)), int(img.shape[1] * ((count + 1) / slicedImageAmount))):
                    holder.append(img[i, j])
        if len(holder) > int(img.shape[0] * int(img.shape[1]/slicedImageAmount)):
            result = np.reshape(holder, (img.shape[0], int((img.shape[1] / slicedImageAmount) + 1)))
            return result
        else:
            result = np.reshape(holder, (img.shape[0], int(img.shape[1] / slicedImageAmount)))
            return result

    elif cutType == "diagonal":
        if slicedImageAmount == 1:
            return img
        result = np.zeros((img.shape[0], img.shape[1]))
        for i in range(0, img.shape[0]):
            for j in range(0, img.shape[1]):
                if count == 0:
                    if (i+j) <= (img.shape[0]*2*(1/slicedImageAmount)):
                        result[i, j] = img[i, j]
                else:
                    if (img.shape[0]*2*((count+1)/slicedImageAmount)) >= (i+j) >= (img.shape[0]*2*((count)/slicedImageAmount)):
                        result[i, j] = img[i, j]
        return result

###########################################creating the shepp logan phantom#############################################
phantom = np.array(shepp_logan(256)) #this is the image that we will be slicing it is 256x256 in size
phantom = np.multiply(phantom, 256) #do this so that we can work with numpy
cv2.imwrite("phantom.png", phantom)
plt.title('Virtual Phantom')
display(phantom) #this line and the line before give a title and display the image that we are currently working with
#######################################################################################################################

print("please input the type of cut: ")
type = str(input()) #should be either "horizontal", "vertical", or "diagonal"

print("Please enter the number of image cuts you would like to see: ")
print("Example: 1 you will get the same image, if 2 you will get the image halved, if 3 you get three images, and so on...")
slicedImageAmount = int(input()) #should not be bigger than the shape of the image which is 256 by 256
#if the input is 1 then you will get the whole image
#if the input is 2 then you will get two images
#if the input is 3 then you will get three different images
#so on

#########################################cutting and displaying the images##############################################
if 1 <= slicedImageAmount < phantom.shape[0]:
    if type == "vertical":
        count = 0
        title = "VerticalCut#1"
        cutArray = imageCut(phantom, type, slicedImageAmount, count)
        cv2.imwrite(title + ".png", cutArray)
        result = np.array(cutArray)  # this is the image that will be put together
        count += 1
        for i in range(1, slicedImageAmount):
            title = "VerticalCut#"
            title += str(i+1)
            cutArray = imageCut(phantom, type, slicedImageAmount, count)
            cv2.imwrite(title+".png", cutArray)
            result = np.append(result, cutArray, axis = 1)
            count += 1
        plt.title('Result')
        display(result)
    elif type == "horizontal":
        count = 0
        title = "HorizontalCut#1"
        cutArray = imageCut(phantom, type, slicedImageAmount, count)
        cv2.imwrite(title + ".png", cutArray)
        result = np.array(cutArray)  # this is the image that will be put together
        count += 1
        for i in range(1, slicedImageAmount):
            title = "HorizontalCut#"
            title += str(i+1)
            cutArray = imageCut(phantom, type, slicedImageAmount, count)
            cv2.imwrite(title+".png", cutArray)
            result = np.append(result, cutArray, axis = 0)
            count += 1
        plt.title('Result')
        display(result)
    elif type == "diagonal":
        count = 0
        title = "DiagonalCut#1"
        cutArray = imageCut(phantom, type, slicedImageAmount, count)
        cv2.imwrite(title + ".png", cutArray)
        result = np.zeros((phantom.shape[0], phantom.shape[1])) #this is the image that we will put together
        for i in range(0, cutArray.shape[0]):
            for j in range(0, cutArray.shape[1]):
                if cutArray[i, j] != 0:
                    result[i, j] = cutArray[i, j]
        count += 1
        for i in range(1, slicedImageAmount):
            title = "DiagonalCut#"
            title += str(i + 1)
            cutArray = imageCut(phantom, type, slicedImageAmount, count)
            cv2.imwrite(title + ".png", cutArray)
            for k in range(0, cutArray.shape[0]):
                for j in range(0, cutArray.shape[1]):
                    if cutArray[k, j] != 0:
                        result[k, j] = cutArray[k, j]
            count += 1
        plt.title('Result')
        display(result)
    else:
        print("Invalid cut type")
else:
    print("Error: Invalid cut amount too many/little cuts")