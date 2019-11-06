# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), '../../../../tmp'))
	print(os.getcwd())
except:
	pass
# %%
print("hello world")


# %%
import numpy as np 
np.__version__


# %%
from matplotlib import pyplot as plt
plt.style.use('default')


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

# %% [markdown]
# ## Getting things ready

# %%


