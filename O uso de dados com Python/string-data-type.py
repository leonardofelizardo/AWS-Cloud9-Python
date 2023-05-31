"""
Uso do tipo de dados de string
"""
"""
Apresentação do tipo de dado string
"""
myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))
"""
Uso da concatenação de strings
"""
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
"""
Uso de strings de entrada / Formatação de strings de saída
"""
name = input("what is your name? ")
print(name)
color = input("what is your favorite color? ")
animal = input("what is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))