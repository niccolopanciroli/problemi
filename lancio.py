print("Dato un elenco di studenti partecipanti a una gara sportiva di lancio del peso visualizza il valore del lancio")
print()

partecipanti = []
lanci= []
numero = int(input("Inserisci il numero dei partecipanti alla gara sportiva "))
contatore = 0

while contatore != numero: 
    contatore= contatore + 1
    nome = str(input("Inserisci il nome dello studente "))
    lancio= int(input("Inserisci la distanza del lancio dello studente "))

    partecipanti.append(nome)
    lanci.append(lancio)

risultato = zip(partecipanti, lanci)
print("I nomi dei pertecipanti con i relativi risultati: ",list(risultato))
print("Il lancio massimo è ", max(lanci))