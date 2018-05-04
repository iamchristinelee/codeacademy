import pandas as pd
from matplotlib import pyplot as plt

# Loading the Data
species = pd.read_csv('species_info.csv')

print species

species_count = species.scientific_name.nunique()
print species_count
species_type = species.category.unique()
print species_type
conservation_statuses = species.conservation_status.unique()
print conservation_statuses
#
#conservation_counts=species.groupby('conservation_status').scientific_name.nunique().reset_index()
#
#print conservation_counts

#species.fillna('No Intervention', inplace = True)
#
#
#conservation_counts_fixed=species.groupby('conservation_status').scientific_name.nunique().reset_index()
#print conservation_counts_fixed
#
#
#species = pd.read_csv('species_info.csv')
#
#species.fillna('No Intervention', inplace = True)
#
#protection_counts= species.groupby('conservation_status')\
#    .scientific_name.nunique().reset_index()\
#    .sort_values(by='scientific_name')
#    
#print protection_counts
#"""Create an axes objected called ax using plt.subplot.
#Create a bar chart whose heights are equal to the scientific_name column of protection_counts.
#Create an x-tick for each of the bars.
#Label each x-tick with the label from conservation_status in protection_counts.
#Label the y-axis Number of Species.
#Title the graph Conservation Status by Species
#Plot the graph using plt.show().
#"""
#plt.figure(figsize=(10,4))
#ax = plt.subplot()
#plt.bar(range(len(protection_counts.conservation_status)), protection_counts.scientific_name)
#ax.set_xticks(range(len(protection_counts.conservation_status)))
#ax.set_xticklabels(protection_counts.conservation_status)
#plt.ylabel('Number of Species')
#plt.title('Conservation Status by Species')
#plt.show()
#
#"""
#
#"""
#
#species['is_protected'] = species.conservation_status.apply(lambda x: 'True' if x != 'No Intervention' else 'False')
#
#print(species.head(5))
#
#
#species['is_protected'] = species.conservation_status != 'No Intervention'
#
#category_counts = species.groupby(['category', 'is_protected']).scientific_name.nunique().reset_index()
#
#print category_counts.head()
#
#category_pivot = category_counts.pivot(columns='is_protected',
#                      index='category',
#                      values='scientific_name')\
#                      .reset_index()
#  
#print category_pivot
#
#category_pivot.columns=['category','not_protected','protected']
#
#category_pivot['percent_protected']=category_pivot.protected/(category_pivot.protected + category_pivot.not_protected)
#
#print(category_pivot.head(5))
