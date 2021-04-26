
.. |FILES| image:: illustrationer/mubilleder/files.jpg
   :height: 20
   :width: 20


Biblioteker
===========

Biblioteker er en smart måde at gemme og gøre brug af funktioner der kan bruges i mange sammenhænge. Du kan skrive dine egen biblioteker eller du kan hente og brug biblioteker andre har brugt. 

Man kan finde mange forskellige biblioteker, der dækker mange forskellige behov.

Find bibliotek
--------------

Til M5stickC er der skrevet et bibliotek der hedder ``fusion.py`` der blandt andet gør det lettere at bruge den indbyggede bevægelsessensor.

For at gøre brug af fusion-biblioteket skal ``fusion.py`` først overføres fra internettet til din computer.
Du finder den her:

https://raw.githubusercontent.com/DatalogiForAlle/M5Guide/master/lib/fusion.py

Du gemmer ``fusion.py`` ved at klikke på linket og derefter trykke **ctrl** + **s** / **command** + **s**. 
Sørg for at gemme ``fusion.py`` samme sted som du gemmer den kode du arbejder med. 
Alternativt kan du copy-paste alt koden ind i en ny fil i Mu-editoren og så gemme den under navnet fusion.py.

.. todo:: afsnit i bunden af siden, hvor de forskellige funktioner i fusion.py forklares?  

Overfør bibliotek
-----------------

For at overføre et bibliotek fra computeren til M5Stick, skal man klikke på Files |FILES| i mu-editoren (husk at lukke REPL og Plotter) og trække den ønskede fil over fra \"Files on your computer:\" over til \"Files on your devise:\". 

Det der plejer at drille her, er at den fil du gerne vil have over på M5StickC ikke ligger i listen med \"Files on your computer:\". 

MU åbner kun den mappe som det kode du er ved at skrive ligger gemt i - så du skal altså sikre dig at din kode og den fil du gerne vil overføre ligger gemt samme sted på computeren. 

.. image:: illustrationer/comtilm5.gif

Importer bibliotek
-----------------

For at bruge biblioteket skal det importeres i den fil du vil bruge det i. 
Det gøres, med ``fusion.py`` som eksempel, ved at skive:: 

	import fusion

aller øverst i din kode.  


Du kan sagtens importere og bruge flere biblioteker på en gang. Bare skrive en linje for hvert af bibliotekerne og sørg for at det ligger øverst i din kode.   

Hvis du vil brug et bibliotek der hedder noget andet end fusion skal du skrive ``import *navnet_på_biblioteket*``. Det kræver også at du har hentet biblioteket og overført det til M5StickC, på samme måde som vi har vist med fusion-eksemplet.


