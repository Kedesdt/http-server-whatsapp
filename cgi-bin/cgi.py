#!/usr/bin/python3
# coding: utf-8

import os.path, cgi, cgitb, json, sqlite3

cgitb.enable(display=0, logdir='/var/banco')


def printJson(data):
    # print('Content_type: text/html')
    print('Status: 200 OK\n\r')
    #print('%s' % data)


form = cgi.FieldStorage()
erro = False
nome = 'Nome'

if "nome" in form:
    nome = str(form['nome'].value)
else:

    erro = True

if not erro:

    if nome == "all":
        data = {}

        conexao = sqlite3.connect(caminho)  # conexao
        cursor = conexao.cursor()
        cursor.execute("select * from radios")
        radios = cursor.fetchall()

        for i in range(len(radios)):
            try:
                query = 'select * from dados where time = (select max(time) from dados where ID=%s) and ID = %s;' % (
                radios[i][0], radios[i][0])
                cursor.execute(query)
                resultado = cursor.fetchall()
                d1 = '{"time": "%s", "nivel": %i, "estereo": %i, "RDS": %i, ' \
                     '"FMStation": %i, "Freq": %f, "AudioL": %i, "AudioR": %i, ' \
                     '"FMready": %i, "Dpl": %i, "Dpr": %i}' % (resultado[0][1], resultado[0][2],
                                                               resultado[0][3], resultado[0][4],
                                                               resultado[0][5], float(resultado[0][6]),
                                                               resultado[0][7], resultado[0][8],
                                                               resultado[0][9], resultado[0][10],
                                                               resultado[0][11])
            except:
                d1 = '{"time": "None", "nivel": "None", "estereo": "None", "RDS": "None", "FMStation": "None", "Freq": "None", "AudioL": "None", "AudioR": "None", "FMready": "None", "Dpl": "None", "Dpr": "None"}'
            try:
                # d2 = open("./%s.json" % radiosP[i], 'rb').read()
                # d2 = d2.decode()
                query = 'select * from pulso where dataHora = (select max(dataHora) from pulso where IDRadio = %s)' % \
                        radios[i][0]
                cursor.execute(query)
                resultado = cursor.fetchall()
                d2 = '{"time": "%s", "nome": "%s", "status": %i}' % (
                resultado[0][0], radios[i][3], 1 if resultado[0][2] == "Local" else 0)
            except:
                d2 = '{"time": "None", "nome": "None", "status": "None"}'

            d1 = json.loads(d1)
            d2 = json.loads(d2)

            data[radios[i][1]] = {"fm": d1, "pulso": d2}

        data = json.dumps(data)

    else:
        data = {}
        conexao = sqlite3.connect(caminho)  # conexao
        cursor = conexao.cursor()

        query = "select * from radios "
        query += "inner join radio_cliente "
        query += "on radio_cliente.ID_radio = radios.ID "
        query += "inner join cliente "
        query += "on cliente.ID = radio_cliente.ID_cliente "
        query += "where cliente.ID = %s" % nome
        query += ";"
        cursor.execute(query)
        radios = cursor.fetchall()

        for i in range(len(radios)):
            try:
                query = 'select * from dados where time = (select max(time) from dados where ID=%s) and ID = %s;' % (
                radios[i][0], radios[i][0])
                cursor.execute(query)
                resultado = cursor.fetchall()
                d1 = '{"time": "%s", "nivel": %i, "estereo": %i, "RDS": %i, ' \
                     '"FMStation": %i, "Freq": %f, "AudioL": %i, "AudioR": %i, ' \
                     '"FMready": %i, "Dpl": %i, "Dpr": %i}' % (resultado[0][1], resultado[0][2],
                                                               resultado[0][3], resultado[0][4],
                                                               resultado[0][5], float(resultado[0][6]),
                                                               resultado[0][7], resultado[0][8],
                                                               resultado[0][9], resultado[0][10],
                                                               resultado[0][11])
            except:
                d1 = '{"time": "None", "nivel": "None", "estereo": "None", "RDS": "None", "FMStation": "None", "Freq": "None", "AudioL": "None", "AudioR": "None", "FMready": "None", "Dpl": "None", "Dpr": "None"}'
            try:
                # d2 = open("./%s.json" % radiosP[i], 'rb').read()
                # d2 = d2.decode()
                query = 'select * from pulso where dataHora = (select max(dataHora) from pulso where IDRadio = %s)' % \
                        radios[i][0]
                cursor.execute(query)
                resultado = cursor.fetchall()
                d2 = '{"time": "%s", "nome": "%s", "status": %i}' % (
                resultado[0][0], radios[i][3], 1 if resultado[0][2] == "Local" else 0)
            except:
                d2 = '{"time": "None", "nome": "None", "status": "None"}'

            d1 = json.loads(d1)
            d2 = json.loads(d2)

            data[radios[i][1]] = {"fm": d1, "pulso": d2}

        data = json.dumps(data)

printJson(data)


