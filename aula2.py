

# INPUT - UTILIZADO PARA RECEBER DADOS DO USUARIO (exemplo)
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))

print("meu nome é ", nome, "tenho ", idade, "peso ", peso, "kg")

# exercicio 1 

nome = input("Digite seu nome: ")
print(f"olá {nome}, seja bem vindo")

#exercicio 2

dia = int(input("Digite seu dia de nascimento: "))
mes = int(input("Digite seu mês de nascimento: "))
ano = int(input("Digite seu ano de nascimento: "))

print(f"Você nasceu em {dia}/{mes}/{ano}")

# exercicio 3

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = num1 + num2
print(f"A soma de {num1} e {num2} é igual a {soma}")
