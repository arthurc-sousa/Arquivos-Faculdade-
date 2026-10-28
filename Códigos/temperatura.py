#Cláudia Jacy Barenco Abbas
#13.10.2026
#Leitura de temperatura atual de algumas capitais do Brasil a partir de uma API na internet.

import urllib.request
import os
from datetime import datetime

capitais = [
    "São Paulo", "Rio de Janeiro", "Brasília", "Salvador", 
    "Belo Horizonte", "Curitiba", "Manaus", "Recife", "Porto Alegre"
]

#Cria matriz de coordenadas (latitude, longitude) para cada capital
coordenadas = [
    [-23.55, -46.63], # São Paulo
    [-22.91, -43.17], # Rio de Janeiro
    [-15.78, -47.93], # Brasília
    [-12.97, -38.51], # Salvador
    [-19.92, -43.94], # Belo Horizonte
    [-25.43, -49.27], # Curitiba
    [-3.10, -60.02],  # Manaus
    [-8.05, -34.88],  # Recife
    [-30.03, -51.23]  # Porto Alegre
]

temperaturas = []

for i in range(len(capitais)):
    lat = coordenadas[i][0] 
    lon = coordenadas[i][1] 
    
    url = "https://api.open-meteo.com/v1/forecast?latitude=" + str(lat) + "&longitude=" + str(lon) + "&current_weather=true"
    
    resposta = urllib.request.urlopen(url)
    texto = resposta.read().decode("utf-8")

    print(texto)
    os.system("pause")
    parte1 = texto.split('"temperature":"°C"')[1]
    parte1 = parte1.split('"temperature":')[1]
    valor_texto = parte1.split(',')[0]
    print(valor_texto)
    temperaturas.append(float(valor_texto))

print("--- TEMPERATURAS REAIS ---\n")
print("Data e hora da consulta:", datetime.now())
for i in range(len(capitais)):
    print(capitais[i], ":", temperaturas[i], "°C")

media = sum(temperaturas) / len(temperaturas)
temp_max = max(temperaturas)
temp_min = min(temperaturas)

posicao_max = temperaturas.index(temp_max)
posicao_min = temperaturas.index(temp_min)

print("\n--- ANÁLISE DOS DADOS ---")
print("Média da rede:", round(media, 2), "°C")
print("Mais quente:", capitais[posicao_max], "com", temp_max, "°C")
print("Mais fria:", capitais[posicao_min], "com", temp_min, "°C")