print("Para o cálculo de rentabilidade, é considerado que:")
print(">>> a Taxa Selic seja de 4,25% ao ano")
print(">>> é pago 100% da Taxa Selic")
print(">>> só é rentabilizado os dias úteis")
print(">>> os impostos sobre os investimentos serão desconsiderados")

t = 4.25
i = t/100

p = float(input("Valor do investimento semanal: "))
#36 semanas
p = p*36

m = p * (1+i)**t/252

resultadoFinal = m * p

print("{:.2f}".format(resultadoFinal))