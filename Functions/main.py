import numpy as np
import cv2
import matplotlib.pyplot as plt
from phantominator import shepp_logan

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
    
#This can be considered the "main" function which puts all the images together and calls the helper functions "imageCut()" and "display()" which can be found in this folder. 
