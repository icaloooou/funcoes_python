##exercicio 1
#Nesse exercicio deveriamos implementar a função 'pertence', que recebe dois parâmetros como entrada - uma tupla e um item - e que deveria retornar o valor True caso o item
#estivesse nessa tupla e False, caso não estivesse.

def pertence(tupla, item):
    if item in tupla:
        return True
    else:
        return False

tupla = (2, 3, 4)
s = pertence(tupla, 3)
print(s)

##exercicio 2 
#Nessa função chamada 'substituir', que recebe três parâmetros - uma lista, um item velho e um item novo - era necessário que fosse retornado uma lista onde todas as ocorrências
#do item velho fossem substituidos pelo item novo.

def substituir(lista, velho, novo):
    while velho in lista:
        item = lista.index(velho)
        lista[item] = novo
    return lista

lista = [1, 2, 2, 4]
lista = substituir(lista, 2, '45')
print(lista)

##exercicio 3
#A função 'posicoes_lista' deveria receber dois parâmetros - uma lista e um item - para que ela pudesse retornar uma outra lista apenas dos índices em que o item aparece.

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
#Na função 'aprovados' o objetivo era receber um dicionário como parâmetro e retornar uma lista com o nome dos alunos que foram aprovados. Lembrando que
#o dicionário deve conter como chave o nome dos alunos e como valor uma lista de notas. Um aluno só é aprovado com média acima ou igual a 6.

def aprovados(alunos):
    glorificados = []
    for a in alunos:
        notas = alunos[a]
        mediaCalculada = sum(notas) / len(alunos[a])
        if mediaCalculada >= 6:
            glorificados.append(a)
    return glorificados
    
alunos = {'Ingrid': [4.5, 7.0, 6.0, 3.0], 'Denise': [9.0, 8.5], 'Ana Paula': [3.5, 1.0, 6.5], 'Marcelo': [9.0, 10.0, 7.0, 7.0]}
ok = aprovados(alunos)
print(ok)

#exercicio 5
#A função 'incluir_nota' faria com que dentro de um dicionário, contendo como chave nome de alunos e como valor uma lista de notas, fosse possível incluir uma nota
#à algum aluno desejado. A função recebe três parâmetros: o dicionário, o nome do aluno em que a nota será atribuida e o valor da nota e no final deve retornar o dicionário com
#as atualização realizadas.

def incluir_nota(alunos, nome, nota):
    if nome in alunos:
        alunos[nome].append(nota)
    return alunos

alunos = {'Ingrid': [4.5, 7.0, 6.0, 3.0], 'Denise': [9.0, 8.5], 'Ana Paula': [3.5, 1.0, 6.5], 'Marcelo': [9.0, 10.0, 7.0, 7.0]}
insercao = incluir_nota(alunos, 'Denise', 10.0)
print(insercao)

#exercicio 6
#Nessa função o dicionário será igual as duas questões acima, o nome de um aluno como chave e como valor uma lista de notas. A função terá que receber como parâmetro esse 
#dicionário e devolver outro dicionário apenas com o nome dos alunos e suas maiores notas.

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
