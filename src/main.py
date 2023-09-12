#%%
import pandas as pd 
from utils import get_random_string
from dotenv import load_dotenv
import os

load_dotenv()


#%% 

print(os.getenv("SUPER_SECRET_KEY"))
# %%

# this is an example of a function
get_random_string(10)
# %%
