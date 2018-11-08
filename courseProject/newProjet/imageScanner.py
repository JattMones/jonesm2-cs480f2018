#!/usr/bin/env python3
"""imageScanner.py: A program that builds a list of objects by looking for adjacent pixels of the same color"""

__author__      = "Matt Jones"
__date__        = "1 Nov 2018"

def findObjects(cam): # works the image algorithm
    results = []
    horzPix = []
    width = cam.shape[0]#Get width of picture
    height = cam.shape[1]#Get height of picture
    xcount = 0#Chain of adjacent pixels of same color (notice, since we move Left to Right, Top to Bottom, wraped adjacent pixels are included)
    xlength = 0#Horizontal length of an object
    ylength = 0#Verticle length of an object
    #For every pixel:
    for i in range(width): # rows
        for j in range(height): # columns
            horzPix.append((cam[i,j,0],cam[i,j,1],cam[i,j,2]))#Adds the tuple for every pixel color (R,G,B)
    i = 0
    while i < ((len(horzPix))-1):#Need -1 so that it doesn't check the last pixel (i) and a pixel that doesn't exist (i+1), see line 23
        if (not(horzPix[i] is (1.0, 1.0, 1.0))):#If the pixel color isn't white
                if (horzPix[i] == horzPix[i+1]):#If two adjacent pixels are the same color
                    xcount += 1#Add to chain of adjacent pixels
                else:
                    if(xcount >= 3):
                        start = i - xcount#Find where the object started
                        xlength = xcount%width#Find the object length
                        if(xcount > width):
                            ylength = math.floor(xcount/width)
                        else:
                            #method that checks the next row at specified x values
                            pass
                    else:
                        xcount = 0
        else:
            pass
        i += 1
    print("Width: "+str(width))
    print("Height: "+str(height))
    results.append((start, xlength, ylength))
    return results
#end of findObjects()


def main(in_file1,in_file2=None): # lead function
    print(" Welcome to the image Scanner.")
    print(" First Input file is :",in_file1)
    ima1 = plt.imread(in_file1)   #Read in image
    listOfObjects = findObjects(ima1)
    print("Number of objects: "+ str(len(listOfObjects)))
    print("List of Objects in",in_file1,": ", listOfObjects)

    print("Program finished!")
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
