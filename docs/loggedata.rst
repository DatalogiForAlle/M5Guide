.. |PLOT| image:: illustrationer/mubilleder/plotter.jpg
   :height: 20
   :width: 20

.. |RUN| image:: illustrationer/mubilleder/run.jpg
   :height: 20
   :width: 20

.. |FILES| image:: illustrationer/mubilleder/files.jpg
   :height: 20
   :width: 20

Gem/hent/overfør data
========================

Gemme data
----------

.txt fil
^^^^^^^^

For at gemme data laves først en fil, ved at kalde funktionen :func:`open` og give to argumenter. 
Det første argument er det ønskede navn på filen, det næste er \'w\' fordi vi ønsker at kunne skrive i filen (w for write)::

	fil = open('data.txt', 'w')

Dernæst fortæller man hvad der ønsker skrevet i filen med funktionen :func:`fil.write`::
	
	fil.write('Her kan du skrive tekst - husk citationstegn!') 

Tilsidst lukkes filen med :func:`f.close`::
	
	fil.close()


.csv fil
^^^^^^^^

På tilsvarende måde kan man lave en .csv fil. Her kan man bruge semikolon som skifter til næste søjle, mens \'\\n\' (newline) skifter til næste række::

	fil = open('data.csv', 'w')
	fil.write(';søjle1;søjle2;søjle3\n' +
         	  'række1;1;2;3\n' +
         	  'række2;4;5;6\n' +
        	  'række3;7;8;9\n')
	fil.close()

Man skal dog holde tungen lige i munden her - der er en masse tilfælde hvor denne metode vil give et dårligt resultat - og pas på med mellemrum. Python har et indbygget bibliotek til at håndtere csv-filer, med det er desværre ikke med som standart på M5stickC. 
Man kan også importere en .txt fil til de fleste regneark, men hvis man ikke skal lave for meget manuel oprydning, er det en fordel at tænke i de baner som beskrevet herover. 


Hente data
----------

Hvis man vil se indholdet af en fil klan det gøres ved at åbne den i læsetilstand med :func:`open` og give \'r\' (r for read) som 2. argument. Dernæst kan funktionen :func:`fil.read` bruges, f.eks sammen med printfunktionen::

	fil = open('data.txt', 'r')
	print(fil.read())
	fil.close()




Fra M5stickC til computer
-------------------------
Med :func:`open` og :func:`fil.write` bliver dokumentet gemt lokalt på M5stick'en. For at få den over på computeren, kan man klikke på Files |FILES| i mu-editoren (husk at lukke REPL og Plotter) og trække den ønskede fil over til \"Files on your computer\". Filen ligger nu samme sted som den mu-fil du arbejder i er gemt.  

.. image:: illustrationer/movefile.gif


Fra computer til M5stickC
-------------------------
.. todo:: skriv afsnit om overførsel af filer fra computer - find på et eksempel på brug/relevans


EKSEMPEL: Gemme IMU data i .csv format
--------------------------------------

For at få gemt målinger fra bevægelsessensoren kan følgende kode benyttes::

	import imu
	import time

	myIMU = imu.IMU()
	fil = open('imudata.csv', 'w')
	fil.write(';accelerometer_x;accelerometer_y;accelerometer_z;' +
          	'gyroskop_x;gyroskop_x;gyroskop_x\n')

	for i in range(10):	
		time.sleep_ms(600)
  	 	dataline = myIMU.acceleration + myIMU.gyro
  	  	print(dataline)
   	 	fil.write(str(i) + '; ')
  	  	for j in range(len(dataline)):
      	  		fil.write(str(dataline[j]) + '; ')
   	 	fil.write('\n')    
	fil.close() 


Nu kan man trække filen over til computeren og åbne den. 
Tjek at tallene er som de skal være - juster i Import Setting, hvis det ser forkert ud. 
Som delimiter/Value Separator skal semikolon bruges (fordi det er den vi bruger i koden) \';\'. 
Som Decimal Separator skal punktum \'.\' bruges. 
Der er basis for at kludre rigtig meget rundt i tallene - så se dig godt for.    

.. figure:: illustrationer/importsettings.png
   :alt: gyroskop, drejning x-, y-, z-aksen. 
   :width: 300px







