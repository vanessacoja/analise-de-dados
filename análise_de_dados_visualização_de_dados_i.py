# -*- coding: utf-8 -*-
"""Análise de Dados: Visualização de Dados I

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hN3BMKE_Qvshx0oJqQj2klo1Wok42Voz

Nestes exercícios, você deve decidir qual é o gráfico visto em aula que melhor visualiza uma base de dados. Após decidir, você deverá criar a visualização usando o conteúdo exposto durante a aula e adicionar um pequeno parágrafo sobre um insights que pode ser extraido do gráfico.

## 1\. Preço do diamante por tipo de corte
"""

import seaborn as sns

data = sns.load_dataset("diamonds")
data.head()

# @title price

from matplotlib import pyplot as plt
data['price'].plot(kind='hist', bins=20, title='price')
plt.gca().spines[['top', 'right',]].set_visible(False)

# gráfico do exercício 1
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

data['price'].plot(kind='hist', bins=20, title='PREÇO de diferentes diamantes', color='red')

# Removendo as bordas superior e direita do gráfico
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Exibindo o gráfico
plt.show()

"""**Insight do gráfico 1**: ...

---

## 2\. Número de passageiros em dezembro por ano
"""

import seaborn as sns

data = sns.load_dataset("flights")
data.head()

# gráfico do exercício 2

from matplotlib import pyplot as plt
import seaborn as sns
def _plot_series(series, series_name, series_index=0):
  palette = list(sns.palettes.mpl_palette('Dark2'))
  xs = series['year']
  ys = series['passengers']

  plt.plot(xs, ys, label=series_name, color=palette[series_index % len(palette)])

fig, ax = plt.subplots(figsize=(10, 5.2), layout='constrained')
df_sorted = data.sort_values('year', ascending=True)
_plot_series(df_sorted, '')
sns.despine(fig=fig, ax=ax)
plt.xlabel('year')
_ = plt.ylabel('passengers')

"""**Insight do gráfico 2**: ...

---

## 3\. Numero de passageiros por mês entre 1949 e 1959
"""

import seaborn as sns

data = sns.load_dataset("flights")
data.head()

# @title passengers

from matplotlib import pyplot as plt
data['passengers'].plot(kind='line', figsize=(8, 4), title='passengers')
plt.gca().spines[['top', 'right']].set_visible(False)



# gráfico do exercício 3

from matplotlib import pyplot as plt
data['passengers'].plot(kind='hist', bins=20, title='passengers')
plt.gca().spines[['top', 'right',]].set_visible(False)

from matplotlib import pyplot as plt
data['passengers'].plot(kind='line', figsize=(8, 4), title='passengers')
plt.gca().spines[['top', 'right']].set_visible(False)

"""**Insight do gráfico 3**: ...

---
"""