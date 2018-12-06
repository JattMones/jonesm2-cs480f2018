#!/usr/bin/env python3
"""imageScanner.py: A program that builds a list of objects by looking for adjacent pixels of the same color"""

__author__      = "Matt Jones"
__date__        = "1 Nov 2018"

def checkObjAcrossRows(objList, posXList, posYList, cam):
    global tempObjList
    tempObjList = []
    fullObjectList = []
    j = 0
    for i in range(len(objList)-1):
        x1 = posXList[j]
        x2 = posXList[j+1]
        y1 = posYList[i]
        color = objList[i][0]
        if not(i is len(objList)):
            k = 0
            #print("Reset Range")
            #print(x2-x1)
            for k in range(x2-x1):
                #print(k)
                if((k == ((x2-x1)-1) and not((cam[y1+1,x1+k,0],cam[y1+1,x1+k,1],cam[y1+1,x1+k,2]) == color))):
                    fullObjectList.append(tempObjList)
                    tempObjList = []
                    print("SEPARATING OBJ")
                    break
                elif(((cam[y1+1,x1+k,0],cam[y1+1,x1+k,1],cam[y1+1,x1+k,2]) == color) and len(tempObjList) == 0):
                    tempObjList.append(objList[i])
                    tempObjList.append(objList[i+1])
                    print("Added first obj in group")
                    break
                elif((cam[y1+1,x1+k,0],cam[y1+1,x1+k,1],cam[y1+1,x1+k,2]) == color):
                    tempObjList.append(objList[i+1])
                    print("adding more")
                    break
        j+=2
    if(len(fullObjectList) == 0):
        fullObjectList.append(tempObjList)
    return fullObjectList

def findObjects(cam): # works the image algorithm to get a list of objects
    tempObjPos = []
    results = []
    horzPix = [] #stores non-white pixels left-right, top-bottom
    horzPos = []#stores x cord for each pixel
    vertPos = []#stores y cord for each pixel
    global objXPos
    global objYPos
    objXPos = []#Stores objects starting x cord
    objYPos = []#stores objects starting y cord
    startBool = False
    height = cam.shape[0]#Get width of picture
    width = cam.shape[1]#Get height of picture
    xcount = 0#Chain of adjacent pixels of same color (notice, since we move Left to Right, Top to Bottom, wraped adjacent pixels are included)
    xlength = 0#Horizontal length of an object
    ylength = 0#Verticle length of an object
    #For every non white pixel, make 3 lists that stores x cordinate, y cordinate, and (R,G,B) values
    for i in range(height): # rows
        for j in range(width): # columns
            if not(cam[i,j,0] == 255 and cam[i,j,1] == 255 and cam[i,j,2] == 255):
                horzPix.append((cam[i,j,0],cam[i,j,1],cam[i,j,2]))#Adds the tuple for every pixel color (R,G,B)
                horzPos.append(j)#x
                vertPos.append(i)#y
                #tempObjPos.append((j,i))
    i = 0
    while i < ((len(horzPix))-1):#Need -1 so that it doesn't check the last pixel (i) and a pixel that doesn't exist (i+1), see line 23
        if (horzPix[i] == horzPix[i+1]):#If two adjacent pixels are the same color
            if not(startBool):#If the object start is still false, sets the object start to pixel
                start = horzPos[i]
                startBool = True#sets object start to true
            if((vertPos[i] - vertPos[i-1]) > 1):#Checks to make sure that they are actually adjacent, and not sperated by whitespace that was removed
                #print("Repitition stopped")
                if(xcount >= 3):
                    end = horzPos[i-1]
                    endY = vertPos[i-1]
                    startBool = False
                    objXPos.append(start)
                    objXPos.append(end)
                    objYPos.append(endY)
                    #print("BREAK        BREAK       BREAK")
                    start = i - xcount#Find where the object started
                    xlength = xcount%width#Find the object length
                    if(xcount > width):
                        ylength = math.floor(xcount/width)
                    results.append((horzPix[i-1], xlength, ylength))
                xcount = 0
            #print("Repitition found")
            xcount += 1#Add to chain of adjacent pixels and start over
        else:
            #print("Repitition stopped")
            if(xcount >= 3):
                end = horzPos[i-1]
                endY = vertPos[i-1]
                startBool = False
                objXPos.append(start)
                objXPos.append(end)
                objYPos.append(endY)
                #print("BREAK        BREAK       BREAK")
                start = i - xcount#Find where the object started
                xlength = xcount%width#Find the object length
                if(xcount > width):
                    ylength = math.floor(xcount/width)
                results.append((horzPix[i-1], (end - start), ylength))
            xcount = 0
        i += 1
    #print("vertPos" , vertPos)
    print("Width: "+str(width))
    print("Height: "+str(height))
    #print("objPos: ", tempObjPos)
    print(results)
    return results
#end of findObjects()


def main(in_file1,in_file2=None): # lead function
    print(" Welcome to the image Scanner.")
    print(" First Input file is :",in_file1)
    ima1 = plt.imread(in_file1)   #Read in image
    horzObj = findObjects(ima1)
    listOfObjects = checkObjAcrossRows(horzObj, objXPos, objYPos, ima1)
    print("Number of objects: "+ str(len(listOfObjects)))
    print("List of Objects in",in_file1,": ", listOfObjects)
    print(len(tempObjList))
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
