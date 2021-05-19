print("Para o cálculo de rentabilidade, é considerado que:")
print(">>> a Taxa Selic seja de 4,25% ao ano")
print(">>> é pago 100% da Taxa Selic")
print(">>> só é rentabilizado os dias úteis")
print(">>> os impostos sobre os investimentos serão desconsiderados")
print(">>> serão considerados 36 semanas para o investimento")
print(">>> O investimento realizado seja de R$ 100,00") 

t = 36
i = 4.25/100
p = 100.00

#36 semanas
p = p*36

m = p *(1+i)**t/252


print("Rendimento: {:.2f}".format(m))
print("Valor total: {:.2f}".format(m+p))
