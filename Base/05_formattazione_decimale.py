# 2f (è usato per la formattare i numeri con la virgola mobile)
media = 23.456789

# ERRORE COMUNE
# print(media.2f) # attenzione a questo tipo di AttributeError: 'float' object has no attribute '2f
print(f"La media è: {media:.5f}") # 5 chifre dopo la virgola
