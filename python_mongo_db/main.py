#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient
from resource.query import query_pipeline
from pandas.io.json import json_normalize
import os
import sys
import codecs
import pandas as pd
import json
import subprocess

#  INICIO DEFINIÇÃO DE FUNÇÕES #


def clearFiles(path):
    try:
        os.remove(path + '\\resultado.json')
    except FileNotFoundError:
        pass

    try:
        os.remove(path + '\\resultado.xlsx')
    except FileNotFoundError:
        pass


def remove_bom_inplace(path):
    buffer_size = 4096
    bom_length = len(codecs.BOM_UTF8)

    with open(path, "r+b") as fp:
        chunk = fp.read(buffer_size)
        if chunk.startswith(codecs.BOM_UTF8):
            i = 0
            chunk = chunk[bom_length:]
            while chunk:
                fp.seek(i)
                fp.write(chunk)
                i += len(chunk)
                fp.seek(bom_length, os.SEEK_CUR)
                chunk = fp.read(buffer_size)
            fp.seek(-bom_length, os.SEEK_CUR)
            fp.truncate()


def escreverJson(path, pedidos):
    arquivoJson = open(path, 'a')

    linhas_pedidos = []

    arquivoJson.write('[\n')

    for pedido in pedidos.aggregate(query_pipeline):
        linhas_pedidos.append(str(pedido).replace('\'', '\"').replace(
            "codigoPedido\": \"", "codigoPedido\": \"-"))

    for linha in range(len(linhas_pedidos)):
        arquivoJson.write(str(linhas_pedidos[linha]))

        if linha < (len(linhas_pedidos) - 1):
            arquivoJson.write(', ')
        arquivoJson.write('\n')

    arquivoJson.write(']')

    arquivoJson.close()


def converter_json_to_excel(arquivoJson, arquivoExcel):
    pd.read_json(arquivoJson, 'r', encoding='utf8').to_excel(
        arquivoExcel, sheet_name='pedidos', index=False)


#  INICIO PROGRAMA #

cliente = MongoClient('mongodb://localhost:27017/jeoas')

banco = cliente['jeoas']

pedidos = banco['pedidos']

basePath = os.path.dirname(os.path.abspath(__file__)) + '\\output'

clearFiles(basePath)

filename = "resultado.json"

escreverJson(basePath + '\\' + filename, pedidos)

remove_bom_inplace(basePath + '\\' + filename)

converter_json_to_excel(basePath + '\\' + filename,
                        basePath + '\\' + 'resultado.xlsx')
