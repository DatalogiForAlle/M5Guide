.. |PLOT| image:: illustrationer/mubilleder/plotter.jpg
   :height: 20
   :width: 20

.. |RUN| image:: illustrationer/mubilleder/run.jpg
   :height: 20
   :width: 20

Accelerometer & Gyroskop
========================

Grundlæggende
-------------
M5StickC indeholder en bevægelsessensor, (SH200Q/MPU6886), der består
af et accelerometer og et gyroskop. Bevægelsessensoren kan fx bruges
til at måle:

 * hvor hurtigt man roterer (gyroskop)
 * hvor hurtigt man accelererer eller bremser (accelerometer)
 * tyngdekraften fra jorden, og dermed hvilken retning er nedad (accelerometer)

Bevægelsessensoren er derfor vigtig komponent i fx i biler til at
udløse airbags, i fly til styring. I mobiltelefoner og smart watches
bruges bevægelsessensoren fx til at finde ud af hvilken vej den
vender, eller til den indbyggede skridttæller.

En bevægelsessensor af denne type kaldes en IMU - *inertial
measurement unit*, og den IMU der er indbygget i M5StickC har 6 grader
af frihed.

.. figure:: illustrationer/6degreeaxis.svg
   :alt: 6 graders frihed, plus pitch, roll og yaw 
   :width: 300px


For at starte med at bruge bevægelsessensoren, skal imu-biblioteket importeres og objektet ``myIMU`` initieres::

	import imu
	
	myIMU = imu.IMU()

           
Accelerometer
^^^^^^^^^^^^^

Accelerometeret registrerer den acceleration hvormed M5StickC bevæges i
retning frem/tilbage eller op/ned langs en akse i tre dimensioner.

Man kan forestille sig at hver akse er forsynet med en lille fjeder
med en vægt, og så måler om fjederen bliver strakt eller trykket
sammen.

.. figure:: illustrationer/accel.svg
   :alt: acceleration langs x-, y-, z-aksen. 
   :width: 300px


Ved hjælp af ``myIMU.acceleration`` kan man hente de rå aflæsninger fra accelerometeret.:: 



   import imu
   import time
   
   myIMU = imu.IMU()

   while True:
   	time.sleep_ms(10)
    	print(myIMU.acceleration)



Klik på **Run** |RUN| og derefter **Plotter** |PLOT| i mu-editoren, for at få vist en graf. Bevæg M5stickC og se at dine bevægelse bliver registreret


.. image:: illustrationer/acc.gif

Hvis man skal bruge sensorens x y z målinger separeret, kan man gemme dem som enkeltstående variabler::

	ax, ay, az = myIMU.acceleration


Når man holder M5StickC stille med skærmen opad, så vil man kunne måle cirka ``(0.0, 0.0, 1.0)`` Det er tyngdekraften der påvirker z-aksen. Hvis M5StickC drejes som vist på illustrationerne, vil tyngdekræften påvirke henholdsvis x- og y-aksen.  

.. figure:: illustrationer/tyngdeAccel.svg
   :alt: acceleration langs x-, y-, z-aksen. 
   :width: 500px



.. Usikkert om nedenstående skal med og gemmes som kommentar ind til
   videre

   Tyngdekraften vil også påvirke accelerometeret, hvis "fjederen" er
   placeret i op/ned-aksen, men ikke hvis den ligger vandret.

   Enhver flytning af sensoren vil udløse ændringer, men kun mens
   sensoren får ændret sin hastighed - ikke hvis den bevæger sig med jævn
   hastighed eller ligger stille.  Accelerometeret kan altså ikke direkte
   bruges til at måle en placering, men afslører derimod kraften bag en
   bevægelse. Accelerometeret kan i sig selv anvendes til f.eks. at
   registrere ryst.



Gyroskop
^^^^^^^^
Gyroskopet registrerer rotationshastighed omkring en
akse. Rotationshastigheden måles i antal grader per sekund.

.. figure:: illustrationer/gyro.svg
   :alt: Gyroskop, drejning x-, y-, z-aksen. 
   :width: 190px

Ved at bruge ``myIMU.gyro`` kan man få vist de rå gyroskop data::
	
	import imu
	import time

	myIMU = imu.IMU()

	while True:
    		time.sleep_ms(10)
    		print(myIMU.gyro)
           

Hvis man skal bruge sensorens x y z målinger separeret, kan man gemme dem som enkeltstående variabler::

	gx, gy, gz = myIMU.gyro

Hvis vi for eksempel starter med at holde M5StickC helt stille, så er
Gyroskop aflæsningen ``(0, 0, 0)``, da den ikke roteres. Roterer vi
den langsomt rundt om x aksen, fx med 30 grader hvert sekund, så vil
Gyroskop-aflæsningen give ``(30, 0, 0)``.



EKSEMPEL: Registrer bevægelse
-----------------------------

Som illustration på hvordan accelerometeret kan bruges er her eksemplekode:: 

	import imu
	import time
	from m5stack import lcd

	myIMU = imu.IMU()

	def detectAccel(accel, threshold):
       		if abs(accel) > threshold: detectAcceleration = True
		else: detectAcceleration = False
       		return detectAcceleration

	while True:
       		time.sleep_ms(10)
        	print((myIMU.acceleration))
        	if detectAccel(myIMU.acceleration[0], 50):
            		lcd.clear(0xFF0000)
            		time.sleep_ms(1200)
        	if detectAccel(myIMU.acceleration[1], 50):
            		lcd.clear(0x00FF00)
            		time.sleep_ms(1200)
        	if detectAccel(myIMU.acceleration[2], 50):
            		lcd.clear(0x0000FF)
            		time.sleep_ms(1200)
        	else: lcd.clear(0x000000)






