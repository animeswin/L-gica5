def calcular_media(notas):
    return sum(notas) / len(notas)

num_alunos = int(input("Digite o número de alunos: "))

medias = []

for _ in range(num_alunos):
    nome = input("Digite o nome do aluno: ")
    notas = []

    for i in range(1, 4):
        nota = float(input(f"Digite a nota {i} do {nome}: "))
        notas.append(nota)

    media = calcular_media(notas)
    medias.append(media)

    status = "aprovado" if media >= 7.0 else "reprovado"

    print(f"\nAluno: {nome}")
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Status: {status}\n")

media_geral = sum(medias) / len(medias) if medias else 0
print(f"Média geral da turma: {media_geral:.2f}")