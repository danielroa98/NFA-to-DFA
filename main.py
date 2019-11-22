#   Second Partial Project
#
#   Daniel Roa          -   A01021960
#   Sebastian Vives     -   A01
#   Sergio Hernandez    -   A01069420
#   Christian Dalma     -   A01423166
import itertools

myfile = open("NFA_test_file_Aug_Dec_2019.txt","r")
counter = 0
lista = []
Qn = []

outFile = open("OutputDemo15.txt", "w+")

outFile.write("Original input: \n")

if myfile.mode == 'r':
    c = myfile.readline()
    outFile.write(c)
    print(c)

outFile.close()

#outFile.open("OutputDemo15.txt", "a")
#outFile.write("\nSigma:\n")


outFile = open("OutputDemo15.txt", "a")
outFile.write("\nQn:\n")
outFile.close()

outFile = open("OutputDemo15.txt", "a")

for x in c:
    if x != '{' and x != '(' and x != ','and x != ')'and x != '}' and x != '\n':
      lista.append(x)
      if x not in Qn and x != '0'and x != '1':
          Qn.append(x)

print(lista)
print("Qn: ", Qn)
listToStr = ' '.join(map(str, Qn))

outFile.write(listToStr)

outFile.close()

outFile = open("OutputDemo15.txt", "a")
outFile.write("\n")
outFile.close()

outFile = open("OutputDemo15.txt", "a")
outFile.write("\nQd:\n{")
outFile.close()
QD = []
# Hacer QD donde seran 2^4 posibilidades
for L in range(0, len(Qn)+1):
    for subset in itertools.combinations(Qn, L):
        QD.append(subset)

print("QD: ",QD)
listToStr = ' '.join(map(str, QD)) 

outFile = open("OutputDemo15.txt", "a")

outFile.write(listToStr)
outFile.write("}")
outFile.close()

outFile = open("OutputDemo15.txt", "a")
outFile.write("\n\nFd:\n{")
outFile.close()

#Obtener FD (Final state)
F = Qn[-1] #Obtenemos el ultimo elemento en la lista Qn
FD = []
for x in QD:
    if F in x:
        FD.append(x)

print("FD: ",FD)
listToStr = ' '.join(map(str, FD)) 

outFile = open("OutputDemo15.txt", "a")

outFile.write(listToStr)
outFile.write("}")
outFile.close()

outFile = open("OutputDemo15.txt", "a")
outFile.write("\n")
outFile.close()

print("\nDelta: ")

print("\t\t\t0\t1")
for elem in QD:
    print("_______________________")
    print(elem, " -|")