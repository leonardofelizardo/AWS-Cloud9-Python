""""
CALCULO DE INSULINA
"""

# lendo arquivo
with open('preproinsulin-seq-clean.txt') as file:
    insulinFile = file.read()

# valores
lsInsulin = insulinFile[0:24]
bInsulin = insulinFile[25:54]
aInsulin = insulinFile[90:110]
cInsulin = insulinFile[55:89]

# concatenar string grandes
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# insulina humana A + B
insulin = aInsulin + bInsulin

print("INSULIN: ", insulin)

# chave A
print("The sequence of human insulin, chain a: " + aInsulin)

# Calculating the molecular weight of insulin  
# Creating a list of the amino acid (AA) weights  
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}

# Count the number of each amino acids  
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']})  

# Multiply the count by the weights  
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())  
print("The rough molecular weight of insulin: " +
str(molecularWeightInsulin))


# peso molecular atual da insulina humana
molecularWeightInsulinActual = 5807.63

# calculo de erro de percentagem
print("Error percentage: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))

# valores de referencia
pKR = {'y':10.07,'c': 8.18,'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25}

# contagem da sequencia de caracteres da insulina
seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})

# variavel de controle
pH = 0

# loop
while (pH <= 14):
    netCharge = (
        +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
        for x in ['k','h','r']}.values()))
        -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
        for x in ['y','c','d','e']}.values())))
    # incremento da variavel de controle
    pH +=1

# resultado da analise da insulina
# formatacao de casa decimais do float ({0:.2f})
print('{0:.2f}'.format(pH), netCharge)