#! /usr/bin/env python3
"""
Displays an archery target using Zelle's graphics.py library.

The archery target consists of a central circle of yellow surrounded by
concentric rings of red, blue, black and white. Each ring has the same width,
which is the same as the radius of the yellow circle.
"""
from graphics import Circle, GraphWin, Point


def draw_target(bullseye_radius=25):
    """
    Draws the target.

    Keyword Arguments:
        bullseye_radius -- radius of the yellow "bullseye" circle (default: {25})

    All measurements used to draw the target are based off the supplied radius
    of the center, yellow circle.
    """
    rings = zip(range(5, 0, -1), ["red", "blue", "black", "white", "yellow"])
    win = GraphWin("Archery Target", bullseye_radius * 11, bullseye_radius * 11)
    win.setBackground("gray23")
    center = Point(win.width / 2, win.height / 2)
    for ring in rings:
        c = Circle(center, bullseye_radius * ring[0])
        c.setFill(ring[1])
        c.draw(win)
    win.getMouse()
    win.close()


if __name__ == "__main__":
    draw_target()
