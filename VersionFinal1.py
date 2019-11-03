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

    outputFile.write("\u03B4:\n")

    outputFile.close()

if __name__=="__main__":  
    outputFile = open(DFAFinal, "a")
    Output(automaton, Qn, QD, DFAFinal)