import pandas as pd
from matplotlib import pyplot as plt

# Loading the Data
species = pd.read_csv('species_info.csv')

# print species.head()

species_count = species.scientific_name.nunique()
print species_count
species_type = species.category.unique()
print species_type
conservation_statuses = species.conservation_status.unique()
print conservation_statuses
