from graphics import *

win = GraphWin("Demo Window")
c = Circle(Point(50, 50), 10)
c.draw(win)
win.getMouse()  # wait for mouse click
win.close()
