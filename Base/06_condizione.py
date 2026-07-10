"""

    Servono a prendere decizioni al programma
    if(SE) else(altrimenti)
    if condizione:
        codie
    else:
        codice


    if(SE) elif(altrimenti sé) else(altrimenti)
    if condizione:
        codie
    elif condizione:
        codice
    elif condizione:
        codice
    elif condizione:
        codice
    else:
        codice
"""

"""
    Gli operatori di confronso sono
    <; >; ==; <=; >=; !=;

    Gli operatori logici
    AND(&&) OR(||) NOT(!)
"""

# Esempio di login
email = 'antonella.r@gmail.com'
password = 'Antonella@2026'

utente = input("📧 Inserisci la mail: ")
password_utente = input('🔐 Inserisci la password: ')

if email == utente and password == password_utente:
    print('Benvenuto nel sistema')
elif email != utente:
    print('📧 Verifica la mail')
elif password_utente != password:
    print('⚠️ Password errato.\n Riprova')
else:
    print('Accesso negato')
