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

while True:
    if btnA.wasPressed():
        # Hvad er klokken?
        year, month, day, hour, minute, second = rtc.now()

        # Formater tidspunktet i et standard format
        timestring = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
        print(timestring)

        # Skriv tidspunktet til .csv filen
        file = open("data.csv", "a")
        file.write(timestring + "\n")
        file.close()
