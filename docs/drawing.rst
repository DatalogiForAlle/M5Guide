.. highlight:: python

Drawing on the screen
=====================

.. get documentation from https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/display

In this part of the M5 Guide, we show how to draw images, shapes and
text on the screen, and how to change the screen orientation.

First you need to import the ``lcd`` object from the ``m5stack``
module::

   from m5stack import lcd

You are now ready to begin drawing, for example to draw a rectangle,
call the function :func:`lcd.rect`::

  lcd.rect(10, 20, 40, 70)

The two first values given to :func:`lcd.rect` determines where the
rectangle should be drawn, the last two gives the width and the height
of the rectangle.

By default most functions will draw shapes using a white color, but it
can be changed by supplying a color value. These are typically
specified as hexadecimal values, such as ``0xFFFF00`` for yellow. `Read more about hexadecimal color
values
<https://www.finalsitesupport.com/hc/en-us/articles/115000768887-Hexadecimal-color-values>`_



Screen orientation and size
---------------------------
.. function:: lcd.orient(orientation)

   Changes screen orientation and clears the screen.
              
   :param orientation: must be one of:
   * ``lcd.PORTRAIT`` (default): portrait mode
   * ``lcd.LANDSCAPE``: landscape mode
   * ``lcd.PORTRAIT_FLIP``: flipped portrait (upside down)
   * ``lcd.LANDSCAPE_FLIP``: flipped landscape mode

   For example, to use landscape mode::

     lcd.orient(lcd.LANDSCAPE)

.. function:: lcd.screensize()

   :rtype: `(int, int)`

   Gets the screen size in pixels, for example::

     (screen_width, screen_height) = lcd.screensize()


Drawing shapes
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

.. function:: lcd.roundrect(x, y, height, width, r)
              lcd.roundrect(x, y, height, width, r, color)
              lcd.roundrect(x, y, height, width, r, color, fillcolor)

   Defaults to white border, no fill
              
.. function:: lcd.pixel(x, y)
              lcd.pixel(x, y, color)

   Defaults to white

.. function:: lcd.line(x1, y1, x2, y2)
              lcd.line(x1, y1, x2, y2, color)

   Defaults to white

.. function:: lcd.triangle(x1, y1, x2, y2, x3, y3)
              lcd.triangle(x1, y1, x2, y2, x3, y3, color)
              lcd.triangle(x1, y1, x2, y2, x3, y3, color, fillcolor)

   Defaults to white border, no fill.

.. function:: lcd.ellipse(x, y, width, height)
              lcd.ellipse(x, y, width, height, opt, color)
              lcd.ellipse(x, y, width, height, opt, color, fillcolor)

   Defaults to white border, no fill.

   If you want to choose color, always supply the number ``15`` as the
   `opt` parameter.


.. function:: lcd.circle(x, y, radius)
              lcd.circle(x, y, radius, color)
              lcd.circle(x, y, radius, color, fillcolor)

   Defaults to white border, no fill.


.. function:: lcd.arc(x, y, radius, thickness, start, end)
              lcd.arc(x, y, radius, thickness, start, end, color)
              lcd.arc(x, y, radius, thickness, start, end, color, fillcolor)

   Defaults to white border, no fill.

   :param x: Number: center x-coordinate
   :param y: Number: center y-coordinate
   :param radius: radius of arc
   :param thickness: Number: thickness of border
   :param start: Number: start angle in degrees (0°-360°)
   :param end: Number: end angle in degrees (0°-360°)


.. function:: lcd.polygon(x, y, radius, sides, thickness)
              lcd.polygon(x, y, radius, sides, thickness, color)
              lcd.polygon(x, y, radius, sides, thickness, color, fillcolor)
              lcd.polygon(x, y, radius, sides, thickness, color, fillcolor, rotate=0)

   Defaults to white border, no fill.

   The ``fillcolor`` argument to :func:`lcd.polygon` appears buggy, so you might experience
   some difficulty.

   :param x: Number: center x-coordinate
   :param y: Number: center y-coordinate
   :param radius: Number: radius of polygon
   :param radius: Number: number of sides of the polygon
   :param thickness: Number: thickness of border
   :param rotate: Number: angle to rotate in degrees (0°-360°)


.. function:: lcd.image(x, y, filename)

   :param x: Number: x-coordinate
   :param y: Number: y-coordinate
   :param filename: String: filename of image file, e.g. ``"img.bmp"``

   Supports ``.bmp`` and ``.jpg``
              

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


Drawing text
------------
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

.. function:: lcd.setTextColor(0x000000, 0xffffff)
   
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
