# Creazione della lista
            #  0        1         2
mia_lista = ["Mela", "Banana", "Pera"] # (variable) mia_lista: list

        #    0       1       2         3        4
colori = ["Rosso", "blu", "Verde", "Giallo", "Bianco"]


# Stampa della lista
print(mia_lista, '\n\n')

# Accedere ad un elemento della lista
print(colori[1]) # select nome from colori where id = 1

# Modificare un elemento della lista
mia_lista[1] = 'Kiwi' # UPDATE tabella set nome = 'Kiwi' where id = 1
print(mia_lista)


print('=' * 40, '\n')

# Lunghezza della lista
studenti = ['Massa', 'Anntonella', 'Luigi', 'Eduardo', 'Matteo', 'Stefano', 'Lucia', 'Annaritantonia', 'Paolo']

print(len(studenti))

# Aggiungere elementi nella lista
voti = []

voti.append(10) # INSERT INTO tabella (ore) values (10)
voti.append([10, 20, 30,40,50]) # INSERT INTO tabella (ore) values (10) (20), (30), (40), (50)

print('Lista dei voti', voti, '\n')

frutti = ['Mela', 'Banana']
frutti.insert(1, 'Ananas')

print()
print(frutti)

# Eleminare un elemento nella lista
frutti.remove('Banana') # DELETE FRON frutti Where nome = 'Banana'

print()
print(frutti)

# Eliminare un elemento nella lista

print()
print(studenti)
studenti.pop(2) # DELETE FRON frutti Where id = 2
print()
print(studenti)


# Svuotare gli elememnti della lista
utenti = ['Massa', 'Anntonella', 'Luigi', 'Eduardo', 'Matteo', 'Stefano', 'Lucia', 'Annaritantonia', 'Paolo']

utenti.clear() # Delete studenti senza il filtro where
print('Lista vuota', utenti)

# Verifica degli elementi esistente

print('=' * 40, '\n')
persone = ['Massa', 'Anntonella', 'Luigi', 'Eduardo', 'Matteo', 'Stefano', 'Lucia', 'Annaritantonia', 'Paolo']
print('Prima della modificazione del None di',  persone[0])
print('=' * 40, '\n')


persone[0] = 'Moussa'
print('Dopo della modificazione ',  persone[0])

# per recuperare una persona con l'indice
print('=' * 40, '\n')


print(len(persone))
print('=' * 40, '\n')

for i in range(len(persone)):
    print('Nome ', i, persone[i])


print('=' * 40, '\n')
