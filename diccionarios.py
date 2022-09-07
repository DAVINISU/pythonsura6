# los diccionarios son variables especiales que me permiten almacenar, multiples datos de diferente tipo en una sola variable.

empleado = {
    'nombre' : "Juan",
    'Edad'   : 28,
    'Cargo'  : "Analista de datos",
    'Salario': 8000000,
    'horasTrabajadas' : 40,
    'aplicaSubsidioTransporte':False,
    'deudas' :[1500000,800000]
}

# print(empleado)
# print(empleado['nombre'])
# print(empleado['deudas'][1])


#recorriendo un diccionario:

for observadorAtributo, observadorValor in empleado.items() :
    print(observadorAtributo)
    print(observadorValor) 