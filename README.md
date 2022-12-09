# CT-Scan-Reconstruction-Algo
This project will be able to simulate the reconstruction algorithm of a CT scan.
It creates a virtual phantom(256x256) and is then able to slice the image either horizontally, vertically, or diagonally. After all the slices have been created it will then put them together.

### This program takes as STDIN:
  - cut type: "diagonal", "horizontal", or "vertical" 
  - sliced image amount: integer ranging from 1-255
  
***Please note that this project does not allow for the types of cuts to run simultaneously, i.e horizontal and diagonal cuts can't happen at the same time and so on***

### Process during and after running this code:
1) This program will first display and create a PNG of the ***original phantom*** 
2) Then it will ask for the ***STDIN***, i.e ***cut type*** and ***sliced image amount***
3) It will then create PNG images to display the ***sliced images***
4) Finally it will display the ***image after the cuts have been put back together***

***Sample images can be found for, "10 diagonal cuts," "6 horizontal cuts," and "6 vertical cuts" in the "output" folder***

***Please close all of the pop-up windows once you are done viewing them so that the code can continue/stop running***

#### This project was created by:
  - ***Brayan Sosa***
  - ***Hatem Saleh***
  - ***Fiza Gubitra***
  - ***Fatima Mirza***
