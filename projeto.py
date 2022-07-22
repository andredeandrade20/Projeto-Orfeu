## Importação das bibliotecas necessárias
import serial
import pyfirmata
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import warnings

## Supressão de avisos
warnings.filterwarnings('ignore')

## Inicia a conexão com o Arduino com os parâmetros da porta e velocidade
arduino = serial.Serial("COM4", 9600)

## Cria uma lista vazia onde serão armazendos os valores das leituras de som
som = []
data = []

## Cria um banco de dados onde os valores dos sensores serão colocados
df = pd.DataFrame({'Som':0, 'Tempo': 0}, index = [0])

## Função que lê os valores obtidos pelos sensores e inputa dentro do dataset criado
## Itera em um intervalo de 100 medidas
cont = 100
for c in range(cont):
    while (arduino.inWaiting() == 0):
        pass
## Faz a leitura dos dados do sensor e transforma em lista
    sensor = float(arduino.readline())
    som.append(sensor)
## Pega o horário que está sendo lido a medida e converte em lista
    time = datetime.now().time()
    time = str(time)
    data.append(time)
## Faz a junção de data e hora com os dados do sensor de som em um único dataframe
    df = pd.DataFrame({'Som': som, 'Tempo': data})
df = df.to_csv('dados.csv', mode = 'a', header = False)

print(df)

## Para a contagem do quando o sensor alcança 100 medidas e encerra a conexão com o arduino
arduino.close()
