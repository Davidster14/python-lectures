# normale funktion

def hello():
    print("hello world")

hello()

# LAMBDA Funktion  (anonyme Funktion... )
# add_ten = lambda a: a + 10


# print(add_ten(7))  

# add_ten = lambda a: a + 10 #  zB
 
# print(add_ten(7))   # zB


# Beispiele zum rumprobieren

def call_function(func,a ,b):
    return func(a, b)

def multiply(x, y):
    return x * y

result = call_function(multiply, 5, 6)
print(result)


# def add_ten(x):
#     return x + 10

# üBUNGEN  DAZU 

# DEF 1 FUNC DIE 2 ZAHLEN MULTIPLIZIERT

def multiply(a, b):
    return a * b
print(multiply(3, 4))  

# def 1 lambda func die 1 zahl quadriert
quadrat_integer = lambda a: a * a

print(quadrat_integer(5)) 

# schreibe 1 funct die eine andere als Argument nimmt 

def argument_function(funktionsname):
    print("ruft die übergebene funktion auf")
    funktionsname()

def hallo():
    print("+ hallo welt\n")

argument_function(hallo)


# übe den Umgang mit Scope in function
 # learning by doing 


# Übung zu download 21.5.24  

                
#Lösung Zahlenraten
import random

def ratezahl():
    # Erzeuge eine zufällige Zahl zwischen 1 und 100
    zufallszahl = random.randint(1, 100)
    versuche =  0

    print(f"Zufallig generierte Zahl beträgt:" ,zufallszahl)   # zum schnellen erraten bei tests :)
    print("\n")

    # Schleife zum Raten der Zahl / Benutzereingabe
    while True:
                
        benutzereingabe = input("Bitte raten Sie eine ganze Zahl zwischen 1 und 100: ")
        try:            
            geratene_zahl = int(benutzereingabe)
            versuche += 1 # um die anzahl der Verscuhe anzuzeigen

            # Vergleiche die geratene Zahl mit der Zufallszahl
            if geratene_zahl < zufallszahl:
                print("Das war zu niedrig Versuchen Sie es noch einmal.")
            elif geratene_zahl > zufallszahl:
                print("Das war zu hoch Versuchen Sie es noch einmal.")
            else:
                print(f" Glückwunsch! Sie haben die richtige Zahl {zufallszahl}   in  {versuche} Versuchen  erraten!")
                break
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein.")

# integration einer func spiel die die anzahl der Versuche zählt 
#def versuche():
# 

# Aufruf der funktion
ratezahl()

