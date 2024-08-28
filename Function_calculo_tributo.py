preco = 1500
custo = 400
lucro = 800

def carga_tributaria(preco, custo, lucro):
    imposto = preco - custo - lucro
    return imposto / preco

print(f'A Carga tributária foi de: {carga_tributaria(preco, custo, lucro):.1%}')