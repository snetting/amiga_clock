import time
import math
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw

# Dimensions of the window
win_width = 200
win_height = 300

# Radius of clock
radius = 80

# Initialize Tkinter window
root = tk.Tk()
root.geometry(f'{win_width}x{win_height}')

# Load an image
image = Image.open('amiga_clock.png')
image = image.resize((win_width, win_height), Image.ANTIALIAS)

def draw_clock():
    # Copy original image
    copy_image = image.copy()
    draw = ImageDraw.Draw(copy_image)

    # Get current time
    curr_time = time.localtime()
    hours = curr_time.tm_hour
    minutes = curr_time.tm_min
    seconds = curr_time.tm_sec

    # Calculate angles of the clock hands
    hour_angle = math.pi / 6 * (hours % 12 - 3)
    minute_angle = math.pi / 30 * (minutes - 15)
    second_angle = math.pi / 30 * (seconds - 15)

    # Draw the clock hands
    draw.line((win_width/2, win_height/2,
               win_width/2 + radius/2 * math.cos(hour_angle),
               win_height/2 + radius/2 * math.sin(hour_angle)), fill='black')
    draw.line((win_width/2, win_height/2,
               win_width/2 + radius * math.cos(minute_angle),
               win_height/2 + radius * math.sin(minute_angle)), fill='black')
    draw.line((win_width/2, win_height/2,
               win_width/2 + radius * math.cos(second_angle),
               win_height/2 + radius * math.sin(second_angle)), fill='black')

    # Convert image for Tkinter
    tk_image = ImageTk.PhotoImage(copy_image)

    # Display image on a label
    label = tk.Label(root, image=tk_image)
    label.place(x=0, y=0, relwidth=1, relheight=1)

    # Keep a reference to the image to prevent garbage collection
    label.image = tk_image

    # Redraw clock every second
    root.after(1000, draw_clock)

draw_clock()

# Start the GUI
root.mainloop()

