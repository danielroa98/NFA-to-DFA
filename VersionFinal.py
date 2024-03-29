'''
Second Partial Project

Daniel Roa          -   A01021960
Sergio Hernandez    -   A01025210
Sebastian Vives     -   A01025211
Christian Dalma     -   A01423166
'''
import itertools

lista = []
QD = []
Qn = []

#Creación del output
DFAFinal = "OutputDFA.txt"
outputFile = open("OutputDFA.txt", "w+")
outputFile.close()

#Documento donde se obtendrán los datos del NFA
automaton = input("Inserta el nombre junto con la terminación .txt del documento a analizar:\n") 

def split(word): 
    return [char for char in word]

def Output(automaton, Qn, QD, DFAFinal):
    outputFile = open(DFAFinal, "w")

    outputFile.write("Original NFA input: \n")
    myfile = open(automaton, "r")

    if myfile.mode == 'r':
        c = myfile.readline()
        outputFile.write(c)
        print(c)
    outputFile.write("\n")

    
    Lang = ['()', '0', '1']


    outputFile.write("Sigma:\n{")
    #outputFile.write("\u03A3:\n{")
    listToStr = ' '.join(map(str, Lang))
    outputFile.write(listToStr)
    outputFile.write("}\n")

    print("Sigma: ["+listToStr+"]")

    outputFile.write("\nQn:\n")
    #outputFile.close()

    for x in c:
        if x != '{' and x != '(' and x != ','and x != ')'and x != '}' and x != '\n':
            lista.append(x)
            if x not in Qn and x != '0'and x != '1':
                Qn.append(x)

    print(lista)
    print("Qn: ", Qn)
    listToStr = ' '.join(map(str, Qn))
    outputFile.write("{")
    outputFile.write(listToStr)
    outputFile.write("}")
    outputFile.write("\n\n")
    
    outputFile.write("Qd:\n")
    
    for L in range(0, len(Qn)+1):
        for subset in itertools.combinations(Qn, L):
            QD.append(subset)

    print("QD: ",QD)
    listToStr = ' '.join(map(str, QD)) 

    outputFile.write("{")
    outputFile.write(listToStr)
    outputFile.write("}\n")

    outputFile.write("\nFd:\n{")

    #Obtener FD (Final state)
    F = Qn[-1] #Obtenemos el ultimo elemento en la lista Qn
    FD = []
    for x in QD:
        if F in x:
            FD.append(x)

    print("FD: ",FD)
    listToStr = ' '.join(map(str, FD)) 

    outputFile.write(listToStr)
    outputFile.write("}\n")

    outputFile.write("\n")

    #outputFile.write("\u03B4:\n")

    outputFile.write("Delta: \n")

    Delta0 = []
    Delta1 = []
    for x in range(len(lista)):
        #Si empieza en 0
        if lista[x] == '0':
            Delta0.append((lista[x+1],lista[x+2]))
        #Si empieza en 1
        elif lista[x] == '1':
            Delta1.append((lista[x+1],lista[x+2]))

    #print(Delta0[1][1])


    y = Delta0[0][1]+Delta0[1][1]
    z = split(y)
    print(len(Delta0))

    #En 0
    Delta00 = []
    for x in range(len(Delta0)):
        if x < len(Delta0)-1:
            #print("Voy a comparar: ",Delta0[x][0], " y ", Delta0[x+1][0])
            if Delta0[x][0] is Delta0[x+1][0]:
            #   print("yay")
                y = Delta0[x][1] + Delta0[x+1][1]
                z = split(y)
            #  print("En 0, ",Delta0[x][0],"va a ",z)
                Delta00.append((Delta0[x][0],z))
            else:
                z = Delta0[x][1]
            # print("En 0, ",Delta0[x][0],"va a ",z)
                Delta00.append((Delta0[x][0],z))
        else:
            z = Delta0[x][1]
        #  print("En 0, ",Delta0[x][0],"va a ",z)
            Delta00.append((Delta0[x][0],z))

    #En 1
    Delta11 = []
    for x in range(len(Delta1)):
        if x < len(Delta1)-1:
            #print("Voy a comparar: ",Delta1[x][0], " y ", Delta1[x+1][0])
            if Delta1[x][0] is Delta1[x+1][0]:
        #      print("yay")
                y = Delta1[x][1] + Delta1[x+1][1]
                z = split(y)
        #     print("En 1, ",Delta1[x][0],"va a ",z)
                Delta11.append((Delta1[x][0],z))
            else:
                z = Delta1[x][1]
            #    print("En 1, ",Delta1[x][0],"va a ",z)
                Delta11.append((Delta1[x][0],z))
        else:
                z = Delta1[x][1]
            #   print("En 1, ",Delta1[x][0],"va a ",z)
                Delta11.append((Delta1[x][0],z))

    #print("0 ",Delta00)
    #print("1 ",Delta11)

    Delta0F = []
    Delta1F = []
    b = True

    for x in range(len(Delta00)):
        if x is 0:
            Delta0F.append((Delta00[x][0], Delta00[x][1]))
        
        else:
            for y in range(len(Delta0F)):
                if Delta00[x][0] == Delta0F[y][0]:
                # print(Delta00[x][0]," Ya esta ahi!")
                    b = False
            if b is True:
                Delta0F.append((Delta00[x][0], Delta00[x][1]))
            else:
                b = True

    for x in range(len(Delta11)):
        if x is 0:
            Delta1F.append((Delta11[x][0], Delta11[x][1]))
        
        else:
            for y in range(len(Delta1F)):
                if Delta11[x][0] == Delta1F[y][0]:
                    print(Delta11[x][0]," Ya esta ahi!")
                    b = False
            if b is True:
                Delta1F.append((Delta11[x][0], Delta11[x][1]))
            else:
                b = True



    print("0 ",Delta0F)
    listToStr = ' '.join(map(str, Delta0F))
    outputFile.write("0")
    outputFile.write(listToStr)
    outputFile.write("\n")

    print("1 ",Delta1F)
    listToStr = ' '.join(map(str, Delta1F))
    outputFile.write("1")
    outputFile.write(listToStr)


    for x in range(len(Qn)):
        found = 0
        for y in range(len(Delta0F)):
            if Qn[x] is Delta0F[y][0]:
                found = found +1
        if found is 1:
            print()
        else:
            #print(Qn[x]," NO esta en Delta0F")
            Delta1F.append((Qn[x], None))

    # Checar si elemento tiene path nulo en 1
    for x in range(len(Qn)):
        found = 0
        for y in range(len(Delta1F)):
            if Qn[x] is Delta1F[y][0]:
                found = found +1
        if found is 1:
            print()
        else:
            #print(Qn[x]," NO esta en Delta1F")
            Delta1F.append((Qn[x], None))

    print("0 ",Delta0F)
    print("1 ",Delta1F)

    for entry in QD:
        #try:
            D0 = []
            D1 = []
            comb0 = []
            comb1 = []
            tupla = entry
            lista0 = []
            lista1 = []
            l = len(entry)
            b = True
            print ()
            
            for x in range(l):
                for y in range(len(Delta0F)):
                    if tupla[x] is Delta0F[y][0]:
                            comb0.append(Delta0F[y][1])

            for x in range(l):
                for y in range(len(Delta1F)):
                    if tupla[x] is Delta1F[y][0]:
                            comb1.append(Delta1F[y][1])
            
            #Ordenar y obteenr cada elemento de la lista comb0
            for e in comb0:
                for x in range(len(e)):
                    lista0.append(e[x])
            
            for x in range(len(lista0)):
                if x is 0:
                    D0.append(lista0[x])
                
                else:
                    for y in range(len(D0)):
                        if lista0[x] == D0[0]:
                        # print(Delta00[x][0]," Ya esta ahi!")
                            b = False
                    if b is True:
                        D0.append(lista0[x])
                    else:
                        b = True
            D0 = list(dict.fromkeys(D0))

            #Ordenar y obteenr cada elemento de la lista comb1
            for e in comb1:
                if e is not None:
                    for x in range(len(e)):
                        lista1.append(e[x])
            
            for x in range(len(lista1)):
                if x is 0:
                    D1.append(lista1[x])
                
                else:
                    for y in range(len(D1)):
                        if lista1[x] == D1[0]:
                        # print(Delta00[x][0]," Ya esta ahi!")
                            b = False
                    if b is True:
                        D1.append(lista1[x])
                    else:
                        b = True
            D1 = list(dict.fromkeys(D1))

            outputFile = open(DFAFinal, "a")
            
            print("0 for",tupla," is: ",D0)
            #listToStr = ' '.join(map(str, Delta0F))
            outputFile.write("0 for ")
            outputFile.write(str(tupla))
            outputFile.write(" is ")
            outputFile.write(str(D0))
            outputFile.write("\n")
            #outputFile.write(listToStr)
            print("1 for",tupla," is: ",D1)
            outputFile.write("1 for ")
            outputFile.write(str(tupla))
            outputFile.write(" is ")
            outputFile.write(str(D1))
            outputFile.write("\n")

            outputFile.close()

    outputFile.close()

if __name__=="__main__":  
    outputFile = open(DFAFinal, "a")
    Output(automaton, Qn, QD, DFAFinal)

#NFA_test_file_Aug_Dec_2019.txt