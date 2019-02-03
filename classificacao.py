# Gordinho | Perna Curta | Faz Au Au ?

porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]
cachorro1 = [1, 1, 1]
cachorro2 = [0, 1, 1]
cachorro3 = [0, 1, 1]

dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

marcacoes = [1, 1, 1, -1, -1, -1]


from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [1, 0, 1]
misterioso4 = [1, 0, 1]
teste = [misterioso1, misterioso2, misterioso3, misterioso4]
modelo.fit(dados, marcacoes)
print(modelo.predict(teste))
