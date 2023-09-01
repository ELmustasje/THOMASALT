import tkinter as tk
import math


def draw_flower(canvas):
    canvas.delete("all")
    width, height = canvas.winfo_width(), canvas.winfo_height()
    center_x, center_y = width // 2, height // 2

    # Draw the flower petals
    petal_radius = 40
    petal_distance = 80
    num_petals = 6
    angle_increment = 360 / num_petals

    for _ in range(num_petals):
        angle_deg = _ * angle_increment
        angle_rad = math.radians(angle_deg)

        x1 = center_x + petal_distance * math.cos(angle_rad)
        y1 = center_y - petal_distance * math.sin(angle_rad)

        x2 = x1 + petal_radius * math.cos(angle_rad + math.pi / 2)
        y2 = y1 - petal_radius * math.sin(angle_rad + math.pi / 2)

        x3 = x1 + petal_radius * math.cos(angle_rad - math.pi / 2)
        y3 = y1 - petal_radius * math.sin(angle_rad - math.pi / 2)

        canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="red")

    # Draw the flower center
    canvas.create_oval(
        center_x - 20, center_y - 20, center_x + 20, center_y + 20, fill="yellow"
    )


# Create the main window
root = tk.Tk()
root.title("Flower with Tkinter")

# Create a canvas for drawing
canvas = tk.Canvas(root, width=200, height=200, bg="white")
canvas.pack()

# Create a button to draw the flower
draw_button = tk.Button(root, text="Draw Flower", command=lambda: draw_flower(canvas))
draw_button.pack()

# Run the Tkinter main loop
root.mainloop()
