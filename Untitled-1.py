def calculator():
    print("=== Calculadora Matemática ===")
    print("Operações: + (soma), - (subtração), * (multiplicação), / (divisão)")
    
    try:
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))
        
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                print("Erro: Divisão por zero!")
                return
            resultado = num1 / num2
        else:
            print("Operação inválida!")
            return
        
        print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
    except ValueError:
        print("Erro: Digite números válidos!")

calculator() 