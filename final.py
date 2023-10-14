import random #importamos el modulo random para generar los numeros random

def genera_lista_random(tamaño): #definimos la funcion que nos ayudara a generar los numeros random usando una variable de tama;o 
    return[random.randint(0, 100) for _ in range(tamaño)] #nos va a devolver una lista de numeros del 0 al 100 con el tama;o que especificaremos mas adelante

def metodo_burbuja(lista): #definimos la funcion del metodo burbuja y le agregamos la variable lista donde se almacenaran los valores
    numero = len(lista) #el numero es igual a los valores dentro de dicha lista
    for i in range(numero): #para que i tenga la posicion designada por el tama;o del numero
        for j in range(0, numero - i - 1): #para que j tenga la posicion designada en el rango de 0 y la posicion de i menos 1 por comparacion)
            if lista[j] > lista[j + 1]: 
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def main():
    tamaño = 7
    numeros_random = genera_lista_random(tamaño)

    print("¡Bienvenido a este pequeño juego!")
    print(f"Deacuerdo a la siguiente lista: {numeros_random}") 

    numeros_acomodados = numeros_random.copy()
    metodo_burbuja(numeros_acomodados)

    respuesta_usuario = input("Ingrese los numero de menor a mayor con una coma y un espacio entre cada uno: ")
    acomodo_usuario = list(map(int, respuesta_usuario.split(',')))

    if acomodo_usuario == numeros_acomodados:
        print("La respuesta correcta es:", numeros_acomodados) #mostrara los valores ordenados
        print("¡Felicidades pasaste el juego!")
    else:
        print("Lo siento tu arreglo no es correcto. La respuesta correcta es: ", numeros_random)
        
if __name__ == "__main__":
    main()
