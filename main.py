import numpy as np
import cv2
import matplotlib.pyplot as plt
from phantominator import shepp_logan

#!!!!!!!!NOTE!!!!!!!!!!!
#I use openCV to create the PNG files that will be shown to the side bar
#I use numpy to facilitate creating and working with matrices it is only used to reshape, create, and append matrices
#I use the matplot library to create the pop up windows for my images
#I use the phantominator library to create my shepp logan phantom
#I only ever take in as input the image size, amount of sliced image and the type of cuts that would like to be seen(vertical, horizontal, or vertical)

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


def display(img): #this is a function to display images, it takes in the matrix(image) that I want to display
    plt.imshow(img, cmap='gray')
    plt.show() #creates the little pop up window


#this is the function that creates all the sliced images
#it takes in the img = matrix(image), cutType = the type of cut that is desired(horizontal, vertical, or diagonal),
# slicedImageAmount = the amount of images, and count = iterator to count how many slices I have made
def imageCut(img, cutType, slicedImageAmount, count):
    if cutType == "horizontal": #lines 36-51 is the code to cut images horizontally
        holder = [] #this is an array that will hold all the values for the slices
        if count == 0: #since we can't divide by zero line 38-41 will take care of the very first slice that we create
            for i in range(0, int(img.shape[0]*(1/slicedImageAmount))):
                for j in range(0, img.shape[1]):
                    holder.append(img[i, j]) #we iterate through the image here and append all values for the sliced range
        else:#the following for loop helps me find the range of the intervals where the cut should be done
            for i in range(int(img.shape[0] * (count / slicedImageAmount)), int(img.shape[0] * ((count + 1) / slicedImageAmount))):
                for j in range(0, img.shape[1]):  #we iterate through the image here and append all values for the sliced range
                    holder.append(img[i, j])
        if len(holder) > int(img.shape[1] * int(img.shape[0]/slicedImageAmount)): #if the amount of pixels is bigger than col*row/number of image slices we reshape as follows
            result = np.reshape(holder, (int(img.shape[0]/slicedImageAmount)+1, img.shape[1])) #reshapes my 1D array into a 2D Array
            return result
        else: #otherwise resize this way
            result = np.reshape(holder, (int(img.shape[0]/slicedImageAmount), img.shape[1]))
            return result

    elif cutType == "vertical":
        holder = [] #the following code is for line 52-67, it works the same as horizontal, just flip everything with row and cols
        if count == 0: #aka change any shape[0] that was in the horizontal section to shape[1] and vice versa
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

    elif cutType == "diagonal": #the following code is for diagonal cuts
        if slicedImageAmount == 1: #the diagonal code works using linear inequalities to create the diagonal slices
            return img
        result = np.zeros((img.shape[0], img.shape[1])) #for diagonal cuts we have to create an image of the same size as the original
        for i in range(0, img.shape[0]):
            for j in range(0, img.shape[1]):
                if count == 0: #we use the equation x + y <= ((row+col)*(1/numberofImageSlices) to determine a linear line that will cut off a section of the image
                    if (i+j) <= ((img.shape[0]+img.shape[1])*(1/slicedImageAmount)):
                        result[i, j] = img[i, j] #this section gets us the top left slice
                else: #we use the equation ((row+col)*(next count)/numberofImageSlices) >= x + y >= ((row+col)*(current count)/numberofImageSlices) to make sure that we get only the pixels in between
                    if ((img.shape[0]+img.shape[1])*((count+1)/slicedImageAmount)) >= (i+j) >= ((img.shape[0]+img.shape[1])*((count)/slicedImageAmount)):
                        result[i, j] = img[i, j] #this section gets us the rest of the diagonal slices
        return result

###########################################creating the shepp logan phantom#############################################
print("Please input the size of your phantom:")
print("Should be a single number, i.e input is 256 then the image size is 256x256")
imgSize = int(input()) #this will be the size of the image, single number should be inputted
if 5 < imgSize:
    phantom = np.array(shepp_logan(imgSize))  # this is the image that we will be slicing it is 256x256 in size
    phantom = np.multiply(phantom, 256)  # do this so that we can work with numpy
    cv2.imwrite("phantom.png", phantom)
    plt.title('Virtual Phantom')
    display(phantom)  # this line and the line before give a title and display the image that we are currently working with
    #######################################################################################################################

    print("please input the type of cut: ")
    type = str(input())  # should be either "horizontal", "vertical", or "diagonal"

    print("Please enter the number of image cuts you would like to see: ")
    print("Example: 1 you will get the same image, if 2 you will get the image halved, if 3 you get three images, and so on...")
    slicedImageAmount = int(input())
    # sliced image should be the number of sliced images that the user would like to see
    # should not be bigger than the shape of the image which is 256 by 256
    # if the input is 1 then you will get the whole image
    # if the input is 2 then you will get two images
    # if the input is 3 then you will get three different images, and so on

    #########################################cutting and displaying the images##############################################
    if 1 <= slicedImageAmount < phantom.shape[0]:  # make sure that the amount of image slices is possible according to the image size
        if type == "vertical":#line 111-126  will execute the code for vertical slices
            count = 0 #the amount of slices that have currently been made, always starts at 0
            title = "VerticalCut#1"
            cutArray = imageCut(phantom, type, slicedImageAmount, count)  # calling the function made to create all the PNG for the image slices
            cv2.imwrite(title + ".png", cutArray)  # imwrite(imagetitle, matrix to create an image for) creates all the PNG images
            result = np.array(cutArray)  # this is the image that will be put together
            count += 1 #increment the count everytime that a slice has been made
            for i in range(1, slicedImageAmount):  # line 112-120 is the same code for line 105-111
                title = "VerticalCut#"
                title += str(i + 1) #this part is done to alter the title for the PNG images
                cutArray = imageCut(phantom, type, slicedImageAmount, count)
                cv2.imwrite(title + ".png", cutArray)
                result = np.append(result, cutArray, axis=1) #this is adding the slices into the resulting image
                count += 1 #increment the count everytime that a slice has been made
            plt.title('Result')
            display(result) #this will display the final image after it has been put together
        elif type == "horizontal": #this are the horizontal slicing and putting back together of the phantom
            count = 0 #the code for horizontal(line 127-142) is works the same code as vertical, except I change the axis I work with
            title = "HorizontalCut#1"
            cutArray = imageCut(phantom, type, slicedImageAmount, count)
            cv2.imwrite(title + ".png", cutArray)
            result = np.array(cutArray)  # this is the image that will be put together
            count += 1
            for i in range(1, slicedImageAmount):
                title = "HorizontalCut#"
                title += str(i + 1)
                cutArray = imageCut(phantom, type, slicedImageAmount, count)
                cv2.imwrite(title + ".png", cutArray)
                result = np.append(result, cutArray, axis=0)
                count += 1
            plt.title('Result')
            display(result)
        elif type == "diagonal": #the following code will be for diagonal cuts
            count = 0 #line 144-148 will work the same way that vertical and horizontal does
            title = "DiagonalCut#1"
            cutArray = imageCut(phantom, type, slicedImageAmount, count)
            cv2.imwrite(title + ".png", cutArray)
            result = np.zeros((phantom.shape[0], phantom.shape[1]))  # this is the image that we will put together
            for i in range(0, cutArray.shape[0]): #iterate through our sliced Image
                for j in range(0, cutArray.shape[1]):
                    if cutArray[i, j] != 0: #if actual tissue intensity values are found then we add it to our result matrix
                        result[i, j] = cutArray[i, j]
            count += 1
            for i in range(1, slicedImageAmount):#line 155-158 will work the same way that vertical and horizontal does
                title = "DiagonalCut#"
                title += str(i + 1)
                cutArray = imageCut(phantom, type, slicedImageAmount, count)
                cv2.imwrite(title + ".png", cutArray)
                for k in range(0, cutArray.shape[0]): #iterate through our sliced Image
                    for j in range(0, cutArray.shape[1]):
                        if cutArray[k, j] != 0: #if actual tissue intensity values are found then we add it to our result matrix
                            result[k, j] = cutArray[k, j]
                count += 1
            plt.title('Result')
            display(result)
        else:
            print("Invalid cut type")
    else:
        print("Error: Invalid cut amount too many/little cuts")
else:
    print("Error: Invalid image size")
