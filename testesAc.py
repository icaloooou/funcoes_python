##exercicio 1
#Escreva uma função com o nome pertence, que recebe como argumentos de entrada uma tupla e um item e retorna True,
#se o item estiver armazenado na tupla, e False, caso contrário.

def pertence(tupla, item):
    if item in tupla:
        return True
    else:
        return False

tupla = (2, 3, 4)
s = pertence(tupla, 3)
print(s)

##exercicio 2
#Escreva uma função chamada substituir que recebe como argumentos de entrada uma lista e dois itens (velho e novo)
#e retorna uma lista onde todas as ocorrências do item velho são substituídas pelo item novo. 

def substituir(lista, velho, novo):
    while velho in lista:
        item = lista.index(velho)
        lista[item] = novo
    return lista

lista = [1, 2, 2, 4]
lista = substituir(lista, 1, '45')
print(lista)

##exercicio 3
#Escreva uma função chamada posicoes_lista que recebe como argumentos de entrada uma lista e um item,
#e retorna uma lista contendo todas os índices em que o item aparece na lista. 

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
#Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista de notas. Escreva uma função chamada aprovados que recebe como
#argumentos de entrada o dicionário e retorna uma lista com o nome dos alunos aprovados (um aluno é aprovado quando a média das suas notas é maior ou igual a 6).

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
#Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista de notas. Escreva uma função chamada incluir_nota que recebe como argumentos
#de entrada o dicionário, o nome de um aluno e uma nota. A função deve inserir a nota na lista de notas do aluno correspondente e retornar o dicionário com
#as alterações realizadas.

def incluir_nota(alunos, nome, nota):
    if nome in alunos:
        alunos[nome].append(nota)
    return alunos

alunos = {'Ingrid': [4.5, 7.0, 10.0, 10.0], 'Denise': [9.0, 8.5], 'Ana Paula': [3.5, 1.0, 6.5], 'Marcelo': [9.0, 10.0, 7.0, 7.0]}
insercao = incluir_nota(alunos, 'Denise', 10.0)
print(insercao)

#exercicio 6
#Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista de notas. Escreva uma função chamada maiores_notas que recebe como argumentos 
#de entrada o dicionário e retorna outro dicionário com o nome e a maior nota de cada aluno.

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
