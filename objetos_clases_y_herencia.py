#Como crear una clase en python
class  Usuario:
    nombre = "Felipe"
    apellido = "Feliz"

usuario = Usuario
usuario2 = Usuario
print(usuario) #Al imprimirlo asi nos da el sig texto : <class '__main__.Usuario'>
print(usuario.nombre, usuario2.apellido) # Al especificar su nombre hacemos que nos proporcione unicamente "Felipe"

#Una alternativa para no asignar nombres directamente en la clase seria de

class User:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print('Hola, mi nombre es: ', self.nombre, self.apellido)
        
user1 = User('Felipe','Feliz')
user2 = User('Chanchito','Feliz')
user1.saludo()
print(user1.nombre, user2.nombre)

#RESUMEN
#Las clases son el molde de lo que vamos a hacer
#Los objetos son instancias de los planos o productos salidos del molde

#__init__ se ejecuta siempre que tengamos una instancia de la clase
#self hace referencia a una instancia que nosotros creemos, pudiendo cambiar los valores de las propiedades de las instancias
# no es necesario enviar self como parametro al crear una instancia de la clase

#METODOS
# vease ejersicio mas arriba para ejemplo
user1.saludo()
user2.saludo()

#NOTA IMPORTANTE
# No es necesario que el self se llame de esa manera, algunos lenguajes usan this, pero en python
# no es necesario, ya que python lo reconoce como self aun si le cambiamos el nombre por otro.
# aunque se recomienda que se llame de esa manera para evitar confusiones
"""
#Ejemplo
class User:
    def __init__(lala,nombre,apellido):
        lala.nombre = nombre
        lala.apellido = apellido

    def saludo(lala):
        print('Hola, mi nombre es: ', lala.nombre, lala.apellido)
"""
