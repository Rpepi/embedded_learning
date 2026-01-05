import serial, time

try: 
    ser = serial.Serial('COM3', 115200, timeout=10)
    print("connexion réussie")

except:
    print("Erreur: connexion impossible")
    exit()

time.sleep(2)


while True:
    choix = input("Tape R(rouge), G(verte), Q(quitter): ").upper()

    if choix == 'Q':
        break

    ser.write(choix.encode())
    print(f"ordre {choix} envoyer!")

ser.close()

