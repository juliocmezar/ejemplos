vector = ["casa","perro","gato","lobo"]

def imprimir(): 
 for x in vector:
     print(x, end = " - ")

for i in range(len(vector)):
    print(vector[i])  

# agregar al final
vector.append(0)

imprimir()

#print(vector)

#borrar por posicion
vector.pop(0)

print(vector)

#borrar por valor de elemento
vector.remove("gato")

print(vector)

#sabar cuantas posiciones tiene el vector
print(len(vector))

#añadir varios elementos
vector.extend(["juan", "pedro"])

print(vector)


matriz = [[1,4,6],[4,8,7]]

print(matriz)

print(len(matriz))

print(matriz[0])