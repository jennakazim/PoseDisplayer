import tkinter as tk
from tkinter import PhotoImage

import time


# import pygame
# from pygame import mixer

# Create the main window
root = tk.Tk()
root.title("Pose Displayer")
root.geometry("800x600") 

poses = ["images/rest.png", "images/peace.png", 
         "images/rest.png", "images/pointer.png",
         "images/rest.png" , "images/pointerAndIndex.png",
         "images/rest.png" , "images/fingersCrossed.png",
         "images/rest.png", "images/fist.png"]

# Create a label widget
label = tk.Label(root, text="Click to start posing!")
label.pack(pady=20) 
start = False


# def test_timer_loop(sec=10, iter=0):
#     while iter < len(poses):    
#         print(iter)    
#         iter += 1
        



# create the timer
def timer_loop(iter, sec=10):
    if sec > 0 and iter < 9:
        # print("TIME " + str(sec))
        timer.config(text=f"{sec}")
        timer.after(1000, timer_loop, iter, sec-1) # loop every 1000 milliseconds
    elif sec <= 0 and iter < 9:
        timer.config(text="")
        timer_loop(iter+1)
    else:
        return
        


def change_image(iter):
    iter+=1
    if iter < 10:
        image.config(file=poses[iter])
        image_label.after(10000, change_image, iter)
      
        

# Create a button
def on_button_click():
    global start
    
    iter = 0
    
    # Toggle the start flag and update UI accordingly
    if start:
        # currently running -> stop posing
        label.config(text="Click (with free hand) to start posing!")
        button.config(text="Start")
        start = False
        
        image.config(file="")
        
    else:
        # currently stopped -> start posing
        label.config(text="Click to stop posing!")
        button.config(text="Stop")
        start = True
        
        iter_1 = 0
        iter_2 = 0

        image.config(file=poses[0])
        timer_loop(iter_1)
        image_label.after(10000, change_image, iter_2)

            

button = tk.Button(root, text="Start", command=on_button_click)
button.pack()


image = PhotoImage(file="")
image_label = tk.Label(root, image=image)
image_label.pack()

timer = tk.Label(root, text="")
timer.pack(pady=20) # or whatever layout you want

# modulemixer.init() # Initialize the mixer 

# Start the Tkinter event loop
root.mainloop()