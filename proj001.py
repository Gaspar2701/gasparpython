#_______________projeto 001__________________________

#------------variveis globais------------------------
lista_produto = []
codigo_produto = 0

#------------ fim variveis globais------------------------


#------------------inicio cadastrar_produto--------------
def cadastrar_produto(codigo):
    print('Bem-vindo  ao menu cadastrar_produto')
    print('código do produto: {}.'.format(codigo))
    nome = input('Digite o NOME do produto:  ')
    fabricante = input('Digite o FABRICANTE do produto:  ')
    preco = float(input('Digite o PREÇO(R$) do produto:  '))
    dicionario_produto = {'codigo'     : codigo,
                          'nome'       : nome,
                          'fabricante' : fabricante,
                          'preco'      : preco}
    lista_produto.append(dicionario_produto.copy())

#------------------fim  cadastrar_produto--------------

#------------------inicio consultar_produto--------------
def consultar_produto():
    print('Bem-vindo  ao menu consultar_produto')
    while True:
        consultar_produto = input('Qual a opção desejada:\n'+
                                ' 1 - consultar por TODOS OS produtos:\n' +
                                ' 2 - consultar produto por CÓDIGO:\n'+
                                ' 3 - consultar produto por FABRICANTE:\n'+
                                ' 4 - retornar\n'+
                                '>>  ')
        if consultar_produto == '1':
            print('Você escolheu a opção consultar por TODOS os produtos')
            for produto in lista_produto:
                print('----------------------------------------')
                for key,value in produto.items():
                    print('{}:  {} '.format(key,value))
                print('------------------------------------')

        elif consultar_produto == '2':
            print('Você escolheu a opção consultar produto por CÓDIGO')

        elif consultar_produto == '3':
            print('Você escolheu a opção consultar produto por FABRICANTE')

        elif consultar_produto == '4':
            return
        else:
            print('Opção inválida . Tente novamente')
            continue#volta para o inicio do laço
#------------------fim  consultar_produto--------------

#------------------inicio remolver_produto--------------
def remolver_produto():
    print('Bem-vindo  ao menu remolver_produto')

#------------------fim  cadastrar_produto--------------

#------------------inicio main--------------
print('Bem-vindo  ao mercantil do Marcos')
while True:
    opcao_principal = input('Qual a opção desejada:\n'+
                            ' 1 - cadastrar produto:\n'+
                            ' 2 - consultar produto:\n'+
                            ' 3 - remover produto:\n'+
                            ' 4 - sair\n'+
                            '>>  ')
    if opcao_principal == '1':
        codigo_produto += + 1
        cadastrar_produto(codigo_produto)
    elif opcao_principal == '2':
        consultar_produto()
    elif opcao_principal == '3':
        remolver_produto()
    elif opcao_principal == '4':
        break #encerra o laço principal eo programa acaba
    else:
        print('Opção inválida . Tente novamente')
        continue#volta para o inicio do laço




#------------------fim  main--------------