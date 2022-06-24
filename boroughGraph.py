#Maya Carla Loleatha Anderson
#maya.anderson86@myhunter.cuny.edu
#this program graphs fraction of an
#inputted boroughs population


import matplotlib.pyplot as plt

import pandas as pd
pop = pd.read_csv('nycHistPop.csv', skiprows = 5)
pop.plot(x = "Year")

borough = input("Enter borough name: ")
outputFile = input("Enter output file name: ")


pop['Fraction'] = pop[borough] / pop['Total']
pop.plot(x= 'Year', y='Fraction')

fig = plt.gcf()
fig.savefig(outputFile)
