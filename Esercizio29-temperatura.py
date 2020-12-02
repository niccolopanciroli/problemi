print("Questo programma fornisce il numero di città che hanno superato il valore stabilito come escursione termica media")
print()

valore_stabilito= int(input("Inserisci un valore della escursione termica media "))
ncittà = int(input("Inserisci il numero delle città "))
x = 0 
nomicittà = []
escursionetermica = []
contatore = 0

while x != ncittà:
    x = x + 1
    città= input("Inserisci il nome della città ")
    nomicittà.append(città)
    temperaturamassima = int(input("Inserisci la temperatura massima registrata in città "))
    temperaturaminima = int(input("Inserisci la temperatura minima registrata in città "))

    if temperaturamassima - temperaturaminima> valore_stabilito:
        escursionetermica.append(temperaturamassima - temperaturaminima)
        contatore = contatore +1

print("Le città che hanno superato il valore stabilito sono: ", contatore)