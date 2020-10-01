.. highlight:: python

Drawing on the screen
=====================

In this part of the guide, we go through all the drawing primitives of
the M5StickC MicroPython library. You need to begin by importing the
``lcd`` object from the ``m5stack`` module::

   from m5stack import lcd

Then you can start calling various functions on the ``lcd`` object,
for example to draw a circle, type in::

  lcd.ellipse(50, 20, 10, 10)

In the last part of this section, we explain how to set rotation and
brightness of the screen.


Screen rotation
---------------
.. function:: lcd.setRotation(rotation_mode)

   :param rotation_mode: ``0`` (the default), ``1``, ``2``, or ``3``.

   Rotates and clears the screen, all following drawing operations
   will follow the defined orientation

   * ``0``: the default orientation
   * ``1``: turn 90 degrees clockwise, compared to the default
   * ``2``: upside down, compared to the default
   * ``3``: turn 90 degrees counter-clockwise, compared to the default

Drawing commands
----------------
.. function:: lcd.clear()
              lcd.clear(color)

   Clears everything on the screen, and paints it black. The `color`
   argument can change which color is used, and should be given in
   hexadecimal.

   For example, to paint the screen yellow, you can call it like this::

     lcd.clear(0xFFFF00)

.. function:: lcd.rect(x, y, height, width)
              lcd.rect(x, y, height, width, color)
              lcd.rect(x, y, height, width, color, fillcolor)

   Draw a rectangle, starting with the top-right corner at the given
   `x` and `y` coordinates. The `height` and `width` parameters adjust
   the size of the rectangle.

   By default, only a white border around the rectangle is drawn.

   An optional `color` argument specifies the border color of the
   rectangle. The color is given as a hexadecimal value.

   A second optional `fillcolor` argument specifies that the rectangle
   should be filled in the given color. The fillcolor is given as a
   hexadecimal value.

   For example, to draw a rectangle with red border and filled with black::

     lcd.rect(10, 10, 40, 30, 0xFF0000, 0x000000)


   :param x: Number: x-coordinate of the rectangle
   :param y: Number: y-coordinate of the rectangle
   :param width: Number: width of the rectangle
   :param height: Number: height of the rectangle
   :param color: Number: border color (optional)
   :param fillcolor: Number: fill color (optional)

.. function:: lcd.text(x, y, msg)
              lcd.text(x, y, msg, color)
              lcd.text(x, y, msg, color, transparent=True)

   Display the string `msg` on the screen at the given coordinates `x`
   and `y`.

   The `color` of the text defaults to white, but can also be specified as
   third argument in hexadecimal (e.g ``0xFF0000`` for red,
   ``0x00FF00`` for green)

   The default behavior is to print the text on black background, if
   you want to disable this, and print on a transparent background add
   ``transparent=True`` as a keyword argument.

   To change which font is used, use the function :func:`lcd.font`.

   Aligning text in the center of the screen, can be done by replacing
   either `x` or `y`, or both, with the special value :const:`lcd.CENTER`

..
   **DONE:**
   ::
      lcd.clear(color=0x000000)
      lcd.text(x, y, 'hello world', color=0xffffff, transparent=True)
      lcd.print('hello world', x, y, color=0xffffff, transparent=True)
      lcd.rect(x, y, width, height, color=0xffffff, fillcolor=0xffffff)

   **TODO:**
   ::
      lcd.pixel(x, y, 0xffffff)
      lcd.line(x1, y1, x2, y2, 0xffffff)
      lcd.triangle(x1, y1, x2, y2, x3, y3, color=0xffffff, fillcolor=0xffffff)
      lcd.circle(x, y, radius, color=0xffffff, fillcolor=0xffffff)
      lcd.ellipse(x, y, rx, ry, color=0xffffff, fillcolor=0xffffff)
      lcd.arc(x, y, radius, thick, start, end, color=0xffffff, fillcolor=0xffffff)
      lcd.polygon(x, y, radius, sides, thick, color=0xffffff, fillcolor=0xffffff, rotate=10)


Change font
-----------
.. function:: lcd.font(font)

   ``lcd.font(lcd.FONT_Default)``

..
      ::

         Alternative fonts:
         - lcd.FONT_Default
         - lcd.FONT_DefaultSmall
         - lcd.FONT_DejaVu18
         - lcd.FONT_DejaVu24
         - lcd.FONT_DejaVu40
         - lcd.FONT_DejaVu56
         - lcd.FONT_DejaVu72
         - lcd.FONT_Ubuntu
         - lcd.FONT_Comic
