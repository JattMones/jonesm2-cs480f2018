## readME:


This projects started as a simple idea of scanning pixels in an image for a similar color. However after analyzing the results of this method, we realized the program was doing a lot of unnecessary work. Now, our project looks for 3 pixels (in the x and y direction) of similar color (that's about 1/32 of an inch), and ignores all "white space pixels" and other pixels in the image. To run, simply run test.py, with one of the image test files in the testImages folder.

Example of cmd line call to our program:
pip install matplotlib
python test.py ..\testImages\line.png

##Update:

Code currently doesn't find any objects in the command above, however if you run our old version called "imageScanner.py" on one of the images, you'll see that our method for scanning and collecting objects is solid. We are just working out some kinks in our new program.
