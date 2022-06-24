#Maya Carla Loleatha Anderson
#maya.anderson86@myhunter.cuny.edu
#this program prints avg. and max of pop in an asked borough

import matplotlib.pyplot as plt

import pandas as pd
pop = pd.read_csv('nycHistPop.csv', skiprows = 5)

borough = input("Enter borough: ")

print("Average population:", pop[borough].mean())
print("Maximum poopulation:", pop[borough].max())
