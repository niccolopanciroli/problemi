numero= int(input("Inserisci il numero decimale da trasformare in binario"))
binario = []
x= numero
while x != 0:

    cifra= x % 2 #il resto è sempre 0 o 1
    x //= 2
    binario.append(cifra)

binario.reverse()
print("Il numero inserito, ",numero, ",trasformato in binario è ",binario)
print("Il numero ", bin(numero))