def lista_numeros()
lista = [] #la lista de numeros que se va a usar
while lista < 7 #mientras los valores de lista no sena mayores o iguales a 7 se van a generar mas numeros
    for contador in range (0, 101): #del 0 al 101 se generaran numeros
        num_random = () 
        lista = num_random #se van acumulando en lista

numeros_preselectos = [6, 12, 20, 53, 62, 22, 13, 9, 0] #lista de /numeros preselectos

print('Numeros seleccionados:', numeros_preselectos) #se presentan los numeros preselectos 

booleano = False #variable con un valor boooleano falso que si entra en el if sigue estando desordenado
while booleano == False: #repetir esto n veces mientras la bandera o la variable bandera sea falso
    booleano = True #dejara de marcar falso cuando deje de entrar en el if
    for i in range(len(numeros_preselectos)-1): #para que i tenga la posicion designada por posicion (menos 1 por comparacion)
        if numeros_preselectos[i] > numeros_preselectos[i + 1]: #si la lista del elemento que estas iterando es mayor al elemento de la lista entras a la condicion
            guardado = numeros_preselectos[i] #la variable aux va a guaradar el valor dle elemento anterior para que no lo perdamos
            numeros_preselectos[i] = numeros_preselectos[i+1] #si es asi necesito que hagas el intercambi del valor del elemento a la derecha
            numeros_preselectos[i + 1] = guardado #el elemetno a la derecha del que se esta iterando actualmente va a avaler aux pq es el valor mas grande, el original
            booleano = False #sigue estando desordenado

print('Numeros ordenados:', numeros_preselectos) #mostrara los valores ordenados
