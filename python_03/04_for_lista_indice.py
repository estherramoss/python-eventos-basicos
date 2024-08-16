# Lista usando laço for
print(" ")
print("Lista de lojas")
print(" ")

lojas = ["Santo André", "São Bernado","SCS", "Mauá", "Diadema"]

# Listar usando laço co indice
for i, loja in enumerate(lojas, 1):
    print(f"{i} - {loja}")