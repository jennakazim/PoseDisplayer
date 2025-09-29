import tkinter as tk
from tkinter import PhotoImage

import time


# import pygame
# from pygame import mixer

# Create the main window
root = tk.Tk()
root.title("Pose Displayer")
root.geometry("1920x1080") 

poses = ["images/rest.png", "images/peace.png", 
         "images/rest.png", "images/pointer.png",
         "images/rest.png" , "images/pointerAndIndex.png",
         "images/rest.png" , "images/fingersCrossed.png",
         "images/rest.png", "images/fist.png"]

# Create a label widget
# add instructions before start

label = tk.Label(root, text='''You will be doing _ poses for 10 seconds each. The order of the individual poses is peace sign,\npointer extended, both pointer and middle extended together, fingers crossed, and fist.\nIn between each individual pose, you will do the rest pose (all five fingers extended naturally).\nPress start when you are ready to begin posing. It should take 1 minute and 40 seconds.''')
label.pack(pady=20) 
start = False


# create the timer
def timer_loop(iter, sec=10):
    
    if sec > 0 and iter < 10:
        # print("TIME " + str(sec))
        timer.config(text=f"{sec}")
        timer.after(1000, timer_loop, iter, sec-1) # loop every 1000 milliseconds
    elif sec <= 0 and iter == 9:
        timer.config(text="")
        timer_loop(iter+1)
    elif sec <= 0 and iter < 10:
        timer.config(text="")
        image.config(file=poses[iter+1])
        timer_loop(iter+1)
    else:
        return
        


def change_image():
    # image.config(file="images/hooray.png")
    label.config(text="Thanks for posing!")
        

# Create a button
def on_button_click():
    global start
    
    # Toggle the start flag and update UI accordingly
    if start:
        # currently running -> stop posing
        label.config(text="Click to start posing!")
        button.config(text="Start")
        start = False
        
        image.config(file="")
        
    else:
        # need to remove the stop button or it starts counting twice if they start again
        # currently stopped -> start posing
        button.pack_forget() # for removing the button
        # label.config(text="Click to stop posing!")
        # button.config(text="Stop")
        # start = True
        
        iter_1 = 0

        image.config(file=poses[0])
        timer_loop(iter_1)
        
        image_label.after(102000, change_image)
            

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