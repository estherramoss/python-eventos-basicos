dia= (input("Indique o dia da semana: "))

# Função de fim de semana
def dia_da_semana(dia):
    match dia: 
        case "Domingo" | "Sábado":
            return "Fim de Semana"
        case "Segunda" | "Terça"| "Quarta" |"Quinta" |"Sexta":
            return "Dia Útil"
        case _:
             return "Valor inválido"
        
        
# Exibe o resultado da função na tela
print(dia_da_semana(dia))
    

