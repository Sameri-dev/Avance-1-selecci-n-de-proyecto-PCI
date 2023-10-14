import random #importamos el modulo random para generar los numeros random

def genera_lista_random(tamaño): #definimos la funcion que nos ayudara a generar los numeros random usando una variable de tama;o 
    return[random.randint(0, 100) for _ in range(tamaño)] #nos va a devolver una lista de numeros del 0 al 100 con el tama;o que especificaremos mas adelante

def metodo_burbuja(lista, booleano): #definimos la funcion del metodo burbuja y le agregamos la variable lista donde se almacenaran los valores
    booleano = False #variable con un valor boooleano falso que si entra en el if sigue estando desordenado

    while booleano == False: #repetir esto n veces mientras la bandera o la variable bandera sea falso
        booleano = True #dejara de marcar falso cuando deje de entrar en el if
        for i in range(len(lista)-1): #para que i tenga la posicion designada por posicion (menos 1 por comparacion)
            if lista[i] > lista[i + 1]: #si la lista del elemento que estas iterando es mayor al elemento de la lista entras a la condicion
                guardado = lista[i] #la variable aux va a guaradar el valor dle elemento anterior para que no lo perdamos
                lista[i] = lista[i + 1] #si es asi necesito que hagas el intercambi del valor del elemento a la derecha
                lista[i + 1] = guardado #el elemetno a la derecha del que se esta iterando actualmente va a avaler aux pq es el valor mas grande, el original
            booleano = False #sigue estando desordenado

def main():
    tamaño = 7 #Al fin le asignamos el tama;o de la lista
    numeros_random = genera_lista_random(tamaño) #

    print("¡Bienvenido a este pequeño juego!") #Le damos la bienvenida al programa la usuario
    print(f"Deacuerdo a la siguiente lista: {numeros_random}") #Mostramos la lista de numeros

    numeros_acomodados = numeros_random.copy() #guardamos la lista de numeros en numeros acomodados
    metodo_burbuja(numeros_acomodados) #y le aplicamos la funcion del metodo burbuja que ya hicimos

    respuesta_usuario = input("Ingrese los numero de menor a mayor con una coma y un espacio entre cada uno: ") #le pedimos ahora al usuario que acomode la lista que le mostramos
    acomodo_usuario = list(map(int, respuesta_usuario.split(','))) #aqui lo que hacemos es darle el mismo formato a la lista del usuario del que tenemos de la lista para poderlos comparar mas adelante

    if acomodo_usuario == numeros_acomodados: #comparamos y si lo que puso el usuario es lo mismo que lo que tenmos entonces
        print("La respuesta correcta es:", numeros_acomodados) #mostrara los valores ordenados
        print("¡Felicidades pasaste el juego!") #Y felicira al usuario
    else: #sino
        print("Lo siento tu arreglo no es correcto. La respuesta correcta es: ", numeros_random) #Le mostraremos la respuesta
        
if __name__ == "__main__": #curiosamente en mi investigacion me encontr con esta funcion la cual se supone que hace que al momento de correr el programa sea mas exacto (sobretos cuando corremos main) entonces decidi probarla
    main()
