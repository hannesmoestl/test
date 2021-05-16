#Erweitern sie das Wörterbuch beispiel um die möglichkeit, Einträge zu ergänzen bzw. zu löschen

woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsch"]
print(len(woerterbuch_deutsch))
woerterbuch_english = ["apple", "pear", "cherry", "melon", "apricot", "peach"]
Wort = input("gibt ein Wort ein welches du übersetzten wilst: ")
auswahl = input("Befehl? [e]infügen, [L]öschen, [A]bfragen: ")

if auswahl == 'E' or auswahl == 'e':
    Wort = input("Welches Wort möchten Sie hinzufügen: ")
    woerterbuch_deutsch.append(Wort)
    print(woerterbuch_deutsch)
    
elif auswahl == 'L' or auswahl == 'l':
    Wort = input("Welches Wort möchten Sie entfernen? ")
    woerterbuch_deutsch.remove(Wort)
    print(woerterbuch_deutsch)
else:
        
    Index_Wort = 0
    while Index_Wort < len(woerterbuch_deutsch):
        if Wort.lower() == woerterbuch_deutsch[Index_Wort].lower():
            Ergebnis = Index_Wort
            print("Übersetzung ist: ", woerterbuch_english[Ergebnis] )
            break
           
        if Wort.lower() == woerterbuch_english[Index_Wort].lower():
            Ergebnis = Index_Wort
            print("Übersetzung ist: ", woerterbuch_deutsch[Ergebnis] )
            break
        Index_Wort +=1
    