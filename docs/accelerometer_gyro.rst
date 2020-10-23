Accelerometer & Gyroskop
========================

Grundlæggende
-------------


M5stickC indeholder en bevægelsessensor, (SH200Q/MPU6886), der består af et accelerometer og et gyroskop.  En bevægelsessensor af denne type kaldes en IMU - inertial measurement unit. 

.. image:: illustrationer/6degreeaxis.svg



Accelerometer
^^^^^^^^^^^^^
Accelerometeret registrerer kræften hvormed M5stick bevæges i retning frem/tilbage/op/ned langs en akse. 
Man kan tænke på en fjerner der kan trækkes ud - høj accelerationskræft - og så efterfølgnede tilbage til en normal - ingen accelerationskræft. Accelrometeret kan altså ikke direkte bruges til at måle en placering, men derimod kræften bag en bevægelse. Accelrometeret kan i sig selv anvendes til f.eks. at registrere ryst.  

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






