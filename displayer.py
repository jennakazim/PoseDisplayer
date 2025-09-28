import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Pose Displayer")
root.geometry("1920x1080") # Set window size (width x height)

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20) # Add padding around the label

# Create a button widget
def on_button_click():
    label.config(text="Button Clicked!")

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

# Start the Tkinter event loop
root.mainloop()