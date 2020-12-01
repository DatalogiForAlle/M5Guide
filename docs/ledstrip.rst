LEDStrip/NeoPixel
=================

Tilslut jeres LED-strip som vist på billedet. Brug et mellemled (3 x
jumper kabel):

.. figure:: illustrationer/ledstrip_connection.png
   :alt: LEDStrip forbindelser
   :width: 500px

Forbindelserne er:
           
.. list-table::
   :header-rows: 1

   * - Type
     - Microcontroller
     - LED-strip ledning
   * - Jord
     - GND
     - Hvid
   * - Strøm (3,3 volt)
     - 3V3
     - Rød
   * - Data/kontrolsignal
     - G26
     - Grøn


Åbn Mu-editoren. Opret en fil “intro.py” med dette indhold::
  
  import machine
  import neopixel

  # 30 LED’er tilsluttet pin 26
  ledstrip = neopixel.NeoPixel(machine.Pin(26), 30)

  # Indstil LED’ernes farver
  ledstrip[0] = (255, 0, 0)
  ledstrip[9] = (0, 0, 255)

  # Opdater LED’erne ved at kalde ledstrip.write()
  ledstrip.write()

**Afprøv programmet:**

* Tryk på Run-knappen i Mu for at køre programmet på M5StickC.
* Tjek, at den første diode lyser rødt (diode 0) og den tiende lyser blåt (diode 9).
* Hvis det ikke virker, så tjek dine forbindelser
  
**Øvelse:**

 * Udvid programmet, så hver anden diode farves rød og hver anden
   farves blå for de første 10 dioder.

Navngiv farver
--------------
Vi kan gøre programmet nemmere at læse, ved at give navne til
farvekoderne::

  # Opret nye navne ’red’ og ’blue’
  red = (255, 0, 0)
  blue = (0, 0, 255)

  # Brug navne i koden - det gør det nemt at læse og ændre
  ledstrip[0] = red
  ledstrip[1] = blue
  ledstrip[2] = red
  ...
  ledstrip[9] = blue
  ledstrip.write()

**Bemærk:** med LEDstrippen angives farverne som tal mellem 0-255 for
hvert af rød grøn og blå, mens til LCD-displayet angives det som
hexadecimale farvekoder. Vi beklager forvirringen.

Animationer
-----------
For at lave animationer skal vi bruge funktionen sleep_ms fra biblioteket time::

  import machine
  import neopixel
  import time
  
  ledstrip = neopixel.NeoPixel(machine.Pin(26), 30)
  
  # Tænd den første diode
  ledstrip[0] = (255, 0, 0)
  ledstrip.write()
  time.sleep_ms(200) # Vent 200 millisekunder

  # Tænd den næste diode
  ledstrip[1] = (0, 0, 255)
  ledstrip.write()
  time.sleep_ms(200) # Vent 200 millisekunder

  # Fortsæt selv ...

**Øvelser:**

* Fortsæt mønsteret for de første 10 LED’er.

* Lav en variabel til at styre hastigheden (i stedet for at gentage "200")

* En LED slukkes ved at sætte den til (0, 0, 0). Sluk den forrige
    LED i hvert trin, så der kun er en LED tændt ad gangen.

Flere farver
------------

.. list-table::

 * - **Rød** (255, 0, 0)
   - **Grøn** (0, 255, 0)
   - **Blå** (0, 0, 255)
 * - **Gul** (255, 255, 0)
   - **Lilla** (127, 0, 255)
   - **Tyrkis** (0, 255, 255)

Flere muligheder
----------------

I kan også gøre brug af funktionerne ``ledstrip.fill(farve)``,
``ledstrip.clear()`` eller ``ledstrip.fillN(farve, antal)``, der
hhv. tænder alle, slukker alle eller tænder et specifikt antal LED’er.

..
    Tutorial: tilslutning og programmering af LED Strip
   ---------------------------------------------------

   Formål
   ------
    - Vis hvordan man tilslutter og programmerer en LED Strip.
    - Vise hvordan man bruger for-loops

   Fx projekt om æggeuret fra kickstart-kurset, eller vise data hentet
   fra internettet på led-strippen.

