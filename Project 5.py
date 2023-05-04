#!/usr/bin/env python
# coding: utf-8

# In[12]:


#Imported libraries
import numpy as np
import cv2 as cv
import time
import math





#Sets up arena with obstacles
def setup(s, r):

    global arena
    
    #Colors
    white = (255, 255, 255)
    gray = (177, 177, 177)
    darkGray = (104, 104, 104)
    
    #Draw Radial Clearance
    for x in range(0, 500):

        for y in range(0, 400):
        
            if checkClearance(x, y, s, r):
                arena[y, x] = darkGray
    
    #Draw Obstacle Borders
    for x in range(0, 500):

        for y in range(0, 400):
        
            if checkBorder(x, y, s):
                arena[y, x] = gray
    
    #Draw Obstacles
    for x in range(0, 500):

        for y in range(0, 400):
        
            if checkObstacle(x, y):
                arena[y, x] = white
                
#Checks to see if a point is within an obstacle
def checkObstacle(x, y):
    
    #Left Squares
    if x >= 50 and x < 150:
        
        if (y >= 50 and y < 150) or (y >= 250 and y < 350):
            return True
    
    #Right Squares
    if x >= 350 and x < 450:
        
        if (y >= 50 and y < 150) or (y >= 250 and y < 350):
            return True
        
    #Left M Rectangle
    if x >= 175 and x < 185:
        
        if y >= 125 and y < 275:
            return True
    
    #Right M Rectangle
    if x >= 315 and x < 325:
        
        if y >= 125 and y < 275:
            return True
        
    #Left M Parallelogram
    if x >= 185 and x < 250:
        
        if (y >= (27/13) * x - (3370/13)) and (y < (27/13) * x - (3175/13)):
            return True
        
    #Right M Parallelogram
    if x >= 250 and x < 315:
        
        if (y >= (-27/13) * x + (10130/13)) and (y < (-27/13) * x + (10325/13)):
            return True
    
    #Circle
    #if (x - 400) * (x - 400) + (y - 110) * (y - 110) <= 50*50:
        #return True
        
    return False
  
#Checks to see if a point is within the border of an obstacle
def checkBorder(x, y, s):
    
    slopeHeight = int(round(s/math.cos(math.radians(64.29))))
    
    #Left Squares
    if x >= 50 - s and x < 150 + s:
        
        if (y >= 50 - s and y < 150 + s) or (y >= 250 - s and y < 350 + s):
            return True
    
    #Right Squares
    if x >= 350 - s and x < 450 + s:
        
        if (y >= 50 - s and y < 150 + s) or (y >= 250 - s and y < 350 + s):
            return True
        
    #Left M Rectangle
    if x >= 175 - s and x < 185 + s:
        
        if y >= 125 - s and y < 275 + s:
            return True
    
    #Right M Rectangle
    if x >= 315 - s and x < 325 + s:
        
        if y >= 125 - s and y < 275 + s:
            return True
        
    #Left M Parallelogram
    if x >= 185 and x < 250:
        
        if (y >= (27/13) * x - (3370/13) - slopeHeight) and (y < (27/13) * x - (3175/13) + slopeHeight) and (y >= 125 - s) and (y <= 275 + s):
            return True
        
    #Right M Parallelogram
    if x >= 250 and x < 315:
        
        if (y >= (-27/13) * x + (10130/13) - slopeHeight) and (y < (-27/13) * x + (10325/13) + slopeHeight) and (y >= 125 - s) and (y <= 275 + s):
            return True

#Checks to see if a point is within radial clearance of a border
def checkClearance(x, y, s, r):
    
    rr = r - 1
    
    if rr == 0:
        return False
    
    slopeHeight = int(round((s + rr)/math.cos(math.radians(64.29))))
    
    #Left Squares
    if x >= 50 - s - rr and x < 150 + s + rr:
        
        if (y >= 50 - s - rr and y < 150 + s + rr) or (y >= 250 - s - rr and y < 350 + s + rr):
            return True
    
    #Right Squares
    if x >= 350 - s - rr and x < 450 + s + rr:
        
        if (y >= 50 - s - rr and y < 150 + s + rr) or (y >= 250 - s - rr and y < 350 + s + rr):
            return True
        
    #Left M Rectangle
    if x >= 175 - s - rr and x < 185 + s + rr:
        
        if y >= 125 - s - rr and y < 275 + s + rr:
            return True
    
    #Right M Rectangle
    if x >= 315 - s - rr and x < 325 + s + rr:
        
        if y >= 125 - s - rr and y < 275 + s + rr:
            return True
        
    #Left M Parallelogram
    if x >= 185 and x < 250:
        
        if (y >= (27/13) * x - (3370/13) - slopeHeight) and (y < (27/13) * x - (3175/13) + slopeHeight) and (y >= 125 - s - rr) and (y <= 275 + s + rr):
            return True
        
    #Right M Parallelogram
    if x >= 250 and x < 315:
        
        if (y >= (-27/13) * x + (10130/13) - slopeHeight) and (y < (-27/13) * x + (10325/13) + slopeHeight) and (y >= 125 - s - rr) and (y <= 275 + s + rr):
            return True

#Checks to see if a point is valid (by checking obstacle, border, and clearance, as well as making sure the point is within arena bounds)
def checkValid(x, y, s, r):
    
    if checkObstacle(x, y):
        return False
    
    if checkBorder(x, y, s):
        return False
    
    if checkClearance(x, y, s, r):
        return False
    
    if (x < 0 or x >= 600 or y < 0 or y >= 250):
        return False
    
    return True





#Main Code
arena = np.zeros((400, 500, 3), dtype = "uint8")

setup(5, 10) #Change the values to change border size and robot radius, respectively
cv.imshow("Arena", arena)
cv.waitKey()
cv.destroyAllWindows()


# In[ ]:




