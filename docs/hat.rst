Højtaler
========

Grundlæggende
-------------

..todo:: skrive tekst


EKSEMPEL: Registrer bevægelse med lyd
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Afspilning af tone når armen løftes korrekt::

	from lib import imu 
	from m5stack import lcd 
	# Importer bibliotek til at arbejde med højttaler
	from flowlib import hat
	import time 

	myIMU = imu.IMU() 

	ax, ay, az = myIMU.acceleration 
	ay_sidst = ay 
	hastighed = 0.025 

	hat_spk0 = hat.get(hat.SPEAKER)
	tone = 1500

	while True: 
		ax, ay, az = myIMU.acceleration 
		if ay > ay_sidst: 
			#For at få lyd ud af højtaleren beder vi den om at "synge"
			hat_spk0.sing(tone, 0.33)
			#Tone bliver højere, jo længere tid vi laver den rigtige bevægelse
			tone += 100
			#denne linje sætter en baggrundsfarve på M5StickC
			lcd.clear(0x75ad0a)

		else: 
			#her sætter vi tone tilbage til udgangspunktet
			tone = 1500
			#denne linje sætter en baggrundsfarve på M5StickC
			lcd.clear(0xffff99)

		ay_sidst = ay+hastighed 
		time.sleep_ms(300)


