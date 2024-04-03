#G_22-47225-1_Week 08 


# Define a new cgraph
#dictionary for connection graph
#Each key in the dictionary represents a region, and the corresponding value is a list of other regions that are connected to the key region.
#For example, ‘WA’  is connected to ‘SA’ and ‘NT’
cgraph = {'WA': ['SA', 'NT'],
          'Q': ['SA', 'NT', 'NSW'],
          'T': [],
          'V': ['SA', 'NSW'],
          'SA': ['WA', 'NT', 'Q', 'NSW','V'],
          'NT': ['Q', 'WA', 'SA'],
          'NSW': ['Q', 'V', 'SA']}

remainingValues = {'WA': ['R','G','B'],
                    'Q': ['R','G','B'],
                    'T': ['R','G','B'],
                    'V':  ['R','G','B'],
                    'NT': ['R','G','B'],
                    'SA': ['R','G','B'],
                    'NSW': ['R','G','B']}

import random
#arguments: node (the current node to be colored), rv (a dictionary of remaining colors for each node), and cg (the connection graph)
def get_color(node, rv, cg):

    #randomly selects a color from the list of remaining colors for the current node
    color = random.choice(rv[node])
    # removes the current node from the rv dictionary, as it has now been colored and no longer needs to be considered
    rv.pop(node)
    # gets the list of nodes that are adjacent to the current node from the connection graph
    adjList = cg[node]
    # starts a loop that iterates over each node in the adjacency list
    for adj in adjList:
      #checks if the adjacent node is still in the rv dictionary
      # and if the color assigned to the current node is still in the list of remaining colors for the adjacent node
        if adj in rv.keys() and color in rv[adj]:
          #removes the color assigned to the current node from the list of remaining colors for the adjacent node.
            rv[adj].remove(color)
    #print(adjList)
    return color

## 1) Highest Degree Node


def get_hdnode(cg, solved={}):
    mnode = '' #initializes mnode (“maximum node”) as an empty string. This variable will hold the node with the highest degree.
    degree = -1
    for k in cg.keys():
        if len(cg[k])  > degree and k not in solved.keys():
            #print(k)
            degree = len(cg[k])
            mnode = k
    return mnode
get_hdnode(cgraph, {})

get_hdnode(cgraph, {'SA':'R'})

"""Color the nodes using Highest degree heuristic"""

assigned = {} # store assigned variables with colors
remainingValues = {'WA': ['R','G','B'],
                    'Q': ['R','G','B'],
                    'T': ['R','G','B'],
                    'V':  ['R','G','B'],
                    'NT': ['R','G','B'],
                    'SA': ['R','G','B'],
                    'NSW': ['R','G','B']}
for i in range(len(cgraph)):
    print('rv: ', end="")
    print(remainingValues)
    # assign color to the highest degree node
    selectedNode = get_hdnode(cgraph, assigned)
    print('Selected Node: '+selectedNode)
    color = get_color(selectedNode, remainingValues, cgraph)

    #check if ‘no color’ was returned, indicating that no colors were available for the selected node.
    # If so, it prints a failure message and breaks the loop.
    if color == 'no color':
        print('Failure: No color available for node ' + selectedNode)
        break
    assigned[selectedNode]= color
    print('assigned: ', end="")
    print(assigned)

remainingValues.keys()

## 2) Minimum Remaining Value


# define a method to select a node by MRV
def get_MRVnode(rv, solved):
    mrv_node = None # initializes mrv_node (“Minimum Remaining Values node”) as None
    min_values = float('inf') # initializes min_values as positive infinity

    #if the current node hasn’t been processed yet and if the number of remaining values
    # for the current node is less than the smallest number of remaining values found so far.
    for node, values in rv.items():
        if node not in solved and len(values) < min_values:
            min_values = len(values)
            mrv_node = node
    return mrv_node

"""Color the nodes using MRV heuristic"""

# Initialize an empty dictionary to store the colors assigned to each node
assigned = {}

# Initialize a dictionary with each node and its remaining available colors
remainingValues = {'WA': ['R','G','B'],
                    'Q': ['R','G','B'],
                    'T': ['R','G','B'],
                    'V':  ['R','G','B'],
                    'NT': ['R','G','B'],
                    'SA': ['R','G','B'],
                    'NSW': ['R','G','B']}

# Start a loop that will run for as many times as there are nodes in the graph
for i in range(len(cgraph)):
    # Print the current state of the remainingValues dictionary
    print('Remaining Values: ', end="")
    print(remainingValues)

    # Select the node with the fewest remaining colors that hasn't been colored yet
    selectedNode = get_MRVnode(remainingValues, assigned)
    print('Selected Node: '+selectedNode)

    # Assign a color to the selected node and update the remainingValues dictionary
    color = get_color(selectedNode, remainingValues, cgraph)

    # Check if 'no color' was returned, indicating that no colors were available for the selected node
    if color == 'no color':
        print('Failure: No color available for node ' + selectedNode)
        break

    # Add the selected node and its assigned color to the assigned dictionary
    assigned[selectedNode]= color

    # Print the current state of the assigned dictionary
    print('Assigned Colors: ', end="")
    print(assigned)

"""**3) Select node randomly**"""

# Define a function named 'get_RandomNode' that takes one argument 'rv'
def get_RandomNode(rv):
    # Create a list of the keys in the 'rv' dictionary, which represent the remaining nodes
    remaining_nodes = [k for k in rv.keys()]
    # Select a random node from the list of remaining nodes
    node = random.choice(remaining_nodes)
    # Return the selected node
    return node

import random

assigned = {}

remainingValues = {'WA': ['R','G','B'],
                    'Q': ['R','G','B'],
                    'T': ['R','G','B'],
                    'V':  ['R','G','B'],
                    'NT': ['R','G','B'],
                    'SA': ['R','G','B'],
                    'NSW': ['R','G','B']}

def get_RandomNode(rv):
    # randomly selects a node from the remaining nodes
    return random.choice(list(rv.keys()))

def get_color(node, rv, cg):
    # randomly selects a color from the list of remaining colors for the current node
    color = random.choice(rv[node])
    # checks if the selected color is adjacent to any other nodes with the same color
    for neighbor in cg[node]:
        if assigned.get(neighbor) == color:
            return 'no color'
    return color

for i in range(len(cgraph)):
    print(remainingValues)
    selectedNode = get_RandomNode(remainingValues)
    print('Selected Node: '+selectedNode)
    color = get_color(selectedNode, remainingValues, cgraph)

    # check if 'no color' is returned
    if color == 'no color':
        print('Failure: No color available for node ' + selectedNode)
        break

    assigned[selectedNode] = color
    print(assigned)

    # removes the current node from the rv dictionary, as it has now been colored and no longer needs to be considered
    remainingValues.pop(selectedNode)