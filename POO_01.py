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

'''
Notar que, en el primer caso, para acceder a un elemento, fue 
necesario colocar "Clase.objeto", pues en dicha oportunidad
se creo primero la clase con todos los objetos, en cambio
en el 2do caso, se creo un "molde vacio" y luego se agregaron
atributos a los objetos y ahi radica la diferencia en
como se accede a dichos elementos
'''


## -------- ## Metodos ## -------- ##

'''
Metodo es:
- Funcion dentro de una clase
- Determina una accion o comportamiento (y se crean nombres
acorde a eso)
- Self ayuda a referirse al mismo objeto
'''

class Matematica:

    def suma(self):

        self.n1 = 2
        self.n2 = 3

s = Matematica()

#El objeto s usara el metodo suma
s.suma()
print(s.n1 + s.n2)

'''
El init ayuda a colocar los atributos cuando se inicia
el objeto, evitando asi los problemas de "setear" 
manualmente linea a linea los valores, se recuerda que antes
se hizo

victor = nombre()
.
.
.
victor.edad = 30
victor.sexo = "masculino"
victor.pais = 'bolivia'

con el init se pasa al metodo ("funcion"), directamente
los parametros o atributos (caracteristicas del objeto)

'''

class Ropa:
    def __init__(self):
        self.marca = 'willow'
        self.talla = 'M'
        self.color = 'rojo'

camisa = Ropa()

print(camisa.talla)

class Calculadora:

# Asi le decimos que el metodo trabajara con las variables
# auxiliares n1 y n2
    def __init__(self,n1,n2):
        
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.multiplicacion = n1 * n2
        self.division = n1 / n2
    
operacion = Calculadora(2,3)

print(operacion.suma)