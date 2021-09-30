import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plot_data(x, y, title, x_label, y_label, legend):
	fig,plot1 = plt.subplots(1, 1)

	plot1.plot(x, y, 'r.-')
	plot1.set_title(title)
	plot1.set_xlabel(x_label)
	plot1.set_ylabel(y_label)
	plot1.grid(color='black', ls='-.', lw=0.25)
	plot1.legend(labels=[legend], loc='best')

df = pd.read_csv('./0840_Engg.txt', header = None, usecols = range(0, 32), sep = ' ')
df = pd.DataFrame(df)
#print(df.dtypes())
x = df[0]
y = df[3]
print(x)
#print(y)
plot_data(x, y, 'Mlp State', 'time(sec)-->', 'Mlp State-->', '1.Exp\n2.Exp2\n3.Exp3')
plt.show()

#plot_data();







