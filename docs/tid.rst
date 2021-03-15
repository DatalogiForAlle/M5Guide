.. _tid_og_dato:

Tid og dato
===========
M5StickC har et indbygget ur, men det holder kun så længe der er strøm
på batteriet.

Indstille uret
--------------

For at indstille uret kan man kalde funktionen :func:`rtc.setTime`,
først skal vi dog importere objektet `rtc` som står for *real time
clock*::

  from m5stack import rtc

Nu kan vi indstille uret ved at kalde::

  rtc.setTime(2020, 10, 23, 15, 48, 52)

Nu er uret indstillet til kl. 15:48:42, 23. oktober 2020. Bemærk, uret
holder kun så længe der er strøm og den skifter ikke selv mellem
sommertid/vintertid.


Hvad er klokken?
----------------

Når vi har brug for at vide hvad klokken er, kan vi spørge med:

>>> rtc.now()
(2020, 10, 23, 15, 56, 39)

Hvis du skal bruge det i dit program, vil du sikkert gemme værdierne i
variabler::

    year, month, day, hour, minute, second = rtc.now()
    lcd.text(10, 10, "{}:{}:{}".format(hour, minute, second))

Indstille tiden via tidsserver
------------------------------
Vi kan også indstille uret via en tidsserver. Rundt i verden står der
en masse servere, hvis eneste opgave er at holde styr på hvad klokken
er og besvare når forskellige computere skal indstille deres ur. For
eksempel har de danske universiteter en fælles server der hedder
`ntp.forskningsnettet.dk` (man kan ikke tilgå den via en browser).

For at indstille uret via en tidsserver, skal vi bruge et ekstra
modul `m5ntp.py`, der ikke følger med en M5StickC.

Download filen `m5ntp.py` og gem den på jeres computer:
https://raw.githubusercontent.com/DatalogiForAlle/M5Guide/master/lib/m5ntp.py

Åbn filen i Mu-editor og overfør den til din M5StickC. Se hvordan her: :ref:`comtilM5`

Når I har overført filen til jeres M5StickC, kan I importere den via::

  import m5ntp

For at hente tiden, skal I først forbinde jeres enhed til WiFi::

  import wifiCfg
  wifiCfg.doConnect("jeres_wifi_netvaerk", "wifi_password_her")

Derefter kan I hente og indstille tiden via::

  m5ntp.settime(1)

Nu er tiden indstillet fra serveren, og I kan bruge :func:`rtc.now()`
som ovenfor.

  >>> rtc.now()
  (2020, 10, 23, 15, 59, 25)

Et simpelt armbåndsur
---------------------

.. code-block:: python

    import wifiCfg
    import time
    import m5ntp

    # Log på WiFi
    wifiCfg.doConnect("DIKU1", "PeterNaur")

    # Indstil uret fra tidsserver
    m5ntp.settime(1)

    # Vis klokken på skærmen
    lcd.clear()
    while True:
        year, month, day, hour, minute, second = rtc.now()
        lcd.text(10, 10, "{}:{}:{}".format(hour, minute, second))
        time.sleep(1)
