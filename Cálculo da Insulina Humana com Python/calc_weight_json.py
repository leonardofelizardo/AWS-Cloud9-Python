"""
Criação de manipuladores e módulos de arquivos para a recuperação de informações sobre insulina
"""
"""
TRABALHANDO COM ARQUIVOS JSON
"""

# importar modulo personalizado
import jsonFileHandler

# recuperar dados do arquivo
data = jsonFileHandler.readJsonFile('day-5/insulin.json')


# leitura dos dados do arquivo
# verifica se os dados do arquivo foram recuperados
if data != "" :
    
    # acessando as chaves do objeto e pegando os respectivos valores
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    
    # concatenacao
    insulin = bInsulin + aInsulin
    
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']
    
    # mostrando o resultado
    print('bInsulin: ' + bInsulin)
    print('aInsulin: ' + aInsulin)
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))
    
else:
    print("Error. Exiting program")
    
    
# Calculating the molecular weight of insulin  
# Getting a list of the amino acid (AA) weights  
aaWeights = data['weights']

# Count the number of each amino acids  
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']})  

# Multiply the count by the weights  
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']}.values())  

print("The rough molecular weight of insulin: " +
str(molecularWeightInsulin))

print("Percent error: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))