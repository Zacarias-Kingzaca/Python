def aumentar(n = 0, taxa = 0, formato=False):
    res = n + (n * taxa / 100)
    return res if formato is False else moeda(res)

def diminuir(n = 0, taxa = 0, formato=False):
    res = n - (n * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(n  = 0, formato=False):
    res = n * 2
    return res if formato is False else moeda(res)


def metade(n  = 0, formato=False):
    res = n / 2
    return res if formato is False else moeda(res)


def moeda(n = 0):
    res = f"{n:.2f}"
    return res

def moeda(n = 0, moeda = "Kzs "):
    return f"{moeda}{n:.2f}".replace(".", ",") 

def resumo(n=0, taxaa=10, taxar=5):
    print("-" * 30)
    print("{:^30}".format("RESUMO DE VALOR"))
    print("-" * 30)
    print(f"Preço analisado: \t{moeda(n)}")
    print(f"Dobro do preço:  \t{dobro(n, True)}")
    print(f"Metade do preço: \t{metade(n, True)}")
    print(f"{taxaa}% de aumento: \t{aumentar(n, taxaa, True)}")
    print(f"{taxar}% de redução: \t{diminuir(n, taxar, True)}")