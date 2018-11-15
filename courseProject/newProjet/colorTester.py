def findObjects(cam): # works the image algorithm
    results = []
    colors = {}
    horzPix = []
    width = cam.shape[0]#Get width of picture
    height = cam.shape[1]#Get height of picture
    xcount = 0#Chain of adjacent pixels of same color (notice, since we move Left to Right, Top to Bottom, wraped adjacent pixels are included)
    xlength = 0#Horizontal length of an object
    ylength = 0#Verticle length of an object
    #For every pixel:
    for i in range(width): # rows
        for j in range(height): # columns
            if not(cam[i,j,0] == 1 and cam[i,j,1] == 1 and cam[i,j,2] == 1):
                horzPix.append((cam[i,j,0],cam[i,j,1],cam[i,j,2]))#Adds the tuple for every pixel color (R,G,B)
    i = 0
    while i < ((len(horzPix))-1):#Need -1 so that it doesn't check the last pixel (i) and a pixel that doesn't exist (i+1), see line 23
        if ((horzPix[i] is tuple((1.0, 1.0, 1.0)))):#If the pixel color isn't white
            results.append("T")
        else:
            results.append("F")
            colors[i]=horzPix[i]
        i += 1
    f = open("output.txt", "w")
    f.write(str(horzPix))
    f.close()
    print(colors[0])
    print(type(colors[0]))
def main(in_file1,in_file2=None): # lead function
    print(" Welcome to the image Scanner.")
    print(" First Input file is :",in_file1)
    ima1 = plt.imread(in_file1)   #Read in image
    findObjects(ima1)

    print("Program finished!")

###
import matplotlib.pyplot as plt
import math
import numpy as np
import sys, os

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
