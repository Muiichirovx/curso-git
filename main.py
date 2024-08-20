
valor1 = int(input("Digite o primeiro valor : "))
valor2 = int(input("Digite o segundo valor : "))



print("Selecione um operador:")
print("Soma + ")
print("Subtração - ")
print("Multiplicação * ")
print("Divisão / ")

operador = input(str("Digite o operador: "))


if operador == "+":
    print(valor1 + valor2)
elif operador == "-":
    print(valor1 - valor2)
elif operador == "*":
    print(valor1 * valor2)
elif operador == "/":
    print(valor1 / valor2)
else:
    print("Operador inválido")




