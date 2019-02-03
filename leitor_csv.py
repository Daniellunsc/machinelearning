import csv


def load_csv_acesso():
    dados = []
    marcacoes = []

    arquivo = open("acesso.csv", "rt")
    leitor = csv.reader(arquivo)
    next(leitor)
    for acessou_home, acessou_como_funciona, acessou_contato, comprou in leitor:
        dados.append([int(acessou_home), int(acessou_como_funciona), int(acessou_contato)])
        marcacoes.append(int(comprou))

    return dados, marcacoes


def load_csv_busca():
    X = []
    Y = []

    arquivo = open("busca_cursos.csv", "rt")
    leitor = csv.reader(arquivo)
    next(leitor)
    for home, busca, logado, comprou in leitor:
        dado = [int(home), busca, int(logado)]
        X.append(dado)
        Y.append(int(comprou))

    return X, Y
