# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.

print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
# Foi ignorado o cabeçalho. O enunciado diz para trazer as primeiras 20 amostras.
for line in data_list[1:21]:
    print(line)

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
# Como foi removido o cabeçalho no código, pode-se iniciar da primeira posição da lista.
for line in data_list[0:20]:
    print(line[6])

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data: list, index: int) -> list:
    """Adiciona as colunas de uma lista em outra lista com base no índice informado.

    Parâmetros
    ----------
    data: list
        A lista da qual os dados da coluna serão utilizados para retornar a nova lista.
    index: int
        Índice utilizado para se obter a coluna.

    Retorno
    -------
    list
        Uma lista contendo as informações obtidas da coluna.
    """
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for line in data:
        column_list.append(line[index])
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = 0
female = 0

# Como não se deve usar função, será usado um for para contar os itens. Será usada a função do item anterior para obter a lista com os gêneros.
for line in column_to_list(data_list, -2):
    if line == "Male":
        male += 1
    elif line == "Female":
        female += 1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list: list) -> list:
    """Conta a quantidade de ocorrências para cada gênero na base de dados.

    Parâmetros
    ----------
    data_list: list
        A lista a ser utilizada na contagem de gêneros.

    Retorno
    -------
    list
        Uma lista contendo as quantidades por gênero [masculino, feminino]
    """
    male = 0
    female = 0

    for line in column_to_list(data_list, -2):
        if line == "Male":
            male += 1
        elif line == "Female":
            female += 1

    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(data_list: list) -> str:
    """Verifica o gênero mais popular na base de dados.

    Parâmetros
    ----------
    data_list: list
        A lista da qual será verificado o gênero mais popular.

    Retorno
    -------
    str
        Retorna "Male" caso Masculino seja o gênero mais popular. Retorna "Female"
        caso o gênero mais popular seja Feminino. Retorna "Equal" caso a
        ocorrência dos gêneros seja igual.
    """
    answer = ""
    count_gender_list = count_gender(data_list)
    if count_gender_list[0] > count_gender_list[1]:
        answer = "Male"
    elif count_gender_list[0] < count_gender_list[1]:
        answer = "Female"
    else:
        answer = "Equal"

    return answer

print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

def count_user_type(data_list: list) -> list:
    """Realiza a contagem dos tipos de usuários na base de dados.

    Parâmetros
    ----------
    data_list: list
        A lista a ser utilizada na contagem de de tipos de usuário.

    Retorno
    -------
    list
        Uma lista contendo as quantidades por tipo de usuário [cliente, assinante, dependente]
    """
    customer = 0
    subscriber = 0
    dependent = 0

    for line in column_to_list(data_list, -3):
        if line == "Customer":
            customer += 1
        elif line == "Subscriber":
            subscriber += 1
        elif line == "Dependent":
            dependent += 1

    return [customer, subscriber, dependent]

types = ["Customer", "Subscriber", "Dependent"]
quantity = count_user_type(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de Usuário')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Pois a lista possui valores vazios para a coluna gênero."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.
count = 0
total = 0.

def list_string_to_float(list: list) -> list:
    """Transforma uma lista com dados do tipo str em uma lista do tipo float.

    Parâmetros
    ----------
    list: list
        A lista com dados do tipo str a serem convertidas em float.

    Retorno
    -------
    list
        Uma lista contendo os dados da lista de entrada convertidos ao tipo float.
    """
    float_list = []
    for line in list:
        float_list.append(float(line))
    return float_list

float_trip_duration_list = list_string_to_float(trip_duration_list)
for line in float_trip_duration_list:

    if min_trip == 0:
        min_trip = line
    elif line < min_trip:
        min_trip = line

    if max_trip == 0:
        max_trip = line
    elif line > max_trip:
        max_trip = line

    total += line
    count += 1

mean_trip = total/count

if count%2 == 1:
    median_trip = sorted(float_trip_duration_list)[count//2]
else:
    median_trip = sum(sorted(float_trip_duration_list)[count//2:count//2 + 1])/2

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:


input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list: list) -> list:
    """Conta a quantidade de ocorrências por valores presentes em uma lista.

    Parâmetros
    ----------
    column_list: list
        A lista com dados a serem contados.

    Retorno
    -------
    list
        Retorna uma lista contendo os distintos valores encontrados na lista e
        uma lista contendo as quantidades de suas ocorrências.
    """

    item_types = list(set(column_list))
    count_items = [0] * len(item_types)

    for line in column_list:
        i = 0
        while i < len(item_types):
            if item_types[i] == line:
                count_items[i] += 1
                break
            i += 1
    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -3)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------
