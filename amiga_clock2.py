import time
import math
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw

# Dimensions of the window
win_width = 200
win_height = 300

# Radius of clock
radius = 60

# Thickness of the clock hands
hand_thickness = 3
hand_thickness_second = 2

# Vertical Offset
vertical_offset = 10

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

    # Adjusted center
    center_x = win_width / 2
    center_y = win_height / 2 - vertical_offset

# Draw the clock hands
    draw.line((center_x, center_y,
               center_x + radius/2 * math.cos(hour_angle),
               center_y + radius/2 * math.sin(hour_angle)), fill='black', width=hand_thickness)
    draw.line((center_x, center_y,
               center_x + radius * math.cos(minute_angle),
               center_y + radius * math.sin(minute_angle)), fill='black', width=hand_thickness)
    draw.line((center_x, center_y,
               center_x + radius * math.cos(second_angle),
               center_y + radius * math.sin(second_angle)), fill='black', width=hand_thickness_second)

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
