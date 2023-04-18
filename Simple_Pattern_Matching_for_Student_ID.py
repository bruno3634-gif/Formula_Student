import datetime 
numero = input()
ano_atual = ""

if numero.isdigit() and len(numero) == 7:

    today = datetime.date.today()
    year = today.year
    ano_atual = str(year)
    ano_atual = ano_atual[2:4]
    ano = numero[1:3]
    campus = numero[0]
    campus_n = int(campus)
    print("Campus: ",campus)
    print("Ano: ",ano)

    if ano <= ano_atual:
        if campus_n <= 5 and campus_n>=1:
            
            print("O número inserido é válido")
        else:
                print("O número inserindo é inválido")
else:
    print("O número inserindo é inválido")
