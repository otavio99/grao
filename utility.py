print("Para o cálculo de rentabilidade, é considerado que:")
print(">>> a Taxa Selic seja de 4,25% ao ano")
print(">>> é pago 100% da Taxa Selic")
print(">>> só é rentabilizado os dias úteis")
print(">>> os impostos sobre os investimentos serão desconsiderados")

t = 36
i = 4.25/100

p = float(input("Valor do investimento semanal: "))
#36 semanas
p = p*36

m = p *(1+i)**t/252



print("Rendimento: {:.2f}".format(m))
print("Ganho total: {:.2f}".format(m+p))
