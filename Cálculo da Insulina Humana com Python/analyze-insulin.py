"""
Preparar-se para analisar insulina com Python
"""
"""
Recuperação da sequência de proteínas da preproinsulina humana
"""
"""
Obtenção da sequência de proteínas da insulina humana
"""

with open('preproinsulin-seq-clean.txt') as file:
    insulinFile = file.read()
print(insulinFile)
lsInsulin = insulinFile[0:24]
bInsulin = insulinFile[25:54]
aInsulin = insulinFile[90:110]
cInsulin = insulinFile[55:89]
print("DINAMICO: ", lsInsulin ,bInsulin, aInsulin, cInsulin)