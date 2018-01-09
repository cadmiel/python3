from google import search
import wikipedia

searchTerm = input('Procurar por: ')

opcao = True
while opcao:
    contador = 0
    print('Onde deseja pesquisar? ')
    print('1 - Google')
    print('2 - Wikipedia')
    print('3 - Sair')
    escolha = int(input('> '))
    print('Por favor aguarde pesquisando...')
    if escolha == 1:
        for url in search(searchTerm, stop=10):
            print(url)
    elif escolha == 2:
        wikipedia.set_lang("pt")
        for results in  wikipedia.search(searchTerm):
            print(wikipedia.summary(results, sentences=1))
    elif escolha == 3:
        opcao = False
        break
    else:
        print('Opção invalida, por favor selecione outra opcao')
        opcao = True
