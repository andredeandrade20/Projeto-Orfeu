import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns

## Função faz a leitura dos dados e aplica o método chunks para ler cada parte dos dados separadamente e depois juntá-los novamente para otimizar a leitura
def loadData(file):
    chunks = []
    for chunk in pd.read_csv(file, encoding = 'UTF-8', low_memory = True, chunksize=1000):
        chunks.append(chunk)
    df = pd.concat(chunks)
    return df

df = loadData('dados.csv')

df['Tempo'] = pd.to_datetime(df['Tempo'])
df['Tempo'] = df['Tempo'].dt.strftime('%M:%S')

print(df.info())

plt.xlabel("Tempo(s)")
plt.ylabel("Intensidade (dB)")
plt.title('Projeto Orfeu: Intensidade x Tempo')
ax = sns.lineplot(data = df, x = 'Tempo', y = 'Intensidade')
ax.figure.set_size_inches(16, 8)

plt.savefig('teste.png')
