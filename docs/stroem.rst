Strøm og batteri
================
M5StickC kommer med sit eget lille batteri (95mAH), der kan holde den
i live i et par timer. Hvis man har behov for at den skal holde
længere, kan man:

 - Tilslutte den til en powerbank via USB-C kablet
 - Tilslutte den til en almindelig USB-oplader i stikkontakten
 - prøve at optimere sit program, så det bruger mindre strøm. Se
   nogle tips nedenfor.


Tips til at spare strøm
-----------------------
.. todo:: skriv sektion


* Begræns brug af WiFi
* Skru ned for skærmens lysniveau ``axp.setLcdBrightness(50)``
* Brug mørke farver på skærmen
          
.. todo:: lav målinger af batteri-levetid: med skærmen slukket, med
          skærmen tændt med hvid i alle pixels, med skærmen slukket og
          WiFi tændt (hent noget data hvert 30. sekund)


          
Tjek om den oplader
-------------------
Hvis I vil vise på skærmen om jeres M5StickC er ved at lade op, eller
måske vil du lave et program der deaktiverer nogle funktioner, hvis
den kører på batteri.

For at finde ud af om den kører på batteri, eller den er sluttet til
en anden strømkilde, kan I bruge funktionen ``axp.getChargeState()``

.. function:: axp.getChargeState()

   :rtype: boolean

   Returnerer ``True`` hvis enheden er sluttet til strøm og oplader,
   ellers returneres ``False``.


Sluk M5StickC fra dit program
-----------------------------
Man slukker sin M5StickC ved at holde tænd/sluk knappen nede i 6
sekunder. Hvis man vil slukke automatisk som del af sit program, kan
man kalde funktionen ``axp.powerOff()``

.. function:: axp.powerOff()

   Slukker din M5StickC.

.. Disse funktioner er ikke rigtig brugbare, har jeg fundet ud af

   Jeg tror ikke man pt. kan aflæse hvor meget strøm der er tilbage på
   batteriet

   .. function:: axp.getBatVoltage()

      :rtype: float

   .. function:: axp.getBatCurrent()

      :rtype: float
