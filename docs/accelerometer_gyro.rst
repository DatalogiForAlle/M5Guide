Accelerometer & Gyroskop
========================

Grundlæggende
-------------


M5stickC indeholder en bevægelsessensor, (SH200Q/MPU6886), der består af et accelerometer og et gyroskop.  En bevægelsessensor af denne type kaldes en IMU - inertial measurement unit. Og denne konkrete IMU har 6 grader af frihed. 

.. image:: illustrationer/6degreeaxis.svg



Accelerometer
^^^^^^^^^^^^^
Accelerometeret registrerer den acceleration hvormed M5stick bevæges i retning frem/tilbage/op/ned langs en akse. Man kan forestille sig at hver akse er forsynet med en lille fjeder med en vægt, og så måler om fjederen bliver strakt eller trykket sammen. Tyngdekraften vil også påvirke accelerometeret, hvis "fjederen" er placeret i op/ned-aksen, men ikke hvis den ligger vandret. Enhver flytning af sensoren vil udløse ændringer, men kun mens sensoren får ændret sin hastighed - ikke hvis den bevæger sig med jævn hastighed eller ligger stille.
Accelerometeret kan altså ikke direkte bruges til at måle en placering, men afslører derimod kraften bag en bevægelse. Accelerometeret kan i sig selv anvendes til f.eks. at registrere ryst.  

.. image:: illustrationer/accel.svg


Gyroskop
^^^^^^^^
Gyroskopet registrerer rotation omkring en akse. 

.. image:: illustrationer/gyro.svg



Dataudtræk
----------

For at starte med at bruge bevægelsessensoren, skal imu-biblioteket importeres og objektet ``myIMU`` initieres::

	import imu
	
	myIMU = imu.IMU()

Nu kan man ved hjælp af ``myIMU.acceleration`` hente de rå aflæsninger fra accelerometeret. Klik **Plotter** i mu-editoren, for at få vist en graf. Bevæg M5stickC og se at dine bevægelse bliver registreret::
	
	import imu
	import time

	myIMU = imu.IMU()

	while True:
    		time.sleep_ms(10)
    		print(myIMU.acceleration)



.. image:: illustrationer/acc.gif

På tilsvarende måde kan man hente gyroskopmålingerne ved at bruge ``myIMU.gyro``

x,y,z 
^^^^^

Hvis man skal bruge sensorens x y z målinger separeret, kan man gemme dem som enkeltstående variabler::

	ax, ay, az = myIMU.acceleration
	gx, gy, gz = myIMU.gyro


Registrer bevægelse
-------------------

Som illustration på hvordan accelerometeret kan bruges er her eksemplekode:: 

	import imu
	import time
	import lcd

	myIMU = imu.IMU()

	def detectShake(accel, threshold):
    		x, y, z = accel
    		if abs(x) > threshold and abs(y) > threshold and abs(z) > threshold:
      			shake = True
    		else:
       			shake = False
   		return shake

	while True:
    		time.sleep_ms(10)
		if detectShake(myIMU.acceleration, 50):
    			lcd.clear(0xFF0000)
		else: lcd.clear(0x00FF00)
 

Gemme data
----------

.csv fil
^^^^^^^^






