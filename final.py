import random #importamos el modulo random para generar los numeros random

def genera_lista_random(tamaño): #definimos la funcion que nos ayudara a generar los numeros random usando una variable de tama;o 
    return[random.randint(0, 100) for _ in range(tamaño)] #nos va a devolver una lista de numeros del 0 al 100 con el tama;o que especificaremos mas adelante

def metodo_burbuja(lista, booleano): #definimos la funcion del metodo burbuja y le agregamos la variable lista donde se almacenaran los valores
      numero = len(lista) #le asignamos a la variable numero la longitud de lo qu se ponga en la lista
    for i in range(numero): #utilizamos for ya que no sabemos cuantas pasadas a la lista tendremos que hacer dentro del rango de numero
        for j in range(0, numero - i - 1): #para limitar el ciclo usamos que pase de 0 hasta el numero menos la posicion menos 1 asegurando que el numero mas grande sea el ultimo
            if lista[j] > lista[j + 1]: #checamos que dentro del ciclo el index j sea mayor que j + 1
                lista[j], lista[j + 1] = lista[j + 1], lista[j] #si esto es verdad los cambiara de lugar asegurando que se acomoden de menor a mayor

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
