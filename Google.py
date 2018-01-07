from google import search

searchTerm = input('Procurar por: ')

print('Resultado d a pesquisa:')
for url in search(searchTerm, stop=10):
    print(url)