#numbers
2 + 2
50 - 5 * 6
8 / 5
# float= 1.1
# int= 1
17 / 3 # devuelve el numero con decimales
17 // 3 # devuelve el numero entero sin los decimales
17 % 3 # devuelve el sobrante de la division
5 ** 2 # devuelve como potencia
width = 20
height = 5 * 9
width * height
# el = asigna valores a las variables

#strings
'hola mundo'
"hola mundo"
'2001'
# se puede hacer tanto con comillas simples y dobles,
# los numeros entre comillas se convierten en un string
'marco\'s' # el "\" se utiliza antes de una comilla simple para que aparezca como string
"marco's" # otra forma es utilizando comillas dobles solamente
# otros ejemplos son
'"yes," they said'
"\"yes,\" they said"
'"Isn\'t," they said'

#funcion print()
s = 'primera linea.\nsegunda linea.'
print(s)
# para evitar que los caracteres precedidos por "\" se interpreten como caracteres especiales,
# puedes usar cadenas sin formato agregando una "r" antes de la comilla simple
print('marco\narco')
print(r'marco\narco')
# Las cadenas de texto literales pueden contener múltiples líneas.
# Una forma es usar triples comillas: """...""" o '''...'''.
# Los fin de línea son incluidos automáticamente,
# pero es posible prevenir esto agregando una "\" al final de la línea.
print("""\
    opciones:
    -1          tirarse peos
    -2          hacer kk
""")
#Los strings se pueden concatenar con el operador "+" y se pueden repetir con "*"
3 * 'un' + 'peo'
# dos o mas cadenas literales(es decir, las encerradas entre comillas)
# una al lado de la otra se concatenan automáticamente.
'mar' 'co'
#Esta característica es particularmente útil cuando quieres dividir cadenas largas:
text = ('Marco garcia de los llanos '
        'Catalina marquez de los escobar')
print(text)
# Esto solo funciona con dos literales, no con variables ni expresiones
# Si quieres concatenar variables o una variable y un literal, usa +
text + 'thon'
# los strings se pueden indexar(subindices) el primer caracter es 0
text = 'Python'
text[0]
text[5]
#Los índices también pueden ser números negativos, para empezar a contar desde la derecha
text[-1]
text[-2]
# las rebanadas(slicing), rebanar te permite obtener una subcadena
text[2:5] #caracteres desde la posicion 2 (incluido) to 5 (excluido)
text[0:2] #caracteres desde la posicion 0 (incluido) to 2 (excluido)
