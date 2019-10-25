#   Second Partial Project
#
#   Daniel Roa          -   A01021960
#   Sebastian Vives     -   A01
#   Sergio Hernandez    -   A01069420
#   Christian Dalma     -   A01423166
file = open("NFA_test_file_Aug_Dec_2019.txt", "r")

if file.mode == 'r':            # r = leer documento
    contenido = file.read()
    print(contenido)            # imprime contenido del .txt

a = [[x for x in line.replace('{', '').replace('}', '').replace(
    '(', '').replace(')', '').replace('\n', "").split(',')] for line in file]
