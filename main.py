#Projeto: Calculadora Aluna: Karina Nerone
def calculadora():
    operacao = input("Escolha a operação a realizar (+, -, *, /, **): ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao == "+":
        resultado = num1 + num2
        print("O resultado da adição é:", resultado)
    elif operacao == "-":
        resultado = num1 - num2
        print("O resultado da subtração é:", resultado)
    elif operacao == "*":
        resultado = num1 * num2
        print("O resultado da multiplicação é:", resultado)
    elif operacao == "/":
        if num2 ==  0:
            print("ERRO: divisão por zero não é permitida!")
        else:
            resultado = num1 / num2
            print("O resultado da divisão é:", resultado)
    elif operacao == "**":
        resultado = num1 ** num2
        print("O resultado da exponenciação é:", resultado)
    elif operacao == "%":
        resultado = num1 % num2
        print("O resultado do módulo é:", resultado)
    else:
        print(f"Operação '{operacao}' inválida! Por favor, escolha uma operação válida (+, -, *, /, **, %).")

calculadora()


