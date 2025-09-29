# %%

from dados import b, info, ebm, jogos, eletro
from util import *

# Exemplo de uso:
resultado = media_e_desvio(b)
print("Média:", resultado["media"])
print("Desvio padrão:", resultado["desvio"])

# Exemplo de uso:
caso_base_info = subtrai_dicts(info, b)
caso_base_ebm = subtrai_dicts(ebm, b)
caso_base_jogos = subtrai_dicts(jogos, b)
caso_base_eletro = subtrai_dicts(eletro, b)


# %%
# simulando carga horária 
info_5 = multiplica_dict(caso_base_info, 1.25)
ebm_5 = multiplica_dict(caso_base_ebm, 1.25)
jogos_5 = multiplica_dict(caso_base_jogos, 1.25)
eletro_5 = multiplica_dict(caso_base_eletro, 1.25)


soma_info_ebm = soma_dicts(info_5, ebm_5)
soma_jogos_eletro = soma_dicts(jogos_5, eletro_5)

soma_parcial = soma_dicts(soma_info_ebm, soma_jogos_eletro)
soma_total = soma_dicts(soma_parcial, b)





# print(json.dumps(soma_total, indent=2, ensure_ascii=False))


def calcula_soma_total(mult_info, mult_ebm, mult_jogos, mult_eletro):
    info_n = multiplica_dict(caso_base_info, mult_info)
    ebm_n = multiplica_dict(caso_base_ebm, mult_ebm)
    jogos_n = multiplica_dict(caso_base_jogos, mult_jogos)
    eletro_n = multiplica_dict(caso_base_eletro, mult_eletro)
    soma_total = soma_n_dicts(info_n, ebm_n, jogos_n, eletro_n, b)
    return soma_total

# # Exemplo de uso:
# soma_total_5555 = calcula_soma_total(1.25, 1.25, 1.25, 1.25)
# print(json.dumps(soma_total_5555, indent=2, ensure_ascii=False))
# print(media_e_desvio(soma_total_5555))

# soma_total_6464 = calcula_soma_total(1.5, 1, 1.5, 1)
# print(json.dumps(soma_total_6464, indent=2, ensure_ascii=False))
# print(media_e_desvio(soma_total_6464))
# %%

# # força bruta
# for info_mult in [1, 1.25, 1.5, 1.75, 2]:
#     for ebm_mult in [1, 1.25, 1.5, 1.75, 2]:
#         for jogos_mult in [1, 1.25, 1.5, 1.75, 2]:
#             for eletro_mult in [1, 1.25, 1.5, 1.75, 2]:
#                 aux = info_mult + ebm_mult + jogos_mult + eletro_mult
#                 if aux == 5.0:
#                     soma_total = calcula_soma_total(info_mult, ebm_mult, jogos_mult, eletro_mult)
#                     resultado = media_e_desvio(soma_total)
#                     print(json.dumps(soma_total, indent=2, ensure_ascii=False))
#                     print("indices: ", info_mult, ebm_mult, jogos_mult, eletro_mult)
    # %%
solucoes = 0
# força bruta
for info_mult in [1, 1.25, 1.5, 1.75, 2]:
    for ebm_mult in [1.5, 2]:
        for jogos_mult in [1, 1.25]:
            for eletro_mult in [1]:
                aux = info_mult + ebm_mult + jogos_mult + eletro_mult
                if aux == 5.0:
                    solucoes = solucoes + 1
                    soma_total = calcula_soma_total(info_mult, ebm_mult, jogos_mult, eletro_mult)
                    resultado = media_e_desvio(soma_total)
                    print(json.dumps(soma_total, indent=2, ensure_ascii=False))
                    print("indices: ", info_mult, ebm_mult, jogos_mult, eletro_mult)
                    print(media_e_desvio(soma_total))
                    input("Pressione Enter para continuar...")

print("Total de soluções: ", solucoes)