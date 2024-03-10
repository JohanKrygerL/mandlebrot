import cmath
import tkinter as tk
import numpy as np

#window size
x_length = 400
x_origin = x_length*0.75
y_length = int(x_length/2)
y_origin = y_length*0.5

#how many max itterations 
#resolution
out_of_bounds_max_count = 100

#lower more zoomed 3 is good
zoom = 1

def calculations(x_cord,y_cord):
    
    x_max = zoom
    y_max = x_max/3

    x_holder = (x_cord-x_origin)/(x_origin/x_max)
    y_holder = -(y_cord-y_origin)/(y_origin/y_max)

    #coordinate to complex number and put into c:

    c = complex(x_holder,y_holder)
    z = complex(0,0)
    out_of_bounds_count = 0 
    for i in range(out_of_bounds_max_count):
        z = z*z+c
        if(abs(z.real) > 2 or abs(z.imag) > 2):
            return i
    return out_of_bounds_max_count

def draw_pixel(canvas, x, y, color):
    canvas.create_rectangle(x, y, x+1, y+1, fill=color, outline=color)

def create_pixel_grid():
    # Define dimensions
    rows = x_length
    cols = y_length

    # Create an empty 2D array filled with zeros
    grid = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):
            grid[i][j] = calculations(i,j)
    print(grid)
    return grid

def color_grid(grid):
    rows = x_length
    cols = y_length
    # Create a NumPy array with dtype 'object' (allows arbitrary Python objects)
    color_grid = np.empty((rows, cols), dtype=object)

    # Initialize each element with an empty string
    color_grid.fill('')


    for i in range(x_length):
        for j in range(y_length):
            if (grid[i][j] < (1*out_of_bounds_max_count)/5):
                color_grid[i][j] = "red"
            elif (grid[i][j] < (2*out_of_bounds_max_count)/5):
                color_grid[i][j] = "green"
            elif (grid[i][j] < (3*out_of_bounds_max_count)/5):
                color_grid[i][j] = "blue"
            elif (grid[i][j] < (4*out_of_bounds_max_count)/5):
                color_grid[i][j] = "yellow"
            elif (grid[i][j] < (5*out_of_bounds_max_count)/5):
                color_grid[i][j] = "purple"
            else:
                color_grid[i][j] = "black"
    return color_grid


    




def main():
    

    grid = create_pixel_grid()
    c_grid = color_grid(grid)
    

    # Create a Tkinter window
    root = tk.Tk()
    root.title("Single Pixel Drawing")

    # Create a canvas
    canvas = tk.Canvas(root, width=x_length, height=y_length)
    canvas.pack()


    for i in range(x_length):
        for j in range(y_length):
            
            draw_pixel(canvas, i, j, c_grid[i][j])

    # Run the Tkinter event loop
    root.mainloop()


main()


