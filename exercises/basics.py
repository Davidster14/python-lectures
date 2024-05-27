'''
Schreibe je eine Funtion add, subtract, multiply, divide, die die
jeweilige Grundrechenart auf die beiden übergebenen Parameter A und B
anwendet.
'''
def add(a, b): 
    return a + b

def subtract(a, b):     
    return a - b

def multiply(a, b): 
    return a * b 

def divide(a, b): 
    return a / b 


print(add(12, 24))  


print(subtract(112, 44))  

print(multiply(77, 3))  


print(divide(99, 33))  

'''
Schreibe eine Funktion, die eine Temperatur in Celsius in eine Temperatur in
Fahrenheit umrechnet.
'''
def inFahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

#beispielberechnungen
print (inFahrenheit(28)) 
       
print (inFahrenheit(15))
    

'''
Schreibe eine Funktion, die eine Temperatur in Fahrenheit in eine Temperatur
in Celsius umrechnet.
'''
def inCelsius(fahrenheit):

    celsius = (fahrenheit - 32) * 5/9 
    return celsius


print (inCelsius(83)) 

print (inCelsius(60)) 
#Versuch        
#print(f"{inCelsius}(58) celsius")
    

'''
    :param fahrenheit: Temperature to convert in Fahrenheit
    :type fahrenheit: float

    :return: Converted temperature in Celsius
    :rtype: float

______________________________________________________________

Schreibe eine Funktion, die prüft, ob eine Zahl gerade ist.
'''
def ist_gerade(zahl):
    return zahl % 2 == 0


zahl = 22
if ist_gerade(zahl):
    print(f"{zahl} ist gerade.")
else:
    print(f"{zahl} ist ungerade.")

    '''
    :param num: Number to test
    :type num: int

    :rtype: bool
    '''
    

'''
Schreibe eine Funktion, die prüft, ob eine Zahl ungerade ist.
'''
def ist_ungerade(zahl):
    return zahl % 2 != 0


zahl = 43
if ist_ungerade(zahl):
    print(f"{zahl} ist ungerade.")
else:
    print(f"{zahl} ist gerade.")
    '''
    :param num: Number to test
    :type num: int

    :rtype: bool
    '''
    

# Kontrollfluss

# if

'''
Schreibe eine Funktion, die abhängig von dem als Zahl eingegebenen Monat die
passende Jahreszeit zurückgibt. Und zwar

"Frühling" für die Monate März, April, Mai
"Sommer" für die Monate Juni, Juli, August
"Herbst" für die Monate September, Oktober, November und
"Winter" für die Monate Dezember, Januar und Februar.
'''
def jahreszeit(monat):
    if monat in [3, 4, 5]:
        return "Frühling"
    elif monat in [6, 7, 8]:
        return "Sommer"
    elif monat in [9, 10, 11]:
        return "Herbst"
    elif monat in [12, 1, 2]:
        return "Winter"
    else:
        return "Ungültiger Monat bitte wähle zwischen 1 - 12 aus. "


monat = 42
print(f"Der {monat}. Monat  gehört zur Jahreszeit: {jahreszeit(monat)}")

'''
    :type monat: int
    :return: Jahreszeit
    :rtype: string
    '''
#____________________________________________________________________________

'''
Schreibe eine Funktion, die die Umsatzsteuer anhand des Umsatzes und des
Steuerjahres berechnet. Der Steuersatz beträgt 19%. Liegt der Umsatz unter
der Freigrenze von 17.500 EUR (für die Steuerjahre 2003-2019) bzw. 22.000 EUR
(für die Steuerjahre ab 2020) soll die Kleinunternehmerregelung angewendet
und keine Umsatzsteuer berechnet werden. Der Rückgabewert ist dann 0.
'''
#version 0.1 ->  Freigrenze beachten!
def umsatzsteuer(umsatz, steuerjahr):
    #  Freigrenzen sind
    if steuerjahr >= 2020:
        freigrenze = 22000
    else:
        freigrenze = 17500
    
    # Kleinunternehmerregelung möglich?
    if umsatz < freigrenze:
        return 0
    else:
        # Berechnung der Umsatzsteuer
        steuersatz = 0.19
        umsatzsteuer = umsatz * steuersatz
        return umsatzsteuer

# Umsatz und Steuerjahr  werden eingefügt 
umsatz = 26000
steuerjahr = 2007
umsatzsteuer = umsatzsteuer(umsatz, steuerjahr)
print(f"Die Umsatzsteuer bei einen Umsatz von {umsatz} EUR im Jahr {steuerjahr} beträgt: {umsatzsteuer:.2f} EURO")


'''
    :param umsatz: Umsatz im Steuerjahr
    :type umsatz: float
    :param steuerjahr: Steuerjahr
    :type steuerjahr: int

    :return: Umsatzsteuer
    :rtype: float
    '''
    

# match

'''
Schreibe eine Funktion, die den Flächeninhalt verschiedener geometrischer
Formen berechnet. Die Funktion soll zwei Argumente erhalten:
Den Namen der geometrischen Form (circle, triangle, rectangle), sowie die
dafür relevanten Parameter als ein Dictionary.
Für die Berechnung eines Kreises wird der Radius (radius) benötigt.
Für die Berechnung eines Dreieckes sowie eines Rechteckes werden die Länge
der Grundseite (base) sowie die Höhe (height) benötigt.

Beispiele für den `params` Parameter:

{ 'radius': 1.0 }
{ 'base': 2, 'height': 1 }

'''
import math

def area(form, parameter):
    if form == "circle":
        radius = parameter.get("radius")
        if radius is not None:
            return math.pi * radius**2
        else:
            return "Radius fehlt"
    elif form == "triangle":
        base = parameter.get("base")
        height = parameter.get("height")
        if base is not None and height is not None:
            return 0.5 * base * height
        else:
            return "Grundseite oder Höhe fehlt"
    elif form == "rectangle":
        base = parameter.get("base")
        height = parameter.get("height")
        if base is not None and height is not None:
            return base * height
        else:
            return "Grundseite oder Höhe fehlt"
    else:
        return "Unbekannte Form"


parameter_circle = {"radius": 1.0}
parameter_triangle = {"base": 12, "height": 14}
parameter_rectangle = {"base": 8, "height": 4}

flaecheninhalt_circle = area("circle", parameter_circle)
flaecheninhalt_triangle = area("triangle", parameter_triangle)
flaecheninhalt_rectangle = area("rectangle", parameter_rectangle)

print(f"Flächeninhalt des Kreises: {flaecheninhalt_circle:.2f}")
print(f"Flächeninhalt des Dreiecks: {flaecheninhalt_triangle:.2f}")
print(f"Flächeninhalt des Rechtecks: {flaecheninhalt_rectangle:.2f}")

'''
    :param shape: Shape
    :type shape: string
    :param params: Parameters of the shape
    :type params: dict

    :return: Area of the shape
    :rtype: float
    '''
   
    

# loops

'''
Schreibe eine Funktion, die alle Karten eines Kartenspiels jeweils mit ihrer
Farbe (Clubs, Spades, Hearts, Diamonds) und ihrem Wert (2 - 10, J, K, Q, A)
erzeugt.
Die Karten werden als Tupel bestehend aus Farbe und Wert dargestellt und alle
Karten in einer Liste gesammelt zurückgegeben.
'''
# def deckOfCards():
#     pass

def deckOfCards():
    farben = ["Clubs", "Spades", "Hearts", "Diamonds"]
    werte = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    
    kartenspiel = [(farbe, wert) for farbe in farben for wert in werte]
    return kartenspiel

# Beispielhafte Nutzung der Funktion
kartenspiel = deckOfCards()

# Ausgabe der Karten
for karte in kartenspiel:
    print(karte)


'''
Schreibe eine Funktion, die die ersten N Antworten für das FizzBuzz-Spiel
erzeugt und auf der Konsole ausgibt.

Siehe auch https://de.wikipedia.org/wiki/Fizz_buzz
'''
def fizzbuzz(x):
     for x in range(1, x + 1):
         if x % 3 == 0 and x % 5 == 0:
             print("FizzBuzz")
         elif x % 3 == 0:
             print("Fizz")
         elif x % 5 == 0:
             print("Buzz")
         else:
             print(x)

# # Aufruf  der Funktion
fizzbuzz(30)
    
# FIZZBUZZ funktioniert eigentlich wird in den test aber negativ angezeigt




# recursion

'''
Schreibe eine rekursive Funktion, die die N-te Fibonacci-Zahl berechnet.

Siehe auch https://de.wikipedia.org/wiki/Fibonacci-Folge
'''
def fibonacci(n):
    if n <= 0:
        raise ValueError("bitte eine positive ganze Zahl eingeben.")
    #elif n == 

    '''
    :type n: int
    
    :return: n-th Fibonacci number
    :rtype: int
    '''

    
