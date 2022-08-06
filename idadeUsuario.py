verificador = True
while(verificador):
    try:
        nome = input("Digite o seu nome Completo: ")
        idade =  2022 - int(input("Digite o seu ano de nascimento: "))
        if(idade <= 0 or idade > 100):
            print("Idade invalida")
        else:
            verificador = False
    except:
        print('Ocorreu um erro, tente novamente')
print(f"Olá {nome} vc tem ou vai fazer {idade} anos em 2022")