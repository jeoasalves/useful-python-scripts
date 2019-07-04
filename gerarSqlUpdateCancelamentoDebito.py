# FUNCOES UTEIS

def rl_quotes(value):
    return '\'' + value + '\''


def r_quotes(value):
    return value + '\''


def l_quotes(value):
    return '\'' + value

def param_parse(param, sql):
    for key, value in param.items():
        if type(value) == str:
            sql = sql.replace(key, rl_quotes(value))
        elif type(value) == int:
            sql = sql.replace(key, str(value))

    return sql

def concat_nl(*params):
    global sql
    value = params[0]

    if len(params) > 1:
        tabulations = params[1]
        sql += '\t' * tabulations + str(value) + '\n'
    else:
        sql += str(value) + '\n'

def concat(*params):
    global sql
    value = params[0]

    if len(params) > 1:
        tabulations = params[1]
        sql += '\t' * tabulations + str(value)
    else:
        sql += str(value)

# PROGRAMA
numero_arquivo = 1
sql = ''
contador = 0
quantidade_registros_arquivo = 10000
nome_arquivo_saida = 'ARQUIVO__'
extensao_arquivo_saida = '.sql'
saida = open(nome_arquivo_saida + str(numero_arquivo) + extensao_arquivo_saida, 'w')
parametros_query = {':id_usuario': 4821,
                    ':nome_usuario_sgu': 'Xxxxxx Xxxxxxxx Xxxxxxxxx',
                    ':cpf_usuario_sgu': '11122233344',
                    ':email_usuario_sgu': 'xxxxxxx@xx.xx.xx',
                    ':id_funcionalidade':13,
                    ':justificativa': 'Xxxxxxxxxxxxxxx',
                    ':id_situacao':3,
                     ':id_debito':0
                    }



def build_sql():
    concat_nl('DECLARE')
    concat_nl('V_ID_SITUACAO NUMBER := 0;',1)
    concat_nl('BEGIN')
    concat_nl('SELECT ID_SITUACAO INTO V_ID_SITUACAO FROM SDA.XXXXXXXXX WHERE ID = :id_debito;',1)
    concat_nl('IF V_ID_SITUACAO = 1 THEN',1)
    concat_nl('UPDATE SDA.XXXXXXXXX SET ID_SITUACAO = :id_situacao WHERE ID = :id_debito;', 2)
    concat_nl('COMMIT;', 2)
    concat_nl('END IF;',1)
    concat_nl('END;')
    concat_nl('/')

with open('entrada.txt') as entrada:
    for linha in entrada:
        id_debito = str(linha).rstrip()
        parametros_query[":id_debito"] = int(id_debito)

        build_sql()

        sql = param_parse(parametros_query, sql)

        saida.write(sql)

        contador += 1

        sql = ''

        if contador >= quantidade_registros_arquivo:
            saida.close()
            numero_arquivo += 1
            contador = 0
            saida = open(nome_arquivo_saida + str(numero_arquivo) + extensao_arquivo_saida, 'w')

saida.close()
