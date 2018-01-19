class File:

    def __init__(self):
        self.results = []
        self.errors  = []

    def search(self, body, term, filename):
        term = term.lower()
        body = body.lower()
        if term in  body:
            self.append({'term':term,'filename':filename, 'occurrence':body.count(term)}, self.results)

    def append(self, newObj, collection=None):

        if collection is None:
            collection = self.errors

        collection.append(newObj)

    def print(self):
        print('******************************')
        print('Resultado da pesquisa')
        print('******************************')
        print('Total de arquivos: ',len(self.results))
        print(self.results)
        print('******************************')
        print('Erros encotrado')
        print('******************************')
        print(self.errors)
        print('******************************')

