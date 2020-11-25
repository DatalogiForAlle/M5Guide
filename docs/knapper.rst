Knaptryk og indbygget LED
=========================
M5StickC har to knapper vi kan programmere. Den under skærmen kaldes
knap A, og den på højre side kaldes knap B. Den sidste knap på venstre
side bruges til at tænde og slukke M5StickC (sluk ved at holde nede i
6 sekunder).

I det ene hjørne, inde bag plastikken, sidder en LED man kan tænde og
slukke.


.. todo:: illustration med angivelse af knapper og LED

.. _knaptryk:

Registrere knaptryk
-------------------
For at registrere knaptryk på knap A, skal vi bruge følgende
kode. Prøv at tast det ind::

  from m5stack import btnA

  def knapAPressed():
    print("Hello")

  btnA.wasPressed(knapAPressed)

Den første linje importerer ``btnA``. De næste linjer definerer en
funktion hvor vi fortæller hvad der skal ske, når man klikker på
knappen. Den sidste linje angiver at funktionen ``buttonA_onPress``
skal kaldes når man klikker på knappen.

Prøv at køre programmet og tryk på knappen.

I stedet for bare at skrive ``Hello`` på skærmen, kan vi prøve at ændre
en variabel og tælle hvor mange gange der er trykket på knappen.

Prøv at erstat ``def knapAPressed():`` med følgende kode::

  count = 0

  def knapAPressed():
    global count
    count = count + 1
    print(count)

Her opretter vi først en tællervariabel ``count``, som starter
ved 0. Derefter gør vi så hver gang man trykker på knap A, lægges
der én til den variabel og værdien vises med ``print(count)``.

Linjen ``global count`` giver skriverettigheder til variablen ``count``,
ellers ville vi kun kunne læse værdien ``count`` inde i funktionen, men
ikke ændre den.

.. _indbygget_led:

Tænd/sluk indbygget LED
-----------------------
I det ene hjørne har din M5StickC en indbygget LED-lampe man kan tænde
og slukke. For at tænde den kan du skrive følgende:

   from m5stack import M5Led
   M5Led.on()

.. figure:: illustrationer/led.svg
   :alt: LED tændt
   :width: 500px

Sluk for LED'en ved at ændre i koden så der står::

   M5Led.off()

Et simpelt program der blinker to gange med LED'en kan skrives sådan
her::

  from m5stack import M5Led
  import time

  M5Led.on()
  time.sleep_ms(500)
  M5Led.off()
  time.sleep_ms(500)
  M5Led.on()
  time.sleep_ms(500)
  M5Led.off()
  time.sleep_ms(500)

