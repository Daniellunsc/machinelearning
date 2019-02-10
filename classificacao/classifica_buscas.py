from collections import Counter
import pandas as pd

df = pd.read_csv('busca_cursos2.csv')

X_df = df[['home', 'busca', 'logado']]
Y_df = df['comprou']

Xdummies_df = pd.get_dummies(X_df)
Ydummies_df = Y_df

X = Xdummies_df.values
Y = Ydummies_df.values

porcentagem_treino = 0.8
porcentagem_teste = 0.1

tamanho_de_treino = int(porcentagem_treino * len(Y))
tamanho_de_teste = int(porcentagem_teste * len(Y))
tamanho_de_validacao = int(len(Y) - tamanho_de_treino - tamanho_de_teste)

treino_dados = X[0:tamanho_de_treino]
treino_marcacoes = Y[0:tamanho_de_treino]

fim_teste = tamanho_de_treino + tamanho_de_teste
teste_dados = X[tamanho_de_treino:fim_teste]
teste_marcacoes = Y[tamanho_de_treino:fim_teste]

validacao_dados = X[fim_teste:]
validacao_marcacoes = Y[fim_teste:]


def fit_and_predict(modelo, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes):
    modelo.fit(treino_dados, treino_marcacoes)

    return predict(modelo, teste_dados, teste_marcacoes)


def predict(modelo, dados, marcacoes):
    resultado = modelo.predict(dados)
    acertos = (resultado == marcacoes)
    total_de_acertos = sum(acertos)
    total_de_elementos = len(teste_dados)
    taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos
    print("Taxa de acerto do algoritmo: %f" % taxa_de_acerto)
    print("Total de elementos: ", total_de_elementos)
    print("================")
    return taxa_de_acerto


from sklearn.naive_bayes import MultinomialNB

modeloMultinomial = MultinomialNB()
print("NB")
multinomial = fit_and_predict(modeloMultinomial, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes)

from sklearn.ensemble import AdaBoostClassifier

modeloAdaboost = AdaBoostClassifier()
print("ADA")
adaboost = fit_and_predict(modeloAdaboost, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes)

if multinomial > adaboost:
    vencedor = modeloMultinomial
else:
    vencedor = modeloAdaboost

print("Vencedor")
resultado = predict(vencedor, validacao_dados, validacao_marcacoes)

# a eficácia do algoritmo que chuta tudo um único valor
acerto_base = max(Counter(validacao_marcacoes).values())
taxa_de_acerto_base = 100.0 * acerto_base / len(validacao_dados)
print("Taxa de acerto base: %f" % taxa_de_acerto_base)
