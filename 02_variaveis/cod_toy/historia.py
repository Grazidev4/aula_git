# 1. Entrada de dados
nome = input("Qual é o seu nome? ")
profissao = input("Qual a sua formação/profissão? ")
primeiro_adjetivo = input("O que você está achando da turma? ")
segundo_adjetivo = input("E o que está achando do instrutor? ")
primeira_comida = input("Qual a sua comida favorita? ")
segunda_comida = input("O que você gosta de tomar ou comer com ela? ")
sentimento = input("Como você se sente no final do dia? ")

# 2. Montagem da história
historia = (
    f"{nome} começou hoje o seu primeiro curso na Generation Brasil. "
    f"Está cursando a formação em {profissao}. "
    f"Achou a sua turma muito {primeiro_adjetivo} mas o instrutor era, no mínimo, {segundo_adjetivo}. "
    f"No almoço, comeu {primeira_comida} e {segunda_comida} enquanto revisava as suas anotações. "
    f"Ao final do dia, sente-se {sentimento}, mas tem a determinação de concluir a jornada."
)

# 3. Resultado final
print(historia)