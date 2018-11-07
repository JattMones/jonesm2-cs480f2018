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

def computeGrass(cam): # works the image algorithm
#For every pixel:
    for i in range(cam.shape[0]): # rows
        for j in range(cam.shape[1]): # columns
            r = cam[i,j,0]
            g = cam[i,j,1]
            b = cam[i,j,2]
            if g > (r+b):
                countGrass = 1

    return countGrass

#end of computeSnow()


def main(in_file1,in_file2=None): # lead function
    print(" Welcome to the image Scanner.")
    print(" First Input file is :",in_file1)
    print(" Second Input file is :",in_file2)
    ima1 = plt.imread(in_file1)   #Read in image
    count1 = 0
    count2 = 0

    count1 = computeSnow(ima1)
    count3 = computeGrass(ima1)
    if in_file2 != None:
            ima2 = plt.imread(in_file2)   #Read in image
            count2 = computeSnow(ima2)
            count4 = computeGrass(ima2)
# unblock this section of code when ready to run the getAvgRGB() function
    colCount1_list = getAvgRGB(ima1)
    if count3 > 0:
        sum = colCount1_list[0]+ colCount1_list[1]+ colCount1_list[2]
        percent = (colCount1_list[1] / sum)*100
    if in_file2 != None:
            ima2 = plt.imread(in_file2)   #Read in image
            colCount2_list = getAvgRGB(ima2)
            if count4 > 0:
                sum = colCount2_list[0]+ colCount2_list[1]+ colCount2_list[2]
                percent2 = (colCount2_list[1] / sum)*100
    print("  *",in_file1, "   Snow count is", count1)
    if count3 > 0:
        print("The picture is "+ str(percent) + "%  grass (this is a relative measurment)")
    print("  *",in_file1, "   The average RGB colours are the following : ", colCount1_list)

    if in_file2 != None:
        print("  *",in_file2, "   Snow count is", count2)
        if count4 > 0:
            print("The picture is "+ str(percent) + "%  grass (this is a relative measurment)")
        print("  *",in_file2, "   The average RGB colours are the following : ", colCount2_list)
    print("  Program finished. (Yey!)")
#end of main()





# Below is code to launch the program with filenames as parameters.
##############################################################################
#Import the packages for images and arrays:
import matplotlib.pyplot as plt
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
