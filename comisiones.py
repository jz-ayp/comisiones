"""
Cálculo de comisiones
"""

# Entradas
lu, ma, mi, ju, vi = [float(input(f"Ventas del {dia}: ")) for dia in ("lunes", "martes", "miércoles", "jueves", "viernes")]

# Proceso
total = sum((lu, ma, mi, ju, vi))
if total <= 20_000:
    tasa = 0.05
else:
    tasa = 0.06
comision = tasa * total

# Salidas
print("Comisión:", comision)
