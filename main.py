# UnMouse 1.0 by DoguCigsar

import tkinter as tk
import random
import mouse
import time

root = tk.Tk()

#Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Get two random numbers between 0 and the screen width and height

x=0

print("<--UnMouse 1.0 by DoguCigsar-->")
print("https://github.com/DoguCigsar/")
print("https://instagram.com/dogucigsar/")
print("https://twitter.com/dogucigsar/")
print("<----------------------------->")

time.sleep(0.999)

#Loop until x equals 100
while x <= 7200:
    #Get random location to move the mouse at
    rand_width = random.randint(0, screen_width)
    rand_height = random.randint(0, screen_height)

    time.sleep(0.001)

    mouse.move(rand_width, rand_height, absolute=True, duration=0.5)
    print("Mouse moved to: " + str(rand_width) + "x" + str(rand_height))
    x = x + 1