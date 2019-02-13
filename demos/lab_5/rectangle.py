#! /usr/bin/env python3
"""
Draws a rectangle based on input from the user and displays its area and
perimeter.

The user will click the graphics window twice, each click specifying opposite
corners of the rectanble.
"""
from tkinter import messagebox
from graphics import GraphWin, Point, Rectangle


def calculate_area(length, width):
    """
    Calculates the area of a rectangle with dimensions length and width.
    """
    return length * width


def calculate_dimensions(point1, point2):
    """
    Calculates the length and width of a rectangle with opposite corners
    defined by point1 and point2.
    """
    return abs(point1.getX() - point2.getX()), abs(point1.getY() - point2.getY())


def calculate_perimeter(length, width):
    """
    Calculates the perimeter of a rectangle with dimensions length and width.
    """
    return 2 * length + 2 * width


def display_info(area, perimeter):
    """
    Displays the calculated area and perimeter.
    """
    messagebox.showinfo(
        "Information", f"Area: {int(area):,}\nPerimeter: {int(perimeter):,}"
    )


def draw_rectangle(win, p1, p2):
    """
    Draws a rectangle with opposite corners specified by mouse clicks and
    displays
    """
    rectangle = Rectangle(p1, p2)
    rectangle.setWidth(3)
    rectangle.draw(win)


def get_rectangle_coordinates(win):
    """
    Gets the coordinates of two opposite points that define a rectangle and
    returns them as Point objects.
    """
    point_1 = win.getMouse()
    point_2 = win.getMouse()
    return point_1, point_2


if __name__ == "__main__":
    # a very procedural programming approach ;)
    # create GraphWin object
    win = GraphWin("rectangle.py", 600, 600)

    # get corners
    p1, p2 = get_rectangle_coordinates(win)

    # draw the rectangle
    draw_rectangle(win, p1, p2)

    # calculate the rectangle's length and width
    length, width = calculate_dimensions(p1, p2)

    # calculate the rectangle's area
    area = calculate_area(length, width)

    # calculate the rectangle's perimeter
    perimeter = calculate_perimeter(length, width)

    # display the rectangle's area and perimeter to the user
    display_info(area, perimeter)

    # wait for user to dismiss the GrapWin window and clean up
    win.getMouse()
    win.close()
