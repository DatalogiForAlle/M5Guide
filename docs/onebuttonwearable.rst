Tutorial: One Button Wearable til patienter med PTSD
====================================================

.. figure:: illustrationer/onebuttonwearable_paper.png
   :class: shadow float-right
   :alt: LED tændt
   :width: 200px

Patienter med posttraumatisk stress, f.eks. fra oplevelser ved krig,
kan få alvorlige traumer og nervesystemet kan have svært ved at falde
til ro. De kan bl.a. opleve anfald af *hyperarousal*. Det kan være
svært at forudsige hvornår anfaldene opstår, og om anfaldene har
sammenhæng med andet de foretager sig.

I denne tutorial viser vi hvordan man kan lave en simpel lille
wearable vedhjælp af M5StickC, som PTSD patienter kan bruge til at
registrere deres anfald. Idéen stammer fra artiklen "Active
Self-Tracking of Subjective Experience with a One-Button Wearable: A
Case Study in Military PTSD" af Larsen, Eskelund og Christiansen.
https://arxiv.org/abs/1703.03437

En sådan wearable kan også bruges til registrere andre begivenheder
(træthed, overspringshandlinger, negative tanker, stress-symptomer
osv.).

Vi forudsætter at du har installeret Mu editoren og er gået igennem
vores :doc:`komigang` guide.

Overordnet plan
---------------
Idéen med projektet er at patienten eller brugeren har et armbåndsur
med en enkelt knap, og hver gang de oplever symptomer på et anfald, så
klikker de på knappen.

Når de klikker på knappen, gemmes tidspunktet for knaptrykket i en
fil, som vi senere kan indlæse i fx Excel. For at gøre det har vi brug
for at kunne tre ting:

1. registrere knaptryk
2. registrere tidspunktet
3. skrive til en fil

Første skridt
-------------
For at komme i gang med at bruge knapperne og registrere tidspunkt,
skal du først se på disse to sider:

- :doc:`knapper`
- :doc:`tid`

Når du har fået arbejdet både med knappen, og hvordan man bruger det
indbyggede ur, så prøv at lave den følgende opgave, hvor du skal
kombinere hvad du har lært til ét samlet projekt.
  
**Opgave:** Gør så tidspunktet printes i konsollen, når man klikker på
knappen.

**NB:** Husk at gemme projektet, kald det fx ``onebuttonwearable.py``

Gemme hvert knaptryk i en fil
-----------------------------
Nu burde din wearable både kunne registrere knaptryk og
tidspunktet. Det næste skridt er så at skrive tidspunkterne til en
fil.

Det vi har tænkt os er at lave en fil med en linje for hver tidspunkt
der er trykket på knappen. Fx kunne det se sådan ud::

  time
  10:48:56
  10:48:57
  15:24:58
  15:24:59
  15:32:59
  15:33:00
  15:33:00
  15:34:48
  15:34:48
  15:34:49
  15:34:50
  16:07:51
  16:07:51
  18:10:52
  18:10:52

Dette er en såkaldt CSV-fil, hvor CSV står for comma-separated values
og som kan åbnes af fx Excel. CSV-filer kan normalt have flere
kolonner adskilt af komma eller semikolon, men i det her simple
program tager vi kun klokkeslættet (det er en opgave til læseren også
at gemme datoen).

Når vi vil skrive en linje tekst i slutningen af en fil i Python, kan
det gøres med følgende linjer::

    timestring = "15:32:59"          # det vi gerne vil skrive
    file = open("data.csv", "a")  # åbn filen
    file.write(timestring + "\n")    # skriv teksten + et linjeskift
    file.close()                     # luk filen
    
**Opgave:** Tast ovenstående ind i dit, sådan at der skrives
``"der er blevet trykket på knappen"`` til filen, hver gang man trykker på knappen.

For at kunne bruge det tidspunkt i har indlæst tidligere, og skrive
det til filen, skal vores ``timestring`` sættes til::

  timestring = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)

Overføre filen til computeren
-----------------------------

Filen skrives til M5StickC's interne filsystem. For at få den over på
din computer, kan man klikke på 'Files' i Mu-editoren (luk REPL og
Plotter først). Derefter kan filen overføres via drag-and-drop:

.. image:: illustrationer/movefile.gif

Filen ligger nu i samme mappe som den Python-fil du har åben i Mu. Den
kan nu åbnes som regneark og analyseres i fx Excel.

Afprøvning
----------
Det er nok ikke alle der kender en med PTSD, der vil kunne afprøve din
wearable.

Prøv i stedet at registrere hver gang du kommer til at
overspringshandle, mens du burde lave noget fokuseret arbejde. Eller
prøv at registrere hver gang du åbner ``facebook.com`` eller en anden
hjemmeside du måske tjekker lidt for ofte.

Prøv at åbne .csv-filen i Excel, og se om du kan lave et plot over
tidspunkterne. Hvornår på dagen laver du flest overspringshandlinger?

Videre
------

 - Lær om hvordan man bruger skærmen på siden :doc:`tegne` Gør fx så
   hver gang man trykker på knappen, så bliver der vist en grøn prik,
   eller anden figur som indikation af at knaptrykket blev registreret
   korrekt.

 - Lær om hvordan man kobler M5StickC på et WiFi-netværk og logger
   data til Airtable.com på siden :doc:`wifi`. Log hvert knaptryk til en
   Airtable database. Bemærk: WiFi bruger meget strøm, så dit ur vil
   meget hurtigt løbe tør for strøm, hvis det er på batteri.

Hele koden til projektet
------------------------

.. code-block:: python

  from m5stack import btnA
  from m5stack import rtc
  import os

  # Sæt tidspunkt, læs evt. siden "Tid og dato", for at se hvordan
  # du finder tidspunktet via internettet
  rtc.setTime(2020, 10, 23, 15, 48, 52)

  filename = "data.csv"

  # Opret filen, hvis den ikke findes
  if filename not in os.listdir():
      print("File {} doesn't exist, creating.".format(filename))
      file = open("data.csv", "w")
      file.write("date;time\n")
      file.close()

  def knapAPressed():
    # Hvad er klokken?
    year, month, day, hour, minute, second = rtc.now()

    # Formater tidspunktet i et standard format
    timestring = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
    print(timestring)

    # Skriv tidspunktet til .csv filen
    file = open("data.csv", "a")
    file.write(timestring + "\n")
    file.close()

  btnA.wasPressed(knapAPressed)


..
   Disposition til denne side
   --------------------------

    - Registrer knaptryk

    - Gem tidspunkt i .csv-fil (eller Airtable) hver gang der trykkes

    - Vis hvordan .csv fil overføres til computeren

    - Evt. vis klokken på skærmen, så det også bare kan bruges som
      armbåndsur (se evt. skærmen, om der er andet interessant vi kan vise)

    - Evt. kan vi finde på nogle nogle opgaver? Så det ikke kun er
      "indtast efter os"...
