#! /usr/bin/env python3
"""
Draws a house based on input from the user and displays.

The first two clicks will be the opposite corners of the rectangular frame of
the house. The third click will indicate the center of the top edge of a
rectangular door. The door should have a total width that is 1/5 of the width
of the house frame. The sides of the door should extend from the corners of the
top down to the bottom of the frame. The fourth click will indicate the center
of a square window. The window is half as wide as the door. The last click
will indicate the peak of the roof. The edges of the roof will extend from the
point at the peak to the corners of the top edge of the house frame.
"""
from graphics import GraphWin, Line, Point, Rectangle

if __name__ == "__main__":
    """
    Here is a really ugly, monolithic function to draw the house.
    """
    win = GraphWin("house.py", 800, 800)
    # draw house frame
    p1 = win.getMouse()
    p2 = win.getMouse()
    house_frame = Rectangle(p2, p1)
    house_frame.draw(win)

    # draw door
    house_width = abs(p1.getX() - p2.getX())
    house_height = abs(p1.getY() - p2.getY())
    door_center = win.getMouse()
    door_width = house_width / 5
    door_top_left = Point(door_center.getX() - door_width / 2, door_center.getY())
    door_bottom_right = Point(door_center.getX() + door_width / 2, p1.getY())
    door = Rectangle(door_top_left, door_bottom_right)
    door.draw(win)

    # draw window
    window_width = door_width / 4
    window_center = win.getMouse()
    window = Rectangle(
        Point(window_center.getX() - window_width, window_center.getY() - window_width),
        Point(window_center.getX() + window_width, window_center.getY() + window_width),
    )
    window.draw(win)

    # draw roof
    peak = win.getMouse()
    l1 = Line(peak, p2)
    l2 = Line(peak, Point(p1.getX(), p1.getY() - house_height))
    l1.draw(win)
    l2.draw(win)

    # pause so the user can admire their work
    win.getMouse()
    win.close
