import csv


def load_csv():
    dados = []
    marcacoes = []

    arquivo = open("acesso.csv", "rt")
    leitor = csv.reader(arquivo)
    next(leitor)
    for acessou_home, acessou_como_funciona, acessou_contato, comprou in leitor:
        dados.append([int(acessou_home), int(acessou_como_funciona), int(acessou_contato)])
        marcacoes.append(int(comprou))

    return dados, marcacoes
