# CT-Scan-Reconstruction-Algo
*** *This project was completed while I was taking junior level CS courses* ***

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
***Please note that if the algorithm is ran multiple times it will override the previous PNG files. For example: if previously there were 6 PNG files and the
algorithm is ran again with a sliced image amount of 3, then the first 3 PNG files will be overrided and the following 3 will be left alone from the past iteration***

***The entire code can be found in the "main.py" file***

***The "Final Report" contains all the findings made by us***

#### This project was created by:
  - ***Brayan Sosa(write the code and report)***
  - ***Hatem Saleh(assisted with code)***
  - ***Fiza Gubitra(assisted with editing report)***
  - ***Fatima Mirza(editing report)***
