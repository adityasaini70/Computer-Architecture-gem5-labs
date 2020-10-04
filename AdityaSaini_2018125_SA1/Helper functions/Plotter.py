#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[30]:


assocs_1_total=['0.670935', '0.645967', '0.616837', '0.540973', '0.509923', '0.490077', '0.482714', '0.482074']
assocs_1_inst=['1', '1', '0.995536', '0.985119', '0.958333', '0.901786', '0.875000', '0.872024']
assocs_1_data=['0.580750', '0.548940', '0.513051', '0.419250', '0.387031', '0.377243', '0.375204', '0.375204']
assocs_1_demand_total=['0.670935', '0.645967', '0.616837', '0.540973', '0.509923', '0.490077', '0.482714', '0.482074']
assocs_2_total=['0.674136', '0.651088', '0.613636', '0.544494', '0.508323', '0.485275', '0.482394', '0.482074']
assocs_2_inst=['1', '1', '0.992560', '0.980655', '0.952381', '0.883929', '0.873512', '0.872024']
assocs_2_data=['0.584829', '0.555465', '0.509788', '0.424959', '0.386623', '0.376020', '0.375204', '0.375204']
assocs_2_demand_total=['0.674136', '0.651088', '0.613636', '0.544494', '0.508323', '0.485275', '0.482394', '0.482074']
assocs_4_total=['0.631882', '0.602113', '0.569782', '0.531050', '0.501921', '0.482074', '0.482074', '0.482074']
assocs_4_inst=['1', '1', '0.994048', '0.982143', '0.933036', '0.872024', '0.872024', '0.872024']
assocs_4_data=['0.530995', '0.493067', '0.453507', '0.407423', '0.383768', '0.375204', '0.375204', '0.375204']
assocs_4_demand_total=['0.631882', '0.602113', '0.569782', '0.531050', '0.501921', '0.482074', '0.482074', '0.482074']
assocs_8_total=['0.632202', '0.606914', '0.561140', '0.524008', '0.499680', '0.482074', '0.482074', '0.482074']
assocs_8_inst=['1', '1', '0.986607', '0.979167', '0.938988', '0.872024', '0.872024', '0.872024']
assocs_8_data=['0.531403', '0.499184', '0.444535', '0.399266', '0.379282', '0.375204', '0.375204', '0.375204']
assocs_8_demand_total=['0.632202', '0.606914', '0.561140', '0.524008', '0.499680', '0.482074', '0.482074', '0.482074']


# In[31]:


def helper(l):
    for i in range(len(l)):
        l[i]=float(l[i])

helper(assocs_1_total)
helper(assocs_1_inst)
helper(assocs_1_data)
helper(assocs_1_demand_total)

helper(assocs_2_total)
helper(assocs_2_inst)
helper(assocs_2_data)
helper(assocs_2_demand_total)

helper(assocs_4_total)
helper(assocs_4_inst)
helper(assocs_4_data)
helper(assocs_4_demand_total)

helper(assocs_8_total)
helper(assocs_8_inst)
helper(assocs_8_data)
helper(assocs_8_demand_total)


# In[32]:


print(assocs_1_total)
print(assocs_1_inst)
print(assocs_1_data)
print(assocs_1_demand_total)

print(assocs_2_total)
print(assocs_2_inst)
print(assocs_2_data)
print(assocs_2_demand_total)

print(assocs_4_total)
print(assocs_4_inst)
print(assocs_4_data)
print(assocs_4_demand_total)

print(assocs_8_total)
print(assocs_8_inst)
print(assocs_8_data)
print(assocs_8_demand_total)


# In[37]:


x=['4','8','16','32','64','256','512','1024']
plt.plot(x,assocs_1_total,lw=1, ls='-', marker='o', markersize=6, markerfacecolor="blue")
plt.plot(x,assocs_2_total,lw=1, ls='-', marker='o', markersize=6, markerfacecolor="yellow")
plt.plot(x,assocs_4_total,lw=1, ls='-', marker='o', markersize=6, markerfacecolor="green")
plt.plot(x,assocs_8_total,lw=1, ls='-', marker='o', markersize=6, markerfacecolor="red")
plt.xlabel('Memory size in kB')
plt.ylabel('L2 Cache total overall miss rate')
plt.legend(['1 way','2 way','4 way','8 way'], title = 'Association')
plt.savefig('test.png',dpi=600)


# In[55]:


table = zip(x, assocs_1_total,assocs_2_total,assocs_4_total,assocs_8_total)
table
from tabulate import tabulate
print(tabulate(table, headers=['Cache Memory in kB','Association Level = 1','Association Level = 2','Association Level = 4','Association Level = 8'], tablefmt="pretty"))


# In[39]:


x=['4','8','16','32','64','256','512','1024']
plt.plot(x,assocs_1_inst,lw=1, ls='-', marker='o', markersize=6, markerfacecolor="blue")
plt.plot(x,assocs_2_inst,lw=1, ls='-', marker='o', markersize=6, markerfacecolor="yellow")
plt.plot(x,assocs_4_inst,lw=1, ls='-', marker='o', markersize=6, markerfacecolor="green")
plt.plot(x,assocs_8_inst,lw=1, ls='-', marker='o', markersize=6, markerfacecolor="red")
plt.xlabel('Memory size in kB')
plt.ylabel('L2 Cache overall instruction miss rate')
plt.legend(['1 way','2 way','4 way','8 way'], title = 'Association')
plt.savefig('test.png',dpi=600)


# In[56]:


table = zip(x, assocs_1_inst,assocs_2_inst,assocs_4_inst,assocs_8_inst)
table
from tabulate import tabulate
print(tabulate(table, headers=['Cache Memory in kB','Association Level = 1','Association Level = 2','Association Level = 4','Association Level = 8'], tablefmt="pretty"))


# In[40]:


x=['4','8','16','32','64','256','512','1024']
plt.plot(x,assocs_1_data,lw=1, ls='-', marker='o', markersize=6, markerfacecolor="blue")
plt.plot(x,assocs_2_data,lw=1, ls='-', marker='o', markersize=6, markerfacecolor="yellow")
plt.plot(x,assocs_4_data,lw=1, ls='-', marker='o', markersize=6, markerfacecolor="green")
plt.plot(x,assocs_8_data,lw=1, ls='-', marker='o', markersize=6, markerfacecolor="red")
plt.xlabel('Memory size in kB')
plt.ylabel('L2 Cache overall data miss rate')
plt.legend(['1 way','2 way','4 way','8 way'], title = 'Association')
plt.savefig('test.png',dpi=600)


# In[57]:


table = zip(x, assocs_1_data,assocs_2_data,assocs_4_data,assocs_8_data)
table
from tabulate import tabulate
print(tabulate(table, headers=['Cache Memory in kB','Association Level = 1','Association Level = 2','Association Level = 4','Association Level = 8'], tablefmt="pretty"))


# In[36]:


x=['4','8','16','32','64','256','512','1024']
plt.plot(x,assocs_1_demand_total,lw=1, ls='-', marker='o', markersize=6, markerfacecolor="blue")
plt.plot(x,assocs_2_demand_total,lw=1, ls='-', marker='o', markersize=6, markerfacecolor="yellow")
plt.plot(x,assocs_4_demand_total,lw=1, ls='-', marker='o', markersize=6, markerfacecolor="green")
plt.plot(x,assocs_8_demand_total,lw=1, ls='-', marker='o', markersize=6, markerfacecolor="red")
plt.xlabel('Memory size in kB')
plt.ylabel('L2 Cache total demand miss rate')
plt.legend(['1 way','2 way','4 way','8 way'], title = 'Association')
plt.savefig('test.png',dpi=600)

