import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Função para obter dados da API
def obter_dados_api():
    url = "https://pokeapi.co/api/v2/pokemon?limit=151"
    resposta = requests.get(url)
    dados = resposta.json()
    return dados["results"]

# Função para obter dados de tipos de Pokémon
def obter_dados_tipos(url):
    resposta = requests.get(url)
    dados = resposta.json()
    return [tipo["type"]["name"] for tipo in dados["types"]]

# Função principal para contar Pokémon por tipo e criar o gráfico
def contar_pokemons_por_tipo(pokemons):
    contagem_tipos = {}

    for pokemon in pokemons:
        url = pokemon["url"]
        tipos = obter_dados_tipos(url)

        for tipo in tipos:
            if tipo in contagem_tipos:
                contagem_tipos[tipo] += 1
            else:
                contagem_tipos[tipo] = 1

    return contagem_tipos

# Configuração do aplicativo
st.title("Contagem de Pokémon por Tipo")

# Obtenha os dados da API
pokemons = obter_dados_api()

# Conte os Pokémon por tipo
contagem_tipos = contar_pokemons_por_tipo(pokemons)

# Converta os dados para DataFrame
dados = pd.DataFrame(list(contagem_tipos.items()), columns=["Tipo", "Contagem"])

# Crie um gráfico de barras horizontais
fig, ax = plt.subplots()
ax.barh(dados["Tipo"], dados["Contagem"])  # Use barh para barras horizontais
ax.set_xlabel("Contagem")
ax.set_ylabel("Tipo de Pokémon")
ax.set_title("Contagem de Pokémon por Tipo")

# Exiba o gráfico no Streamlit
st.pyplot(fig)


# streamlit run exemplo_dataapp.py

