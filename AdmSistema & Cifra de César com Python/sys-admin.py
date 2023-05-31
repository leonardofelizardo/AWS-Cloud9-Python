"""
Administrando Sistemas com Python
"""
# importar a lib OS
import os
# importar a lib SUBPROCESS
import subprocess

# comandos
# listar itens na pasta
os.system("ls")
subprocess.run(["ls"])

# listar com infos
subprocess.run(["ls", "-l"])

# listar arquivo especifico
subprocess.run(["ls", "-l", "README.md"])

# comando e processos em variaveis
command="uname"
commandArgument="-a"

print(f'Gathering system information with command: {command} {commandArgument}')
# executando infos da maquina
subprocess.run([command,commandArgument])

command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])