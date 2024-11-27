# mandelbrot.py
# Lab 9
# Name: Yahia Abdelsalam
# Pledge: "I pledge my honor that I have abided by the Stevens Honor System"

# keep this import line...
from cs5png import PNGImage


# Part 1: Define the mult function
def mult(c, n):
    """ Returns the product of c and n by repeated addition. """
    result = 0
    for i in range(n):  #
        result += c
    return result

# Part 2: Define the update function for the Mandelbrot update step
def update(c, n):
    """ Starts with z = 0 and performs z = z**2 + c a total of n times, returning the final z. """
    z = 0
    for i in range(n):  
        z = z**2 + c
    return z

# Part 3: Define the inMSet function to check if a point is in the Mandelbrot set
def inMSet(c, n):
    """ Returns True if the complex number c is in the Mandelbrot set, False otherwise. """
    z = 0
    for i in range(n):  
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True

# Part 4: Define the scale function to map pixel coordinates to the complex plane
def scale(pix, pixMax, floatMin, floatMax):
    """ Maps a pixel coordinate to a complex plane coordinate. """
    return floatMin + (floatMax - floatMin) * pix / pixMax


# Part 5: Define the mset function to create the Mandelbrot set image
def mset(width, height):
    """ Creates an image of the Mandelbrot set with the specified width and height. """
    # Initialize the image
    image = PNGImage(width, height)
    
    for col in range(width):
        for row in range(height):
            x = scale(col, width, -2, 1)    
            y = scale(row, height, -1, 1)     
            
            # Create the complex number c
            c = x + y * 1j
            
            # Determine if the complex number c is in the Mandelbrot set
            if inMSet(c, 25):  
                image.plotPoint(col, row)

    image.saveFile()
# This generates pixle image of the Mandelbrot and saves it as a png file
mset(350, 540)
    
