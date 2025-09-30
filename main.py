# %%

from dados import b, info, ebm, jogos, eletro
from util import *

# construindo casos base
caso_base_info = subtrai_dicts(info, b)
caso_base_ebm = subtrai_dicts(ebm, b)
caso_base_jogos = subtrai_dicts(jogos, b)
caso_base_eletro = subtrai_dicts(eletro, b)


# %% simulando carga horária 


def calcula_soma_total(mult_info, mult_jogos, mult_ebm, mult_eletro):
    info_n = multiplica_dict(caso_base_info, mult_info)
    ebm_n = multiplica_dict(caso_base_ebm, mult_ebm)
    jogos_n = multiplica_dict(caso_base_jogos, mult_jogos)
    eletro_n = multiplica_dict(caso_base_eletro, mult_eletro)
    soma_total = soma_n_dicts(info_n, ebm_n, jogos_n, eletro_n, b)
    return soma_total


print("------------------------------"*4)
cenario = [8,5,7,0]
parametros = [x/4 for x in cenario]
nome_cenario = "".join([str(x) for x in cenario])
print(f"cenário {nome_cenario}")
soma_total = calcula_soma_total(*parametros)
print(json.dumps(soma_total, indent=2, ensure_ascii=False))
print(media_e_desvio(soma_total))

