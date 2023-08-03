#En el presente ejercicio se desea obtner 
#el precio final que se tine que pagar si 
#se aplica el 36% de desceunto del total 
#de la compra

total = float(input('Ingrese total : '))
descuento = total * 0.36
pagar = total - descuento

print(f"se debe de pagar : ${total}")
print(f"Su descuento es de : ${descuento:.2f}")
print(f"El total a pagar es de : ${pagar:.2f}")

