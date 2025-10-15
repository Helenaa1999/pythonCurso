"""Enunciado: declaramos variables con nombres descriptivos, calculamos el precio final con IVA y formateamos una cadena de salida."""

IVA = 21
precio_base = 120.0

calculadora_Iva = (precio_base * IVA)/100
precio_final = calculadora_Iva + precio_base;
print(f"El IVA del producto es de {calculadora_Iva} euros. Precio final {precio_final}")