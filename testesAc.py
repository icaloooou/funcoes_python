'''
##exercicio 1
def pertence(tupla, item):
    if item in tupla:
        return True
    else:
        return False

tupla = (2, 3, 4)
s = pertence(tupla, 3)
print(s)

##exercicio 2
def substituir(lista, velho, novo):
    while velho in lista:
        item = lista.index(velho)
        lista[item] = novo
    return lista

lista = [1, 2, 2, 4]
lista = substituir(lista, 1, '45')
print(lista)

##exercicio 3
def posicoes_lista(lista, item):
    lista2 = lista[:]
    indices = []
    for x in lista2:
        if item in lista2:
            lugar = lista2.index(item)
            indices.append(lugar)
            lista2[lugar] = ' '
    return indices

lista = [1, 2, 3, 1, 4, 1]
print(lista)
s = posicoes_lista(lista, 1)
print(s)

#exercicio 4
def aprovados(alunos):
    glorificados = []
    for a in alunos:
        notas = alunos[a]
        mediaCalculada = sum(notas) / len(alunos[a])
        if mediaCalculada >= 6:
            glorificados.append(a)
    return glorificados
    
alunos = {'Ingrid': [4.5, 7.0, 10.0, 10.0], 'Denise': [9.0, 8.5], 'Ana Paula': [3.5, 1.0, 6.5], 'Marcelo': [9.0, 10.0, 7.0, 7.0]}
ok = aprovados(alunos)
print(ok)

#exercicio 5
def incluir_nota(alunos, nome, nota):
    if nome in alunos:
        alunos[nome].append(nota)
    return alunos

alunos = {'Ingrid': [4.5, 7.0, 10.0, 10.0], 'Denise': [9.0, 8.5], 'Ana Paula': [3.5, 1.0, 6.5], 'Marcelo': [9.0, 10.0, 7.0, 7.0]}
insercao = incluir_nota(alunos, 'Denise', 10.0)
print(insercao)
'''
#exercicio 6
def maiores_notas(alunos):
    maiores = {}
    for a in alunos:
        notas = alunos[a]
        notas = max(notas)
        maiores[a] = notas
    return maiores

alunos = {'Ingrid': [4.5, 7.0, 6.0, 3.0], 'Denise': [9.0, 8.5], 'Ana Paula': [3.5, 1.0, 6.5], 'Marcelo': [9.0, 10.0, 7.0, 7.0]}
n = maiores_notas(alunos)
print(n)
