import json
from functools import reduce
import math

def subtrai_dicts(list1, list2):
    """
    Recebe duas listas no formato dos exemplos e retorna uma nova lista
    com a subtração do campo 'media' para cada grupo.
    """
    resultado = []
    for d1, d2 in zip(list1, list2):
        resultado.append({
            "grupo": d1["grupo"],
            "media": d1["media"] - d2["media"]
        })
    return resultado

def soma_dicts(list1, list2):
    """
    Recebe duas listas no formato dos exemplos e retorna uma nova lista
    com a soma do campo 'media' para cada grupo.
    """
    resultado = []
    for d1, d2 in zip(list1, list2):
        resultado.append({
            "grupo": d1["grupo"],
            "media": d1["media"] + d2["media"]
        })
    return resultado

def multiplica_dict(list1, n):
    """
    Recebe uma lista no formato dos exemplos e retorna uma nova lista
    com o campo 'media' multiplicado por n para cada grupo.
    """
    resultado = []
    for d in list1:
        resultado.append({
            "grupo": d["grupo"],
            "media": d["media"] * n
        })
    return resultado

def soma_n_dicts(*lists):
    """
    Soma N listas de dicionários no formato dos exemplos, usando soma_dicts.
    """
    return reduce(soma_dicts, lists)


def media_e_desvio(lista):
    """
    Recebe uma lista de dicionários no formato dos exemplos e retorna um dicionário
    com a média, o desvio padrão dos valores do campo 'media' e o grupo com maior média.
    """
    valores = [d["media"] for d in lista]
    n = len(valores)
    if n == 0:
        return {"media": 0, "desvio": 0, "maior_grupo": None}
    media = sum(valores) / n
    desvio = math.sqrt(sum((x - media) ** 2 for x in valores) / n)
    maior = max(lista, key=lambda d: d["media"])
    return {
        "media": media,
        "desvio": desvio,
        "maior_grupo": {
            "grupo": maior["grupo"],
            "media": maior["media"]
        }
    }
