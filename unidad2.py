'''
1)Crear unprograma que le solicite al usuario un entero y lo imprima por pantalla.
 Recordá que podés usar las funciones input (para solicitar información) y print para mostrar
 información.
'''
num=int(input('Ingrese un n°:'))
print(num)

'''
2)Crear un programa que le solicite al usuario dos números enteros y luego imprima por pantalla:
 ● lasumadeambosnúmeros
 ● larestadeambosnúmeros
 ● lamultiplicación de ambos números
 ● ladivisión entera de ambos números
 ● elresto
'''
num1=(input('Ingrese un primer n°:'))   #no le agregué el tipo de dato int porque sino no me tomaba los operadores
num2=(input('Ingrese un segundo n°:'))
operador=input('Ingrese un operador (+- * / // % ):')
sumatoria=eval(num1+operador+num2)
print(sumatoria)

'''
3)Crear unprograma que le solicite al usuario un entero y determine si es par, mostrando por pantalla un
 mensaje que indique el resultado.
 Para determinar si un número es par o impar, se puede determinar con el uso del operador %, les
 dejamos a ustedes el cómo.
'''

numb = int(input('Ingrese un n°: '))     
if numb % 2 != 0:
    print('El n° es impar.')
else:
    print('El n° es par')



'''
4)Escribir un programa que le pida a un usuario su año de nacimiento y otro año, y le diga qué edad tenía
 el usuario en el año ingresado.
'''
edad=int(input('Ingrese su año de nacimiento:'))
anio=int(input('Ingrese un año cualquiera:'))
edad_usuario= anio - edad
print('Usted tenía ',edad_usuario, 'años de edad')

'''
5)Crear unprograma que le solicite al usuario 5 enteros y muestre por pantalla el promedio de ellos.
 Es muy común usar variables para acumular valores
'''
suma = 0
for i in range(5):
    numero = int(input(f"Ingrese 5 n° enteros {i + 1}: "))
    suma += numero        
    promedio = suma / 5
    print("El promedio de los números ingresados es:", promedio)

'''
6)Crear una función que reciba un número y muestre el anterior y el siguiente.
'''

'''
7)Crear una función que una un string y un entero, ambos dentro de un string.
'''

'''
8)Crear una función que reciba un entero y que retorne (devuelva) el resto y el cociente.
'''

'''
9)Pedirle nombre y apellido por separado e imprimir “Apellido, Nombre”.
 Este proceso se llama concatenar cadenas.
'''

'''
10)Obtener una palabra e imprimir la cantidad de letras.
'''


'''
11) Obtener una palabra e imprimir los primeros 5 caracteres (pista: slicear la palabra)
'''


'''
12)Obtener una palabra, borrarle todas las ‘a’ e imprimirla por pantalla (pista: usar una función predefinida
 de Python)
'''
