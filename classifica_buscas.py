import pandas as pd
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv("busca_cursos.csv")
X_df = df[['home', 'busca', 'logado']]
Y_df = df['comprou']
X_dummies_df = pd.get_dummies(X_df)
Y_dummies_df = Y_df

## eficacia



X = X_dummies_df.values
Y = Y_dummies_df.values

acertos_de_um = len(Y[Y==1])
acerto_de_zero = len(Y[Y==0])

taxa_de_acerto_base = max(acertos_de_um, acerto_de_zero) / len(Y) * 100.0

print("Taxa de acerto base: {} %".format(taxa_de_acerto_base))

tamanho_de_treino = 0.9 * len(Y)
tamanho_de_teste = int(len(Y) - tamanho_de_treino)

treino_dados = X[:int(tamanho_de_treino)]
treino_marcacoes = Y[:int(tamanho_de_treino)]

teste_dados = X[-tamanho_de_teste:]
teste_marcacoes = Y[-tamanho_de_teste:]

model = MultinomialNB()
model.fit(treino_dados, treino_marcacoes)

resultados = model.predict(teste_dados)
diferencas = resultados - teste_marcacoes
acertos = [d for d in diferencas if d == 0]
total_acertos = len(acertos)
total_elemento = len(teste_dados)

taxa_acerto = 100.0 * total_acertos / total_elemento

print("Taxa de acerto do algoritmo: {} %".format(taxa_acerto))

