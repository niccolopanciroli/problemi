print("Questo programma fornisce la interpretazione in decimale di un numero binario")
print()
print("I valori del sistema binario sono solo 1 e 0")
print()
lunghezza= int(input("Inserisci il numero di cifre di cui è composto il numero binario"))
decimale = 0
binario = ""
esponente= 0
x = 0
somma = 0
while x != lunghezza:
    x = x + 1
    cifra = int(input("Inserisci il valore della prima cifra da destra"))
    decimale +=  (2**esponente)*cifra
    esponente= esponente + 1
    binario = binario + str(cifra)

print("Numero binario in decimale è uguale a", decimale)
print("Secondo python il numero binario in decimale è uguale a", int(binario[::-1], base = 2))