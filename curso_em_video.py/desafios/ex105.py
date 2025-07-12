from os import system
system("cls")
print()

def notas(*n,  sit=False):
    """
    ->  Função para analisar notas e situações de vários alunos.

    n = Uma ou mais nota dos alunos (aceita várias)
    sit = Valor opcional, mostra se deve ou não mostrar a situaçõa
    return = Dicionário com várias informações de situações
    """
    r = dict()

    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'Boa'
        elif r['média'] >= 5:
            r['situação'] = 'Razuável'
        else:
            r['situação'] = 'Mal'
        return r
    return r

res = notas(1, 1, 6, sit=True)
print(res)
help(notas)