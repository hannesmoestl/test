#schleifen-/Zählvariable i,j,k
#addieren sie in einer schleife die zahlen a bis 100 und gegeb sie das ergebniss an

counter = 10
while counter >=0:
    counter = counter -1 #alt counter =1
    print(counter)
    
Ergebnis = 0
x = 1
while x <= 100:
    Ergebnis += x
    x += 1
print(Ergebnis)

