from tkinter import E


studenti = {}

while True:
    print("\n--- Registro Studenti ---\n")
    print("1. AGGIUNGI STUDENTE:")
    print("2. MOSTRA REGISTRO")
    print("3. CALCOLA LA MEDIA")
    print("4. PROMOSSI/BOCCIATI")
    print("0. USCIRE")

    scelta = int(input("\nScelta: "))

    if scelta == 1:
        nome = input("\nNome: ")

        voti = []

        for i in range(3):
            while True:
                try:
                    voto = int(input(f"\nVoto {i+1}: "))
                    voti.append(voto)

                    # Salvataggio nel file (csv e excel)
                    break
                except:
                    print("\nInserisci un numero valido!")

        studenti[nome] = voti
    elif scelta == 2:
        if not studenti:
            print("\nRegistro vuoto")
        else:
            for nome, voti in studenti.items():
                print(nome, voti)
    elif scelta == 3:
        if not studenti:
            print("\nNessuno studente inserito")
        else:
            for nome, voti in studenti.items():
                media = sum(voti) / len(voti)
                print(f"\n{nome} - media: {media:2f}")

    elif scelta == 4:
        if not studenti:
            print('\nNessun studente iserito')
        else:
            for nome, voti in studenti.items():
                media = sum(voti) / len(voti)

                if media >= 8:
                    print(nome, 'è stato "PROMOSSO"\n')
                else:
                    print(nome, 'è stato "BOCCIATO"\n')
    elif scelta == 0:
        print('\nUscita del programma scolastico')
        break
    else:
        print("Scelta non valida!")

