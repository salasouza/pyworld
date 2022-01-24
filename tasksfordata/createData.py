import pandas as pd

a = {'Steps':['step_01','step_02',
               'step_03', 'step_04',
               'step_05','step_06',
              'Exit'],
     "Total": [100,80,70,60,50,30,70]}

steps = pd.DataFrame(a, index = ['step_01','step_02',
                'step_03', 'step_04',
                'step_05','step_06','step_07'])

steps.to_csv('trust/sankey.csv')
print(steps)
