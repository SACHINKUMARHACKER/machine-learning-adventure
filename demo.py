#%%
# importing the required libraries
import numpy as np 
import pandas as pd 
import seaborn as sns 
from matplotlib import pyplot as plt 

# %%
print("first commit")
print(np.__version__)

# %%
x = np.linspace(0, 2, 100)

plt.plot(x, x , label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title('Simple Plot')

plt.legend()
plt.show()

# %%
plt.style.use('default')

# %%
