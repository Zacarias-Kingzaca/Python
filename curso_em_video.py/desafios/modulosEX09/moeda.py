def aumentar(n = 0, taxa = 0, formato=False):
    res = n + (n * taxa / 100)
    return res if formato is False else moeda(n)

def diminuir(n = 0, taxa = 0, formato=False):
    res = n - (n * taxa / 100)
    return res if formato is False else moeda(n)


def dobro(n  = 0, formato=False):
    res = n * 2
    return res if formato is False else moeda(n)


def metade(n  = 0, formato=False):
    res = n / 2
    return res if formato is False else moeda(n)


def moeda(n = 0):
    res = f"{n:.2f}"
    return res

def moeda(n = 0, moeda = "Kzs "):
    return f"{moeda}{n:.2f}".replace(".", ",") 