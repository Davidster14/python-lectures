# Lösung der Ratezahl Spiel aufgabe (bitte noch vergleichen)

import random

def ratezahl():
    # Erzeuge eine zufällige Zahl zwischen 1 und 100
    zufallszahl = random.randint(1, 100)
    versuche = 0  # Zähler für die Anzahl der Versuche

    # Schleife zum Raten der Zahl
    while True:
        # Benutzereingabe
        benutzereingabe = input("Bitte raten Sie eine Zahl zwischen 1 und 100: ")
        try:
            geratene_zahl = int(benutzereingabe)
            versuche += 1  # Erhöhe den Zähler für die Versuche
            
            # Vergleiche die geratene Zahl mit der Zufallszahl
            if geratene_zahl < zufallszahl:
                print("Zu niedrig! Versuchen Sie es noch einmal.")
            elif geratene_zahl > zufallszahl:
                print("Zu hoch! Versuchen Sie es noch einmal.")
            else:
                print(f"Herzlichen Glückwunsch! Sie haben die Zahl {zufallszahl} nach {versuche} Versuchen erraten.")
                break
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein.")

# Beispielhafte Nutzung der Funktion
ratezahl()