WiFi
====

Det er nemt at forbinde en M5StickC til et wifi netværk.

For at forbinde, skal vi først importere modulet ``wifiCfg`` øverst i vores fil::

  import wifiCfg

Derefter kan I forbinde til et wifi hotspot ved at angive dets navn og
password::
  wifiCfg.doConnect("MitWifiNet", "wifipassword")


.. function:: wifiCfg.doConnect(essid, password)

   Forbind til wifi-netværket med navnet `essid` og passwordet `password`.
              
   :param essid: Tekststreng: navnet på det WiFi-hotspot du vil forbinde til (fx ``"eduroam"``)
   :param password: Tekststreng: passwordet til WiFi netværket
