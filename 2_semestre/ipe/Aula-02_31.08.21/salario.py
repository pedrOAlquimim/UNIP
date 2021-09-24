fixo = 998
comissao = 0.05
venda = 48995
cm = 22.45
inss = 0.08

salarioB = (fixo + (venda * comissao))
salarioL = salarioB - ((salarioB * inss) + (cm))
print('R$', salarioL)