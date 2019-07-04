# -*- coding: UTF-8 -*-
# -*- coding: UTF-8 -*-

import sys
import os
import util
from buscador import Buscador

if len(sys.argv) == 5:
    print("-" * 100)

    util.logar_valor("diretorio", sys.argv[1])
    util.logar_valor("palavra chave", sys.argv[2])
    util.logar_valor("padrao", sys.argv[3])

    print("-" * 100)

    if os.name != 'posix':
        barra_diretorio = util.barra_windows
    else:
        barra_diretorio = util.barra_linux

    busca = Buscador(sys.argv[1], sys.argv[2], sys.argv[
                     3], sys.argv[4], barra_diretorio)

    busca.pesquisar()

    resultados = busca.get_resultados()

    print('Encontrado ', len(resultados), ' files:')

    for arquivo, contador in resultados.items():
        print('Arquivo: ', arquivo, ' Ocorências:', contador)
else:
    print("Usage:")
    print(
        "py main.py [DIRECTORY] [KEYWORD] [PATTERN(JAVA, TXT, XML, PY, ...)] [SHOW_LINE(true | false)]")
    print("Example:")
    print("py main.py c:\\projet\\django\\ driver xml true")
