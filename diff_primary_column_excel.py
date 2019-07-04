from xlrd import open_workbook

def ler_primeira_coluna(arquivo_excel):
    planilha = open_workbook(arquivo_excel,on_demand=True)

    lista_coluna = []

    for nomePasta in planilha.sheet_names():
        pasta = planilha.sheet_by_name(nomePasta)

        for indice,celula in enumerate(pasta.col(0)):
            if indice == 0:
                continue

            lista_coluna.append(celula.value)

        break

    return lista_coluna

def diff(listaA, listaB):
    c = set(listaA).union(set(listaB))
    d = set(listaA).intersection(set(listaB))
    return list(c - d)


def imprimir_lista(lista):
    for item in lista:
        print(item)

colunaA = ler_primeira_coluna('simple.xls')
colunaB = ler_primeira_coluna('simpleB.xls')

print()
print("Coluna A: ")
print()
print(str(colunaA))

print()
print("Coluna B: ")
print()
print(str(colunaB))

diferenca = diff(colunaA, colunaB)

print()
print("Diferenca entre as colunas: ")
print()
print(str(diferenca))





