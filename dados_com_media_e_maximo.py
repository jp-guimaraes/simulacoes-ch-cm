# %%
import json

# Dados das cargas horárias por grupo
b = {
    "metadata": {
        "titulo": "Cargas Horárias por Grupo",
        "colunas": ["Grupo", "Media", "Maximo"]
    },
    "dados": [
        {
            "grupo": "Eletroeletronica",
            "media": 4.8,
            "maximo": 6
        },
        {
            "grupo": "EBM",
            "media": 4.6,
            "maximo": 6
        },
        {
            "grupo": "Jogos",
            "media": 1.0,
            "maximo": 2
        },
        {
            "grupo": "Manutencao",
            "media": 3.0,
            "maximo": 4
        },
        {
            "grupo": "Multimedia",
            "media": 0.0,
            "maximo": 0
        },
        {
            "grupo": "Redes",
            "media": 3.6,
            "maximo": 6
        },
        {
            "grupo": "SI",
            "media": 6.8,
            "maximo": 7
        }
    ]
}

info = {
    "metadata": {
        "titulo": "Cargas Horárias por Grupo",
        "colunas": ["Grupo", "Media", "Maximo"]
    },
    "dados": [
        {
            "grupo": "Eletroeletronica",
            "media": 6,
            "maximo": 7
        },
        {
            "grupo": "EBM",
            "media": 4.6,
            "maximo": 6
        },
        {
            "grupo": "Jogos",
            "media": 1.0,
            "maximo": 2
        },
        {
            "grupo": "Manutencao",
            "media": 5.0,
            "maximo": 7
        },
        {
            "grupo": "Multimedia",
            "media": 0.0,
            "maximo": 0
        },
        {
            "grupo": "Redes",
            "media": 7.6,
            "maximo": 9
        },
        {
            "grupo": "SI",
            "media": 10.8,
            "maximo": 12
        }
    ]
}


ebm = {
    "metadata": {
        "titulo": "Cargas Horárias por Grupo",
        "colunas": ["Grupo", "Media", "Maximo"]
    },
    "dados": [
        {
            "grupo": "Eletroeletronica",
            "media": 8,
            "maximo": 9
        },
        {
            "grupo": "EBM",
            "media": 8.9,
            "maximo": 12
        },
        {
            "grupo": "Jogos",
            "media": 1.0,
            "maximo": 2
        },
        {
            "grupo": "Manutencao",
            "media": 3.7,
            "maximo": 5
        },
        {
            "grupo": "Multimedia",
            "media": 0.0,
            "maximo": 0
        },
        {
            "grupo": "Redes",
            "media": 3.6,
            "maximo": 6
        },
        {
            "grupo": "SI",
            "media": 6.8,
            "maximo": 7
        }
    ]
}




jogos = {
    "metadata": {
        "titulo": "Cargas Horárias por Grupo",
        "colunas": ["Grupo", "Media", "Maximo"]
    },
    "dados": [
        {
            "grupo": "Eletroeletronica",
            "media": 4.8,
            "maximo": 6
        },
        {
            "grupo": "EBM",
            "media": 4.6,
            "maximo": 6
        },
        {
            "grupo": "Jogos",
            "media": 10.0,
            "maximo": 11
        },
        {
            "grupo": "Manutencao",
            "media": 3,
            "maximo": 4
        },
        {
            "grupo": "Multimedia",
            "media": 12,
            "maximo": 12
        },
        {
            "grupo": "Redes",
            "media": 5.6,
            "maximo": 8
        },
        {
            "grupo": "SI",
            "media": 6.8,
            "maximo": 7
        }
    ]
}


eletro = {
    "metadata": {
        "titulo": "Cargas Horárias por Grupo",
        "colunas": ["Grupo", "Media", "Maximo"]
    },
    "dados": [
        {
            "grupo": "Eletroeletronica",
            "media": 14.3,
            "maximo": 15
        },
        {
            "grupo": "EBM",
            "media": 4.6,
            "maximo": 6
        },
        {
            "grupo": "Jogos",
            "media": 1,
            "maximo": 2
        },
        {
            "grupo": "Manutencao",
            "media": 3,
            "maximo": 4
        },
        {
            "grupo": "Multimedia",
            "media": 0,
            "maximo": 0
        },
        {
            "grupo": "Redes",
            "media": 3.6,
            "maximo": 6
        },
        {
            "grupo": "SI",
            "media": 6.8,
            "maximo": 7
        }
    ]
}

