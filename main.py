"""
Inserta el encabezado aquí y escribe tu código abajo


# Declaraciones
CONSTANTE = valor

# Entradas
entrada = input()

# Proceso


# Salidas
print(salida)
"""


# Entradas
vtas_lun = eval(input("Introduzca las ventas del lunes: "))
vtas_mar = eval(input("Introduzca las ventas del martes: "))
vtas_mie = eval(input("Introduzca las ventas del miércoles: "))
vtas_jue = eval(input("Introduzca las ventas del jueves: "))
vtas_vie = eval(input("Introduzca las ventas del viernes: "))

# Proceso
total = vtas_lun + vtas_mar + vtas_mie + vtas_jue + vtas_vie;
if total <= 20000:
    comision = total * 0.05
else:
	comision = total * 0.06

# Salidas
print("Ventas totales:", total)
print("Comisión:", comision)
