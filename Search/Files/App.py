from bottle import run
import os
import docx2txt
from Business import File

import textract
import platform

if 'Windows' in platform.system():
    print('SO WINDOWS')
else:
    print('OTHER')


opcao=True
prefixDirectory = 'Doc/'

while opcao:
    # os.system('clear')

    searchTerm = input('Procurar por: ')

    __file = File()

    for filename in os.listdir(prefixDirectory):
        try:
            body = ''
            body = str( textract.process(prefixDirectory+filename) )
            __file.search(body, searchTerm, filename)
            # if('.docx' in filename):
            #     body = docx2txt.process(prefixDirectory+filename)
            #     __file.search(body, searchTerm, filename)
            # elif('.txt' in filename):
            #     body = open(prefixDirectory + filename, mode='r+')
            #     __file.search(body.read(), searchTerm, filename)
            #     body.close()
            # else:
            #     __file.append(
            #         {'term':searchTerm,'filename':filename,
            #          'msg':'extensão('+filename.split('.')[-1]+') não suportada!!!'}
            #     )
        except Exception as error:
            print('Erro:',error)

    __file.print()

    print('1 - Continuar')
    print('2 - Sair')

    try:
        contt = int(input('> '))
    except Exception as error:
        contt = 2
        print('Erro: ',error, ' - opção inválida')

    if contt == 2:
        opcao = False
        break

    opcao = True

## COMEÇO SCRIPT RODA WINDOWS
#
# while opcao:
#     os.system('clear')
#     searchTerm = input('Procurar por: ')
#
#     __file = File()
#
#     for filename in os.listdir(prefixDirectory):
#         try:
#             body = ''
#             if('.docx' in filename):
#                 body = docx2txt.process(prefixDirectory+filename)
#                 __file.search(body, searchTerm, filename)
#             elif('.txt' in filename):
#                 body = open(prefixDirectory + filename, mode='r+')
#                 __file.search(body.read(), searchTerm, filename)
#                 body.close()
#             else:
#                 __file.append(
#                     {'term':searchTerm,'filename':filename,
#                      'msg':'extensão('+filename.split('.')[-1]+') não suportada!!!'}
#                 )
#         except Exception as error:
#             print('Erro:',error)
#
#     __file.print()
#
#     print('1 - Continuar')
#     print('2 - Sair')
#
#     try:
#         contt = int(input('> '))
#     except Exception as error:
#         contt = 2
#         print('Erro: ',error, ' - opção inválida')
#
#     if contt == 2:
#         opcao = False
#         break
#
#     opcao = True
#
## FIM SCRIPT RODA WINDOWS

# run(reloader=True)