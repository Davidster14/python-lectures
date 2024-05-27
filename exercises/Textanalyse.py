# def text_eingabe():
#     text = input("please enter a sentence with min 12 words: ")
#     return text


# def wortzaehlung(text):
#     worte = text.split()
#     return len(worte)


def text_eingeben():
   
    text = input("please enter a sentence with min 10 words: ")
    return text

#zählen der woerter
def wortzaehlung(text):
  
    worte = text.split()
    return len(worte)


# wie oft kommt ein wort in dem text vor?
def wort_haeufigkeit(text):
    
    worte = text.split()
    haeufigkeit = {}
    
    for wort in worte:
        wort = wort.lower()  # Optionale Normalisierung auf Kleinbuchstaben
        if wort in haeufigkeit:
            haeufigkeit[wort] += 1
        else:
            haeufigkeit[wort] = 1
            
    return haeufigkeit


# main function (?)
def main():
    text = text_eingeben()
    anzahl_woerter = wortzaehlung(text)
    print(f"your sentence includes  {anzahl_woerter} words.")
    haeufigkeit = wort_haeufigkeit(text)
    print("word frequency:")
    for wort, freq in haeufigkeit.items():
        print(f"{wort}: {freq}")

# Ausfuehrung der main function
if __name__ == "__main__":
    main()