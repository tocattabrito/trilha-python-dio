salario = 2000




# Exemplo 1
# def salario_bonus(bonus):
#     global salario
#     salario += bonus
#     return salario


# salario_com_bonus = salario_bonus(500)  # 2500
# print(salario_com_bonus)


# Exemplo 2
def salario_bonus(bonus, lista):
    global salario
    
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux={lista_aux}")

    salario += bonus
    return salario

lista = [1,2]
salario_com_bonus = salario_bonus(500, lista)  # 2500
print(salario_com_bonus)
print(lista)