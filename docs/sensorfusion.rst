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

Attitude: Pitch, roll, yaw
^^^^^^^^^^^^^^^^^^^^^^^^^^

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

Hvordan beregner man attitude på M5StickC?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TODO
