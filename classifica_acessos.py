from leitor_csv import load_csv
from sklearn.naive_bayes import MultinomialNB

X, Y = load_csv()

treino_dados = X[:90]
treino_marcacoes = Y[:90]

teste_dados = X[-9:]
teste_marcacoes = Y[-9:]

model = MultinomialNB()
model.fit(treino_dados, treino_marcacoes)

usuario = [1, 0, 1]

# print(model.predict([[1, 0, 1], [0, 1, 0]]))

resultados = model.predict(teste_dados)
diferencas = resultados - teste_marcacoes
acertos = [d for d in diferencas if d == 0]
total_acertos = len(acertos)
total_elemento = len(teste_dados)

taxa_acerto = 100.0 * total_acertos / total_elemento

print(taxa_acerto)
print(total_elemento)
