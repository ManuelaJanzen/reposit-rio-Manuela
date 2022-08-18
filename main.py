#Comando para ler o arquivo txt
myTxtFile = open("teste4.txt","r")
vector = []
matriz = []
vector = myTxtFile.readlines()
for i in range(len(vector)):
    matriz.append(vector[i].split())



# Função para realizar a união de conjuntos:
def union(vectorOne, vectorTwo):

    # Comandos para retirar elementos repetidos de um conjunto:
    noDupes = []
    for i in vectorOne:
        if i not in noDupes:
            noDupes.append(i)
    noDupesTwo = []
    for i in vectorTwo:
        if i not in noDupesTwo:
            noDupesTwo.append(i)

    # Comandos para obter o resultado da operação desejada:
    result = []
    for i in range(len(noDupes)):
        result.append(noDupes[i])
    for x in range(len(noDupesTwo)):
        result.append(noDupesTwo[x])

    # Comandos para retirar elementos repetidos de um conjunto:
    noDupesResult = []
    for i in result:
        if i not in noDupesResult:
            noDupesResult.append(i)

    # Comandos para retirar vírgulas das listas:
    groupA = []
    for a in range(len(noDupes)):
        listA = noDupes[a]
        a = listA.replace(",","")
        groupA.append(a)
    groupB = []
    for b in range(len(noDupesTwo)):
        listB = noDupesTwo[b]
        b = listB.replace(",", "")
        groupB.append(b)
    groupC = []
    for c in range(len(noDupesResult)):
        listC = noDupesResult[c]
        c = listC.replace(",", "")
        groupC.append(c)

    # Comando para dar print dos conjuntos finais e do resultado:
    print("União: conjunto 1",'{',','.join(groupA),"}",", conjunto 2",'{',','.join(groupB),"}", ". Resultado:", '{',','.join(groupC),"}")



# Função para realizar a operação de diferença de conjuntos:
def diference(vectorOne, vectorTwo):

    # Comandos para retirar elementos repetidos de um conjunto:
    noDupes = []
    for i in vectorOne:
        if i not in noDupes:
            noDupes.append(i)
    noDupesTwo = []
    for i in vectorTwo:
        if i not in noDupesTwo:
            noDupesTwo.append(i)

    # Comandos para obter o resultado da operação desejada:
    result = []
    for i in vectorOne:
        if i not in vectorTwo:
            result.append(i)
    for x in vectorTwo:
        if x not in vectorOne:
            result.append(x)

    # Comandos para retirar vírgulas das listas:
    groupA = []
    for a in range(len(noDupes)):
        listA = noDupes[a]
        a = listA.replace(",", "")
        groupA.append(a)
    groupB = []
    for b in range(len(noDupesTwo)):
        listB = noDupesTwo[b]
        b = listB.replace(",", "")
        groupB.append(b)
    groupC = []
    for c in range(len(result)):
        listC = result[c]
        c = listC.replace(",", "")
        groupC.append(c)

    # Comando para dar print dos conjuntos finais e do resultado:
    print("Diferença: conjunto 1", '{', ','.join(groupA), "}", ", conjunto 2", '{', ','.join(groupB), "}", ". Resultado:", '{', ','.join(groupC), "}")



# Função para realizar a operação de interseção de conjuntos:
def intersection(vectorOne, vectorTwo):

    # Comandos para retirar elementos repetidos de um conjunto:
    noDupes = []
    for i in vectorOne:
        if i not in noDupes:
            noDupes.append(i)
    noDupesTwo =[]
    for i in vectorTwo:
        if i not in noDupesTwo:
            noDupesTwo.append(i)

    # Comandos para obter o resultado da operação desejada:
    result = []
    for i in noDupes:
        if i in noDupesTwo:
            result.append(i)

    # Comandos para retirar vírgulas das listas:
    groupA = []
    for a in range(len(noDupes)):
        listA = noDupes[a]
        a = listA.replace(",", "")
        groupA.append(a)
    groupB = []
    for b in range(len(noDupesTwo)):
        listB = noDupesTwo[b]
        b = listB.replace(",", "")
        groupB.append(b)
    groupC = []
    for c in range(len(result)):
        listC = result[c]
        c = listC.replace(",", "")
        groupC.append(c)

    # Comando para dar print dos conjuntos finais e do resultado:
    print("Interseção: conjunto 1", '{', ','.join(groupA), "}", ", conjunto 2", '{', ','.join(groupB), "}", ". Resultado:", '{', ','.join(groupC), "}")


# Função para realizar a operação de plano cartesiano de conjuntos:
def cartesianPlane(vectorOne, vectorTwo):

    # Comandos para retirar elementos repetidos de um conjunto:
    noDupes = []
    for i in vectorOne:
        if i not in noDupes:
            noDupes.append(i)
    noDupesTwo = []
    for i in vectorTwo:
        if i not in noDupesTwo:
            noDupesTwo.append(i)

    # Comandos para obter o resultado da operação desejada:
    result = []
    for i in range(len(noDupes)):
        for x in range(len(noDupesTwo)):
            vector = []
            vector.append(vectorOne[i])
            vector.append(vectorTwo[x])
            result.append(vector)

    # Comandos para retirar vírgulas das listas:
    groupA = []
    for a in range(len(noDupes)):
        listA = noDupes[a]
        a = listA.replace(",", "")
        groupA.append(a)
    groupB = []
    for b in range(len(noDupesTwo)):
        listB = noDupesTwo[b]
        b = listB.replace(",", "")
        groupB.append(b)
    groupC = []
    for c in range(len(result)):
        listC = result[c]
        c = listC.replace(",", "")
        vectorC.append(c)
        vectorCC = ','.join(vectorC)
        vectorCCC = []
        vectorCCC.append(vectorCC)
    groupC.append(vectorCCC)

    # Comando para dar print dos conjuntos finais e do resultado:
    print("Produto cartesiano: conjunto 1", '{', ','.join(groupA), "}", ", conjunto 2", '{', ','.join(groupB), "}", ". Resultado:", groupC)

# Comandos para ler a matriz e identificar as operaçoes desejadas:
for i in range(len(matriz)):
        if matriz[i][0] == "U":
           union(matriz[i + 1], matriz[i + 2])
        if matriz[i][0] == "D":
            diference(matriz[i + 1], matriz[i + 2])
        if matriz[i][0] == "I":
            intersection(matriz[i + 1], matriz[i + 2])
        if matriz[i][0] == "C":
            cartesianPlane(matriz[i + 1], matriz[i + 2])

