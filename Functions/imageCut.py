import numpy as np
import cv2
import matplotlib.pyplot as plt
from phantominator import shepp_logan

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