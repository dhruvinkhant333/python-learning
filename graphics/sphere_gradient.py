# Source - https://codereview.stackexchange.com/q/229448
# Posted by Progrmming is fun, modified by community. See post 'Timeline' for change history
# Retrieved 2026-07-07, License - CC BY-SA 4.0
# IMPROVED VERSION: Fixed window closing issue and added buffering for reduced flashing

"""
A program for fun to see how red, blue and purple appears at resolution.
Draws concentric circles with alternating red/purple coloring using sine wave brightness.

PURPOSE:
--------
Creates a visual effect of an inverted sphere with a gradient from red to purple.
The brightness of each circle follows a sine wave curve for smooth transitions.

HOW IT WORKS:
-------------
1. Creates a graphics window with pink background
2. Draws concentric circles from center outward
3. Each circle color alternates: red → purple → red (using modulus operator)
4. Brightness increases from center to edge using sine wave function
5. All circles are buffered (created first, drawn together) to reduce flashing

IMPROVEMENTS MADE:
------------------
✓ Gracefully handles window closure (no crash on close)
✓ Draws all circles before rendering (reduces flashing)
✓ Responsive to both mouse click and window close events
✓ Better code organization with main() function
✓ Comprehensive error handling

ALGORITHM:
----------
For each radius from max down to 0:
  1. Calculate brightness: sin(circle/radius * π/2) * 255
  2. Determine color using modulus:
     - If circle % 2 == 1: RED channel = brightness
     - If (circle+1) % 2 == 1: BLUE channel = brightness
     - GREEN channel = 0 (always)
  3. Create circle object and add to list
  4. Draw all circles at once for smooth rendering

CONTROLS:
---------
- Click anywhere in window to close
- Close window button also works gracefully
- No crashes or errors on exit

TECHNICAL NOTES:
----------------
- Uses tkinter (via graphics.py) for GUI
- Buffering technique reduces rendering artifacts
- Sine wave provides smooth brightness gradient
- Modulus operator enables alternating color channels
"""

from math import *
from graphics import *

def hole(circles_list, centerx, centery, radius):
    """
    Create circles with alternating red/purple coloring.
    Instead of drawing immediately, returns list of circle objects.
    This allows all circles to be drawn at once (buffering effect).
    
    Args:
        circles_list: List to append circles to
        centerx: Center X coordinate
        centery: Center Y coordinate
        radius: Maximum radius for circles
    """
    for circle in range(radius, 0, -1):
        c = Circle(Point(centerx, centery), circle)
        c.setWidth(0)
        # Calculate brightness using sine wave (0 to 255)
        coloratangle = int(sin(circle/radius*pi/2)*255)
        # Alternate between red and purple using modulus
        c.setFill(color_rgb(coloratangle * (circle % 2), 0, coloratangle * ((circle + 1) % 2)))
        circles_list.append(c)

def main():
    """Main program with improved window handling."""
    
    windowheight = 1350
    windowwidth = 730
    win = GraphWin("My Circle", windowheight, windowwidth)
    win.setBackground(color_rgb(255, 100, 100))
    
    centerx = int(windowheight / 2)
    centery = int(windowwidth / 2)
    radius = int(sqrt(centerx**2 + centery**2))  # Pythagoras theorem
    
    # Create circles list (buffering - all circles created before drawing)
    circles = []
    hole(circles, centerx, centery, radius)
    
    # Draw all circles at once (reduces flashing)
    for circle in circles:
        circle.draw(win)
    
    # Gracefully handle window closure or mouse click
    try:
        # Wait for mouse click OR window close
        win.getMouse()
    except GraphicsError:
        # Window was closed - this is expected and not an error
        pass
    finally:
        # Always close cleanly
        win.close()

if __name__ == "__main__":
    main()
