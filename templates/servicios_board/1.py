

class personas():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


persona1 = personas(input("ingrese nombre: "),int(input("ingrese edad: ")))
entrada= input("queres consultar cliente? s/n ? ")
if entrada == "s":
    print(persona1.nombre)
    print(persona1.edad)
else:
    "bla bla"


