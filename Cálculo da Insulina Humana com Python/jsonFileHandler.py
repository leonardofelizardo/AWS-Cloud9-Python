"""
MODULO - TRABALHANDO COM ARQUIVOS
"""
# importar o modulo JSON
import json

# caminho do arquivo
#filePath = "day-5/insulin.json"

# funcao para ler e recuperar os dados do arquivo JSON
def readJsonFile(fileName):
    data = ""
    
    # tratamento de excesao
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    
    # retornar dados do arquivo
    return data