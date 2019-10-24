#   Second Partial Project
#
#   Daniel Roa          -   A01021960
#   Sebastian Vives     -   A01
#   Sergio Hernandez    -   A01069420
#   Christian Dalma     -   A01423166
#file = open("NFA_test_file_Aug_Dec_2019.txt", "r")

#if file.mode == 'r':            # r = leer documento
#    contenido = file.read()
#    print(contenido)            # imprime contenido del .txt
import numpy as np

def readFile(file):
	with open(file, 'r') as f:
		a = [[x for x in line.replace('{', '').replace('}', '').replace(
			'(', '').replace(')', '').replace('\n', "").split(',')] for line in f]
	a = np.array(a)
	array2D = a.reshape((a.size/3, 3))
	return array2D

