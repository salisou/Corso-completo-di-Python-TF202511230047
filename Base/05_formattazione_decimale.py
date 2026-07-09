# 2f (è usato per la formattare i nume in virgola mobile)
media = 23.456789

# ERRORE COMUNE 
# print(media.f2) # attenzione a questo tipo di AttributeError: 'float' object has no attribute 'f2
print(f"La media è: {media:.5f}") # 5 chifre dopo la virgola 