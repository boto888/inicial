def rendimento_OITO_porcento(entrada):
    rendimento = 1.08
    inicial = entrada
    historico = []
    for tempo in range(1, 11):
        inicial *= rendimento
        historico.append((tempo, inicial))
    return historico

def rendimento_DEZ_porcento(entrada):
    rendimento = 1.10
    inicial = entrada
    historico = []
    for tempo in range(1, 11):
        inicial *= rendimento
        historico.append((tempo, inicial))
    return historico

def rendimento_QUINZE_porcento(entrada):
    rendimento = 1.15
    inicial = entrada
    historico = []
    for tempo in range(1, 11):
        inicial *= rendimento
        historico.append((tempo, inicial))
    return historico


print(f"""
    Escolha a opção que mais lhe agrada.\n
      1 -> para depositos com rendimentos de 8% ao ano.\b
      2 -> para depositos com rendimentos de 10% ao ano.\b
      3 -> para depositos com rendimentos de 15% ao ano.\b
""")
try:
    escolha_de_deposito = int(input('sua escolha foi: '))
    if escolha_de_deposito == 1:
        valor_do_deposito = int(input('digite o valor a ser depositado: '))
        retorno_do_investimento = rendimento_OITO_porcento(entrada=valor_do_deposito)
        for tempo, valor in retorno_do_investimento:
            print(f'{tempo}| {valor:.2f}')
    elif escolha_de_deposito == 2:
        valor_do_deposito = int(input('digite o valor a ser depositado: '))
        retorno_do_investimento = rendimento_DEZ_porcento(entrada=valor_do_deposito)
        for tempo, valor in retorno_do_investimento:
            print(f'{tempo}| {valor:.2f}')
    elif escolha_de_deposito == 3:
        valor_do_deposito = int(input('digite o valor a ser depositado: '))
        retorno_do_investimento = rendimento_QUINZE_porcento(entrada=valor_do_deposito)
        for tempo, valor in retorno_do_investimento:
            print(f'{tempo}| {valor:.2f}')
    else:
        print('opcão inválida')
except TypeError:
    print('entrada inválida hehehe')
except ValueError as e:
    print('entrada inválida hehehe', type(e)) # exec bash
    