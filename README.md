# Metodo Burbuja-PCI
Samantha Erin Medina Muñoz A01712495

#Si puediera revisar practicamente todo (planteo de la situacion, creacion del repositor, operadores aritmeticos, funciones, condicionales, ciclo for, listas, comentarios, normas) en este caso no utilice ni matrices

Avance 1: Selecciona un tema para tu proyecto y setup de repositorio Describe su contexto y porque crees que es interesante. Escribe un algoritmo que describa tu proyecto.

¿Qué juego puedes hacer para ayudar a mantener las capacidades cognitivas?

	Utilizando el método burbuja se generan números aleatorios donde el usuario tendrá que ordenarlos para pasar el nivel o concluir el juego.

¿Qué características debe tener un juego para que sea útil para estos propósitos?

	El juego debe de ser simple para que el usuario no se estrese ni pierda el interés, el objetivo principal es aumentar los tiempos de concentración y observación del usuario. 

¿Te gustaría inventar un juego nuevo? O ¿hacer un programa que permita jugar algún juego que ya conozcas y que pueda ser utilizado para fortalecer las habilidades cognitivas? Piensa en algo que te guste jugar, algún juego para el que tengas que pensar en estrategias para ganar. ¿Serviría para este objetivo?
	
 	Si me gustaría, creo que le podría agregar mas cosas a este primer boceto. A mi en lo particular me fascina jugar sudoku por lo que estoy basando mi juego en un juego de números. 
 
# Ordenamiento de Burbuja: 
# Contexto: 
Hoy en día se ha demostrado que las personas han perdido la capacidad para concentrarse debido al uso excesivo de aparatos electrónicos que los mantienen entretenidos por horas y que gracias a la manera en que funcionan estos están constantemente presentándonos publicaciones o interacciones de nuestro interés con satisfacción instantánea.

No solamente eso, al mismo tiempo se ha demostrado que el aprendizaje de las matemáticas interactivas ayuda a fomentar el desarrollo de pensamiento lógico a cualquier edad pero especialmente para los niños. 

Con este proyecto se pretende hacer que el usuario desarrolle un nivel de atención más extenso mientras juega un juego sencillo y evite el estrés, esto por medio de la música, los visuales y las vibraciones de su aparato. 
	
# Algoritmo: 

1.(inicio) Al abrir el programa se le presenta al usuario una serie de números aleatorios 

2.Se le pide al usuario ordenar los números de menor a mayor 

3.El usuario ingresa los números (separados por comas) 

4.Una vez terminado y con la ayuda del método de ordenamiento burbuja el programa mostrará los resultados. El método burbuja funciona de la siguiente manera: 

	i.el programa hace varias pasadas a la lista de números
 	ii.los compara 
  	iii.los va cambiando de orden hasta que la lista quede completa de menor a mayor  

5.Al momento de comparar los resultados:

	i.Si el usuario obtiene todas las respuestas bien será recompensado con puntos y se le preguntará si quisiera seguir jugando
	ii.Si el usuario responde que sí a la pregunta se le mostrar una secuencia más complicada 
	iii.Si el usuario responde que no o sale del programa el programa se cerrará (fin)
	iv.Si el usuario no obtiene la secuencia correcta se le mostrará una secuencia similar (o con el mismo nivel de dificultad) 
	v.Si el usuario teclea alguna letra, un dígito incorrecto o no separa con comas se le marcara error y tendrá que corregir

*Como dijimos anteriormente este programa seguirá corriendo en loop hasta que sea cerrado por el usuario.*

# Avance 2: Escribir los operadores que utilizara el programa 

	Primero le debemos de mostrar la secuencia de numeros aleatorios al usuario y le pediremos que los ordene
print('Ordene la siguiente secuencia:')

	Para los numeros aleatorios utilizaremos el randrange(a, b, salto) que es una funcion que nos dara diferentes numeros aleatorios entre a y b y salto es el numero de numeros que van a tener de diferencia, lo empezaremos del 1 al 100 saltandose 3 asi ns dara un numero par y uno impar.

secuencia=(randrange(1, 100, 3))

 	La de arriba es nuestra variable donde se produce el numero aleatorio
 
print(secuencia)

Entrada 

	Se busca que el usuario introduzca la secuencia de numeros ya ordenadas, a esta linea se le conocera com linea a y se vera algo asi:

 a=inp(input('Porfavor ingrese su respuesta'))

Proceso

	Ahora para el proceso se va a tener que utilizar 2 buclees para reorganizar a, podriamos tmabien reorganizar la secuencia original pero me parece mas rapido arreglar el numero insertado por el usuario para poder comprobarlo.

 	i=al recorrido o la iteracion y se va a ir acumulando

  	p=es el bucle o iteracion que se va a encargar de analizar los numeros y los va a ir cambiando los numeros

   	n=son las 


while(a>1)

	En la primera linea me refiero a que mientras el primer elemento de a sea mayor que 1 el programa va a seguir corriendo
 
 for i (n-1)

	primer bucle
 
        for p (n-1-i)

	segundo bucle 

	    if (p) > (p+1)

	comparacion
	
		(p), (p+1) = (p+1), (p)

Salida

A

 	Se desea que se muestre el resultado final al usuario


	Considero que estos son los operadores que voy a estar utilizando para el trabajo sin embargo es posible que cambien o aumenten si le deseo poner animacion, sonidos, movimiento etc. al proyecto.


 # Avance3

	Considero que las funciones que tengo ahorita son suficientes por el momento, una vez que pruebe el programa decidire si es necesario agregar o quitar funciones. 

 # Avance 4 y 5 (para el 5 solo cambie un while por el for)

 numeros_preselectos = [6, 12, 20, 53, 62, 22, 13, 9, 0] # numeros preselectos

print('Numeros seleccionados:', numeros_preselectos) # se presentan los numeros preselectos 

booleano = False # variable con un valor boooleano falso que si entra en el if sigue estando desordenado
while booleano == False: # repetir esto n veces mientras la bandera o la variable bandera sea falso
    booleano = True # dejara de marcar falso cuando deje de entrar en el if
    for i in range(len(numeros_preselectos)-1): # para que i tenga la posicion designada por posicion (menos 1 por comparacion)
        if numeros_preselectos[i] > numeros_preselectos[i + 1]: # si la lista del elemento que estas iterando es mayor al elemento de la lista entras a la condicion
            aux = numeros_preselectos[i] # la variable aux va a guaradar el valor dle elemento anterior para que no lo perdamos
            numeros_preselectos[i] = numeros_preselectos[i+1] # si es asi necesito que hagas el intercambi del valor del elemento a la derecha
            numeros_preselectos[i + 1] = aux # el elemetno a la derecha del que se esta iterando actualmente va a avaler aux pq es el valor mas grande, el original
            booleano = False # sigue estando desordenado

print('Numeros ordenados:', numeros_preselectos) # mostrara los valores ordenados

# Necesito encontrar una manera de que el programa cree la lista de numeros random y de ahi que ya inicie el programa
 
# Referencias: 
Libiano, J. E. (2022, March 23). Las capacidades cognitivas: qué son, tipos, funcionamiento y estimulación. Nueron Up. https://www.neuronup.com/estimulacion-y-rehabilitacion-cognitiva/las-capacidades-cognitivas-que-son-tipos-funcionamiento-y-estimulacion/
G, R. (2019, August 19). Estudio afirma que juegos de lógica en línea ayudan a reducir la declinación cognitiva asociada a la vejez. Peru21 G21. https://g21.peru21.pe/respuestas/viral-youtube-juegos-logica-linea-extienden-juventud-cognitiva-personas-avanzada-edad-estudio-estados-unidos-espana-mexico-colombia-argentina-yt-yutube-ciencia-nnda-nnrt-video-497378-noticia/
5.7. El ordenamiento burbuja — Solución de problemas con algoritmos y estructuras de datos. (n.d.). https://runestone.academy/ns/books/published/pythoned/SortSearch/ElOrdenamientoBurbuja.html
Primaria, M. (2022, February 2). Juegos de ordenar y colocar para niños online y gratis. Mundo Primaria. https://www.mundoprimaria.com/juegos-educativos/juegos-de-memoria-infantiles/juegos-de-ordenar#:~:text=Los%20juegos%20de%20ordenar%20para,y%20la%20monitorizaci%C3%B3n%20y%20control.
Mendoza, M. C. V. (2023, January 19). El desarrollo de la inteligencia lógico matemático mediante el juego en niños de educación inicial. https://dominiodelasciencias.com/ojs/index.php/es/article/view/3155
J2logo. (2022, January 16). Generar números aleatorios en Python. Funciones principales. J2LOGO. https://j2logo.com/python/generar-numeros-aleatorios-en-python/
Amorin, D. (2023). Ordenamiento de Burbuja en Python. Diego Amorin. https://diegoamorin.com/ordenamiento-burbuja-python/
Bustamante, S. J. (2021). Guía de funciones de Python con ejemplos. freeCodeCamp.org. https://www.freecodecamp.org/espanol/news/guia-de-funciones-de-python-con-ejemplos/
