#CA Assignment 1 - Q2 plot helper function
#Function : Takes input from Q2_table_helper.py and classifies the data into different types of miss_rates
#Name - Aditya Saini
#Roll number - 2018125
#Branch - B.Tech ECE

import ast
f = open('table.txt','rt')
#Converting the string input back into a dictionary
data = ast.literal_eval(f.read())

#Extracting the different cache sizes which were used for analysis
x = list(data.keys())

#Defining the different level of associations
assocs=[1,2,4,8]

# Convention for the following lists:
#
#   assocs_<assocs_level>_<miss_rate_type> : Represents the miss_rate values of type <miss_rate_type> at association level <assocs_level>
#   The different types of assocs_level are mentioned in the list 'assocs' = [1,2,4,8]
#
#   The different types of miss_rate_type are as follows:
#       <total> -->> Represents the total overall miss_rate
#       <inst> -->> Represents the overall miss_rate of cpu instructions
#       <data> -->> Represents the overall miss_rate of cpu data
#       <demand_total> -->> Represents the total demand miss_rate
assocs_1_total=[]
assocs_1_inst=[]
assocs_1_data=[]
assocs_1_demand_total=[]
assocs_2_total=[]
assocs_2_inst=[]
assocs_2_data=[]
assocs_2_demand_total=[]
assocs_4_total=[]
assocs_4_inst=[]
assocs_4_data=[]
assocs_4_demand_total=[]
assocs_8_total=[]
assocs_8_inst=[]
assocs_8_data=[]
assocs_8_demand_total=[]

#Iterating over the data and classifying the different miss_rate values
for cache_size in data:
    for val in data[cache_size][1]:
        if val[0] == 'system.l2cache.overall_miss_rate::total':
            assocs_1_total.append(val[1])
        if val[0] == 'system.l2cache.overall_miss_rate::.cpu.inst':
            assocs_1_inst.append(val[1])
        if val[0] == 'system.l2cache.overall_miss_rate::.cpu.data':
            assocs_1_data.append(val[1])
        if val[0] == 'system.l2cache.demand_miss_rate::total':
            assocs_1_demand_total.append(val[1])
    
    for val in data[cache_size][2]:
        if val[0] == 'system.l2cache.overall_miss_rate::total':
            assocs_2_total.append(val[1])
        if val[0] == 'system.l2cache.overall_miss_rate::.cpu.inst':
            assocs_2_inst.append(val[1])
        if val[0] == 'system.l2cache.overall_miss_rate::.cpu.data':
            assocs_2_data.append(val[1])
        if val[0] == 'system.l2cache.demand_miss_rate::total':
            assocs_2_demand_total.append(val[1])

    for val in data[cache_size][4]:
        if val[0] == 'system.l2cache.overall_miss_rate::total':
            assocs_4_total.append(val[1])
        if val[0] == 'system.l2cache.overall_miss_rate::.cpu.inst':
            assocs_4_inst.append(val[1])
        if val[0] == 'system.l2cache.overall_miss_rate::.cpu.data':
            assocs_4_data.append(val[1])
        if val[0] == 'system.l2cache.demand_miss_rate::total':
            assocs_4_demand_total.append(val[1])

    for val in data[cache_size][8]:
        if val[0] == 'system.l2cache.overall_miss_rate::total':
            assocs_8_total.append(val[1])
        if val[0] == 'system.l2cache.overall_miss_rate::.cpu.inst':
            assocs_8_inst.append(val[1])
        if val[0] == 'system.l2cache.overall_miss_rate::.cpu.data':
            assocs_8_data.append(val[1])
        if val[0] == 'system.l2cache.demand_miss_rate::total':
            assocs_8_demand_total.append(val[1])
            
#Finally printing all the values which we'll use for plotting
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