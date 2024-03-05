
def simple_reflex_agnt(percept):
    print('Received: '+ str(percept))
    location = percept[0]
    status = percept[1]
    if status != 'Clean':
        action = 'Clean Dirt'
    elif location == 'A':
        action = 'Go Right'
    elif location == 'B':
        action = 'Go Left'
    return action

import random

Location = random.choice(['A','B'])
Condition = random.choice(['Clean','Dirty'])

while True:
    action = simple_reflex_agnt((Location,Condition))
    print('Perfomed: '+ action)
    user_input = input('Type b to exit! or any key to continue.')
    if(user_input == 'b'): break
    if action == 'Go Right':
        Location = 'B'
        Condition = random.choice(['Clean','Dirty'])
    elif action == 'Go Left':
        Location = 'A'
    else:
        Condition = 'Clean'

