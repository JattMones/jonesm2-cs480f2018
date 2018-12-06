import matplotlib.pyplot as plt
import math
import numpy as np
import sys

def checkVisibilityX(i):
    if ((horzVertPos[i] == horzVertPos[i+1] and horzVertPos[i] == horzVertPos[i+2]) and (horzPos[i+2]-horzPos[i+1] == 1 and horzPos[i+1]-horzPos[i] == 1)):
        if (nonWhiteHorzPix[i] == nonWhiteHorzPix[i+1] and nonWhiteHorzPix[i] == nonWhiteHorzPix[i+2] and nonWhiteHorzPix[i] == nonWhiteHorzPix[i+3]):
            return True
    else:
        return False
def checkVisibilityY(i):
    if (vertHorzPos[i] == vertHorzPos[i+1] and vertHorzPos[i] == vertHorzPos[i+2]) and (vertPos[i+2]-vertPos[i+1] == 1 and vertPos[i+1]-vertPos[i] == 1):
        if (nonWhiteVertPix[i] == nonWhiteVertPix[i+1] and nonWhiteVertPix[i] == nonWhiteVertPix[i+2] and nonWhiteVertPix[i] == nonWhiteVertPix[i+3]):
            return True
    else:
        return False

def main(in_file1,in_file2=None): # lead function
    print(" Welcome to the image Scanner.")
    print(" First Input file is :",in_file1)

    ima1 = plt.imread(in_file1)   #Read in image
    height = ima1.shape[0]#Get width of picture
    width = ima1.shape[1]#Get height of picture
    print("height:",height)
    print("width",width)
    global nonWhiteHorzPix
    nonWhiteHorzPix=[]
    global nonWhiteVertPix
    nonWhiteVertPix=[]
    global horzPos
    horzPos=[]
    global horzVertPos
    horzVertPos=[]
    global vertHorzPos
    vertHorzPos=[]
    global vertPos
    vertPos=[]
    horzLength = 0
    vertLength = 0
    horzObjects = []
    vertObjects = []

    for i in range(height): # rows
        for j in range(width): # columns
            if not(ima1[i,j,0] == 255 and ima1[i,j,1] == 255 and ima1[i,j,2] == 255):
                nonWhiteHorzPix.append((ima1[i,j,0],ima1[i,j,1],ima1[i,j,2]))#Adds the tuple for every pixel color (R,G,B)
                horzPos.append(j)#x
                horzVertPos.append(i)#y
    i = 0
    j = 0
    for i in (range(width)): # columns
        for j in (range(height)): # rows
            if not(ima1[j,i,0] == 255 and ima1[j,i,1] == 255 and ima1[j,i,2] == 255):
                nonWhiteVertPix.append((ima1[j,i,0],ima1[j,i,1],ima1[j,i,2]))#Adds the tuple for every pixel color (R,G,B)
                vertHorzPos.append(i)#x
                vertPos.append(j)#y
    see = False
    while i <= (len(nonWhiteHorzPix)-3):
        if not(see):
            see = checkVisibilityX(i)
            if(see):
                i -=1
        else:
            if ((horzVertPos[i] == horzVertPos[i+1]) and  horzPos[i+1]-horzPos[i] == 1):
                if nonWhiteHorzPix[i] == nonWhiteHorzPix[i+1]:
                    horzLength += 1
                    i+=1
                else:
                    horzObjects.append(horzLength)
                    see = False
        i += 1
    see = False
    i = 0
    while i <= (len(nonWhiteVertPix)-3):
        if not(see):
            see = checkVisibilityY(i)
            if(see):
                i -=1
        else:
            if ((vertHorzPos[i] == vertHorzPos[i+1]) and  vertPos[i+1]-vertPos[i] == 1):
                if nonWhiteVertPix[i] == nonWhiteVertPix[i+1]:
                    vertLength += 1
                    i+=1
                else:
                    vertObjects.append(vertLength)
                    see = False
        i += 1
    print("Horz Obj.",len(horzObjects))
    print("Vert Obj.", len(vertObjects))


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
