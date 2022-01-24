import pandas as pd
import holoviews as hv
from holoviews import opts, dim
hv.extension('bokeh')
import matplotlib.pyplot as plt

sankey = hv.Sankey([
    ['a', 'b', 90],
    ['a', 'Desistência', 10],

    ['b', 'c', 80],
    ['b', 'Desistência', 10],

    ['c', 'd', 70],
    ['c', 'Desistência', 10],

    ['d', 'e', 60],
    ['d', 'Desistência', 60],

    ['e', 'f', 50],
    ['e', 'Desistência', 10],

    ['f', 'saiu', 40],
    ['f', 'Desistência', 10]
])


plt.sankey.opts(width=950, height=600, cmap='Set1',
            title = 'Jornada do Usuário - Pós Sucesso no PID')
plt.show()
