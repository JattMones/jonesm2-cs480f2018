#!/usr/bin/env python3
"""imageScanner.py: Program to scan the pixels of images for their RGB data."""

__author__      = "NAME"
__date__        = "5 Oct 2018"



def getAvgRGB(ima): # works the image algorithm
#Scan the whole image and then get an average red, Green and Blue number for the image
    counter = 0            #Number of pixels that are almost white


    red_int = 0
    green_int = 0
    blue_int = 0

    for i in range(ima.shape[0]):
        for j in range(ima.shape[1]):
            counter += 1
            red_int = red_int + ima[i,j,0]
            green_int = green_int + ima[i,j,1]
            blue_int = blue_int + ima[i,j,2]

    avgRed_flt = red_int / counter
    avgGreen_flt = green_int / counter
    avgBlue_flt = blue_int / counter

    return [avgRed_flt, avgGreen_flt, avgBlue_flt]
#end of getAvgRGB()



def computeSnow(cam): # works the image algorithm
#For every pixel:
    countSnow = 0            #Number of pixels that are almost white
    t = 0.75                 #Threshold for almost white-- can adjust between 0.0 and 1.0

    for i in range(cam.shape[0]): # rows
        for j in range(cam.shape[1]): # columns
            print(i,j,cam[i,j,0],cam[i,j,1],cam[i,j,2])
            #Check if red, green, and blue pixels are > t for each i,j location:
            if (cam[i,j,0] > t) and (cam[i,j,1] > t) and (cam[i,j,2] > t): # the Red Green Blue values (channels of colour)

                countSnow = countSnow + 1
    return countSnow

#end of computeSnow()

def findObjects(cam): # works the image algorithm
#For every pixel:
    horzPix = []
    width = cam.shape[0]
    height = cam.shape[1]
    count = 0
    xcount = 0
    xlength = 0
    ylength = 0
    for i in range(width): # rows
        for j in range(height): # columns
            horzPix.append((cam[i,j,0],cam[i,j,1],cam[i,j,2]))
            count+= 1
    i = 0
    while i < ((len(horzPix))-1):
        if (not(horzPix[i] is (1.0, 1.0, 1.0))):
                if (horzPix[i] == horzPix[i+1]):
                    print("found repitition")
                    xcount += 1
                else:
                    if(xcount >= 3):
                        start = i - xcount
                        xlength = xcount%width
                        if(xcount > width):
                            ylength = math.floor(xcount/width)
                        else:
                            #check specific ylength
                            pass
                    else:
                        xcount = 0
        else:
            pass
        i += 1
    print("Width: "+str(width))
    print("Height: "+str(height))
    results = (start, xlength, ylength)
    return results
#end of computeSnow()


def main(in_file1,in_file2=None): # lead function
    print(" Welcome to the image Scanner.")
    print(" First Input file is :",in_file1)
    ima1 = plt.imread(in_file1)   #Read in image
    count1 = findObjects(ima1)
    print("  *",in_file1, "   object1", count1)

    print("  Program finished. (Yey!)")
#end of main()





# Below is code to launch the program with filenames as parameters.
##############################################################################
#Import the packages for images and arrays:
import matplotlib.pyplot as plt
import math
import numpy as np
import sys

if __name__ == '__main__':

    if len(sys.argv) == 2:
         main(sys.argv[1])

    elif len(sys.argv) == 3:
         main(sys.argv[1],sys.argv[2])
    else:
         print("  A program to count pixels in a png file. ")
         print("     Usage: Program name image1.png image2.png")
         print(" For example: ./imageScanner.py ../graphics/Feb2011.png ../graphics/Feb2014.png ")
         sys.exit(0)
