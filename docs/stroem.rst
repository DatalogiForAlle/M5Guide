Strøm og batteri
================

.. todo:: lav målinger af batteri-levetid: med skærmen slukket, med
          skærmen tændt med hvid i alle pixels, med skærmen slukket og
          WiFi tændt (hent noget data hvert 30. sekund)

.. todo:: skriv dokumentation af alle nedenstående

.. function:: axp.getChargeState()

   :rtype: boolean

   Returnerer ``True`` hvis enheden er sluttet til strøm og oplader,
   ellers returneres ``False``.



.. function:: axp.getBatVoltage()

   :rtype: float


.. function:: axp.getBatCurrent()

   :rtype: float



Juster skærmens lysstyrke
-------------------------
``axp.setLcdBrightness(30)``

Tips til at spare strøm
-----------------------
 .. todo:: skriv sektion

 * Begræns brug af WiFi
 * Skru ned for skærmens lysniveau
 * Brug mørke farver på skærmen
