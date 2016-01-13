import pulp
import pandas as pd
import os
from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_knapsack(items,capacity):
    ''' solve the kanosack problem with a capacity constrain and a finxed number of items.
    items: array with value and weight
    capacity : max weight of the knapsack    
    '''
    value = [x.value for x in items]
    weight = [x.weight for x in items]

    nb_var = range(len(value))
    var_names = ['x'+str(n) for n in nb_var]
    X = []
    for i in nb_var:
        X.append(pulp.LpVariable(var_names[i], 0, 1, cat='Binary'))
    
#x = pulp.LpVariable("x", 0, 3)
#y = pulp.LpVariable("y", 0, 1)
    prob = pulp.LpProblem("Knapsack_weight", pulp.LpMaximize)
    
    prob += pulp.lpSum([weight[i]*X[i] for i in nb_var]) <= capacity
    prob += pulp.lpSum([value[i]*X[i] for i in nb_var])
    
    status = prob.solve()
    print pulp.LpStatus[status]
    for i in nb_var:
        print var_names[i]+":"+str(pulp.value(X[i]))
    
    optimal = '0'
    if pulp.LpStatus[status]=='Optimal':
        optimal = '1'
    
    total_value = sum([value[i]*pulp.value(X[i]) for i in nb_var])
    print "total value:", total_value
    taken = [int(pulp.value(X[i])) for i in nb_var]
    output_data = str(total_value) + ' ' + optimal + '\n'
    output_data += ' '.join(map(str, taken))
    print output_data
    return output_data
    

def load_file(filename):
    input_data_file = open(filename, 'r')
    input_data = ''.join(input_data_file.readlines())
    input_data_file.close()
    
    lines = input_data.split('\n')
    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])
    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    return input_data, items, capacity

directory = r'C:\Users\home\Documents\LinearProgramming\knapsack\data'
list_file = os.listdir(directory)
item_array = []
capacity_array = []
size =[]
for name in list_file:
    filename = directory + '\\'+ name    
    input_data, items, capacity = load_file(filename)
    size.append(len(items))
    
df = pd.DataFrame(list_file)
df['size']=size
df_sort = df.sort(size)

for name in df_sort[0]:
    filename = directory + '\\'+ name
    input_data, items, capacity = load_file(filename)
    print filename
    print len(items)
    if len(items)<200:
        solve_knapsack(items,capacity)