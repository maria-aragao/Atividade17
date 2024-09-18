# Crie um programa que receba um ano e verifique se ele é bissexto. Um ano é bissexto se for divisível por 4, exceto se for divisível por 100 e não por 400.

N = int(input("Digite seu ano:"))

if N % 100 !=0 and N % 4 == 0 or N % 400 == 0:
    print("o seu ano é bissexto")

else: 
    print("seu ano não é bissexto")