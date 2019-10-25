import itertools

myfile = open("NFA.txt","r")
counter = 0
lista = []
Qn = []

if myfile.mode == 'r':
    c = myfile.readline()
    print(c)

for x in c:
    if x != '{' and x != '(' and x != ','and x != ')'and x != '}' and x != '\n':
      lista.append(x)
      if x not in Qn and x != '0'and x != '1':
          Qn.append(x)

print(lista)
print("Qn: ", Qn)

QD = []
# Hacer QD donde seran 2^4 posibilidades
for L in range(0, len(Qn)+1):
    for subset in itertools.combinations(Qn, L):
        QD.append(subset)

print("QD: ",QD)

#Obtener FD (Final state)
F = Qn[-1] #Obtenemos el ultimo elemento en la lista Qn
FD = []
for x in QD:
    if F in x:
        FD.append(x)
    
print("FD: ",FD)
