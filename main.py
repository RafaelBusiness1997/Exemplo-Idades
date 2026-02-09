"""Verifica se uma pessoa é maior ou menor de idade com base no ano de nascimento."""
import os
from datetime import date


def calcular_idade(para_ano_nascimento: int) -> int:
    """Calcula a idade com base no ano de nascimento."""
    ano_atual = date.today().year
    return ano_atual - para_ano_nascimento


def definir_categoria(para_idade: int) -> str:
    """Define categoria de utilizador dependendo da idade."""
    if para_idade < 10:
        return "Criança"
    elif para_idade < 18:
        return "Adolescente"
    elif para_idade < 65:
        return "Adulto"
    elif para_idade < 100:
        return "Sénior"
    else:
        return "Ancião"


if __name__ == "__main__":

    while True:

        try:
            ano_nascimento = int(input("Introduza o seu ano de nascimento: "))
            idade = calcular_idade(ano_nascimento)

            if ano_nascimento < 0 or idade < 0:
                print("Ano de nascimento inválido!")
                continue

            print(
                f"A idade para o ano de nascimento {ano_nascimento} é de {idade} anos.")
            print(f"É {definir_categoria(idade)}")

            continuar = input("Deseja continuar? (s/n)").lower()
            if continuar == "n":
                break
            os.system("cls")

        except ValueError as e:
            print("Erros: ", e)
            print("Introduza um valor válido")

    os.system("cls")
    print("Obrigado por utilizar o programa!")
