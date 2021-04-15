#Aufgabe 1
#schreiben sie ein thonny Programm
#1.) den Benutzer begrüßt
#2.)eine erste Zahl entgegen nimmt
#3.) eine zweite Zahl entgegenimmt
#4.) die Summe beider Zahlen entgegennimmt undgibt
#5.) die Differenz der kleineren Zahlen von der Größeren berechnet und ausgibt
#6.) das Produkt der beiden Zahlen ausgibt
#7.) den Quotient der beiden Zahlen berechnet und ausgibt (inkl. Nachkommastellen)



print("Hallo Benutzer") #Begrüßung

meine_zahl1_string = input("gib eine Zahl an:") #string wegen input
meine_zahl2_string = input("gib eine zweite Zahl an:") 
meine_zahl1 = float(meine_zahl1_string) # float wegen kommastellen
meine_zahl2 = float(meine_zahl2_string)
print("Die Summe der zwei Zahlen ist:", meine_zahl1 + meine_zahl2) # ausgabe 
print("Die Differnez der zwei Zahlen ist:", meine_zahl1 - meine_zahl2)
print("Das Produkt der zwei Zahlen ist:", meine_zahl1 * meine_zahl2)
print("Der Quotient der zwei Zahlen ist:", meine_zahl1 / meine_zahl2)



#meine_zahlb = input("gib noch eine Zahl ein Oida", meine_zahlb)
#print(type(meine_zahlb))


#neue anweisung
if meine_zahl1>meine_zahl2:
 print("Differenz: ",meine_zahl1-meine_zahl2)
else:
 print("Differenz: ",meine_zahl2-meine_zahl1)
if meine_zahl1>meine_zahl2:
 print("Quotient: ",meine_zahl1/meine_zahl2)
else:
 print("Quotient: ",meine_zahl2/meine_zahl1)

