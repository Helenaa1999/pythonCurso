"""Enunciado: declaramos variables con nombres descriptivos, calculamos el precio final con IVA y formateamos una cadena de salida."""
from decimal import Decimal, getcontext

getcontext().prec = 10

IVA = Decimal("21")
precio_base = Decimal("120")

calculadora_Iva = (precio_base * IVA)/Decimal("100")
precio_final = calculadora_Iva + precio_base;

#Lo de 5f significa que quiero que muestre 5 decimales
print(f"El IVA del producto es de {calculadora_Iva:5f} euros. Precio final {precio_final:5f}")