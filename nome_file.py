import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Creazione del dataframe con 10 righe e 4 colonne con valori casuali
df = pd.DataFrame(np.random.rand(10, 4), columns=['A', 'B', 'C', 'D'])

# Stile per evidenziare le colonne con colori diversi
column_color = {'A': 'lightblue', 'B': 'lightgreen', 'C': 'lightcoral', 'D': 'lightgoldenrodyellow'}
fig, ax = plt.subplots(figsize=(8, 6))
ax.axis('tight')
ax.axis('off') 

cell_colors = [[column_color[col]] * len(df) for col in df.columns]
cell_colors = list(map(list, zip(*cell_colors)))

table = ax.table(cellText=df.round(2).values, 
                 colLabels=df.columns, 
                 cellColours=cell_colors, 
                 cellLoc='center', 
                 loc='center')

plt.title("Highlighted DataFrame Columns")
plt.show()
