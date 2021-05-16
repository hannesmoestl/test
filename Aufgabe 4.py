
woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsch"]
print(len(woerterbuch_deutsch))
woerterbuch_english = ["apple", "pear", "cherry", "melon", "apricot", "peach"]
Wort = input("gibt ein Wort ein welches du übersetzten wilst: ")

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
    