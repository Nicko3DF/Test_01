'''
# Clase

# En python es necesario que la 1ra letra sea mayus
class Auto:
    marca = ''
    modelo = 0
    Placa = ''

# Ya esta la 1ra clase creada
# Ahora hay que añador objetos

# Asi le pone asignamos la clase de auto al objeto creado
taxi = Auto()
print(taxi.modelo)


## -------- ## Clases y objetos ## -------- ##
# no es necesario colocar (object)
class persona(object):
    doctor = "Victor"

# para ingresar al valor de doctor, es necesario "pasar" por la clase

print(persona.doctor)

'''
## ----------------------

class jugadores_A:
    j1 = "Metabee"
    j2 = "Rokusho"

class jugadores_B:
    j3 = "Rexona"
    j1 = "Salo"

print(jugadores_B.j1)

'''
No necesariamente los objetos (lo que esta dentro de la
clase) deben de iniciarse altiro, pueden iniciase despues
(crear los objetos aparte)
'''

class nombre:
    pass
# con pass nos "skipeamos" esto para que no de error

victor = nombre()
maria = nombre()

'''
A las caracterisiticas del objeto, se le denominan 
"atributos" y debemos de agregarle los atributos a los objetos

se hace mediante
objeto.atributo = valor
ejemplo
victor.tamaño = 180
'''

victor.edad = 30
victor.sexo = "masculino"
victor.pais = 'bolivia'

maria.edad = 25
maria.sexo = 'femenino'
maria.pais = 'colombia'

print("%%%%%%%%%%")
print(victor.edad)
print(victor.sexo)
print(victor.pais)
print("%%%%%%%%%%")

## -------- ## Metodos ## -------- ##

