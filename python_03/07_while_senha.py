i = 1
while i >= 3:
    user = input("Informe o usuário: ")
    senha = input("Informe a senha: ")

# Checagem
    if user != "Gisele" or senha != "123":
        i += 1
        print("Usuário ou Senha incorretos!")
        print(" ")

    else: 
        print("")
        print(f"Bem - Vindo, {user}!")
        break # Encerra ao inserir a senha correta

else:
    print(f"Você execeu todas as: {i-1} tentativas!!")