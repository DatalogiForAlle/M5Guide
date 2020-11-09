Hvilken retning peger M5StickC?
-------------------------------
Kan vi bruge accelerometer og gyroskop til f.eks. at afgøre om skærmen
vender på højkant (portræt) eller langs (landskab) og bruge det til at
rotere skærmen? Eller kan vi bruge det til at se om skærmen vender
nedad.

Bevægelsessensoren og dens accelerometer og gyroskop fortæller hvordan
bevægelse og rotation ændrer sig. Hvor meget roterer den? Hvor hurtigt
falder den mod jorden?

Hvis vi vil bevsare de andre spørgsmål, om hvordan M5StickC vender,
skal vi omregne de *rå* accelerometer og gyroskop sensorværdier
vinkler, der fortæller os noget om M5StickC's vinkel
ift. jordoverfladen.

Disse vinkler kaldes *pitch*, *roll* og *yaw*, og kan illustreres med
en flyvemaskine:

Pitch, roll, yaw
^^^^^^^^^^^^^^^^
Et flys placering i luften beskrives ved følgende tre vinkler:

 * Pitch: Peger spidsen af flyet op eller ned?
 * Roll: Hvor meget roterer flyet?
 * Yaw: Kompasretning ift. jorden (M5StickC har dog ikke et kompas)

.. raw:: html

  <video preload="auto" autoplay="autoplay" loop="loop" style="width: 200px; height: 200px;">
    <source src="_static/pitch_animation.mp4" type="video/mp4"></source>
  </video>
  <video preload="auto" autoplay="autoplay" loop="loop" style="width: 200px; height: 200px;">
    <source src="_static/roll_animation.mp4" type="video/mp4"></source>
  </video>
  <video preload="auto" autoplay="autoplay" loop="loop" style="width: 200px; height: 200px;">
    <source src="_static/yaw_animation.mp4" type="video/mp4"></source>
  </video>

Hvordan beregner man `pitch` og `roll` på M5StickC?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

På M5StickC kan vi ikke beregne `yaw`, da der ikke er et kompas, men
`pitch` og `roll` kan beregnes ud fra de *rå* accelerometer og
gyroskop værdier.

Når vores M5StickC står stille, ved vi for eksempel at accelerometeret
kan fortælle os hvilken vej tyngdekraften trækker, og dermed hvilken
vej M5StickC vender ift. jorden.

Når vi begynder at bevæge vores M5StickC, så kan vi dog ikke klare os
med accelerometeret, da det ikke længere kun er tyngdekraften der
påvirker accelerometeret. Derfor skal vi have gang i gyroskopet, som
er mere præcist i de små bevægelser, når de to kombineres kan vi få et
relativt præcist bud på vinklerne.

.. code-block::

  Rå accelerometer data --.
                           \
                            --- sensor fusion  ---> attitude
                           / 
  Rå gyroskop data -------.

Omregningen sker via en *sensor fusion* algoritme. Der findes flere
forskellige algoritmer, og vi kommer til at bruge en der kaldes et
*Mahony filter*. For at det virker, skal algoritmen hele tiden
opdateres med de nyeste værdier fra accelerometeret og gyroskopet.

Først overføres filen ``fusion.py`` fra din computer til M5StickC:

TODO


Tjek at det virker ved at importere biblioteket::

  import fusion

Nu kan vi konstruere et *filter*-objekt, der kan udføre omregningen::

  filter = fusion.MahonyFilter()

Det fungerer ved at man jævnligt i sit program kalder::

  filter.update(myIMU.acceleration, myIMU.gyro)

Kommandoen `filter.update` opdaterer filterets viden om hvilken vej
M5StickC peger, og efter vi har kaldt den kan `pitch` og `roll`
aflæses::

  print(filter.pitch, filter.roll)
  

Samlet eksempel
^^^^^^^^^^^^^^^
Her er et større eksempel, hvor vi hele tiden holder filteret
opdateret, og en gang i mellem viser vi vinklerne på skærmen (hver tyvende gang)::

  import imu
  import time
  import fusion
  from m5stack import lcd

  myIMU = imu.IMU()
  filter = fusion.MahonyFilter()

  count = 0
  lcd.clear()

  while True:
      filter.update(myIMU.acceleration, myIMU.gyro)

      if count == 20:
          lcd.print(filter.pitch, 20, 10)
          lcd.print(filter.roll, 20, 30)
          count = 0
      count += 1
