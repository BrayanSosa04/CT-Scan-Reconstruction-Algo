import numpy as np
import cv2
import matplotlib.pyplot as plt
from phantominator import shepp_logan

def display(img): #this is a function to display images, it takes in the matrix(image) that I want to display
    plt.imshow(img, cmap='gray')
    plt.show() #creates the little pop-up window
    
#This is the display function used in our project to help us display images. It can be considered a helper function for the "main" file in this folder
